import json
import os
from datetime import datetime
from difflib import get_close_matches
from itertools import chain

import django_rq
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.db.models import Count, Q
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView

from core.utils import get_rqworker_count, wiki_summary

from .models import Abbr

BACKUP_FILE_NAME = "Abbr_backup.json"
BACKUP_FILE_FULLPATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), BACKUP_FILE_NAME)
# LASTDIR_AND_FILENAME = os.path.join(os.path.basename(os.path.split(BACKUP_FILE_FULLPATH)[0]), BACKUP_FILE_NAME)


class AbbrDetailView(DetailView):
    model = Abbr
    template_name = "abbr/abbr_detail.html"

    def get(self, request, **kwargs):
        self.object = self.get_object()
        # needs 404 handling

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class AbbrListView(ListView):
    model = Abbr
    template_name = "abbr/abbr_list.html"
    context_object_name = "abbr_list"

    def get_backup_count(self):
        if not os.path.exists(BACKUP_FILE_FULLPATH):
            return 0

        data = open(BACKUP_FILE_FULLPATH)
        try:
            json_data = json.load(data)
        except:
            return 0

        return len(json_data)

    @property
    def count_difference(self):
        return Abbr.objects.count() - self.get_backup_count()

    def last_backup_time(self):
        if os.path.exists(BACKUP_FILE_FULLPATH):
            return datetime.fromtimestamp(os.stat(BACKUP_FILE_FULLPATH).st_mtime)
        else:
            # return 'never'
            return datetime.strptime("1981/09/08", "%Y/%m/%d")

    def time_diff_last_download_and_last_change(self):
        # download has no timezone info...
        last_download = self.last_backup_time()
        last_change = Abbr().last_change_date().replace(tzinfo=None)
        diff = abs(last_change - last_download).days
        return diff

    def get_queryset(self):
        queryset = super().get_queryset()
        if "q" in self.request.GET:
            q = self.request.GET.get("q").strip()
            if q:
                startswith_match = queryset.filter(name__istartswith=q).order_by(Lower("name"), Lower("description"))

                other_match = (
                    queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
                    .exclude(name__istartswith=q)
                    .order_by(Lower("name"), Lower("description"))
                )

                result = list(chain(startswith_match, other_match))
                return result

        return Abbr.objects.order_by("name")
        # return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        context["last_backup_time"] = self.last_backup_time()
        context["backup_name"] = BACKUP_FILE_NAME
        context["backup_exists"] = os.path.exists(BACKUP_FILE_FULLPATH)
        context["backup_count"] = self.get_backup_count()
        context["total_count"] = Abbr.objects.count()
        context["count_diff"] = self.count_difference
        context["last_change_date"] = Abbr().last_change_date()
        # context['change_diff'] = self.time_diff_last_download_and_last_change()

        q = self.request.GET.get("q")
        if q is not None and len(Abbr.objects.filter(description__icontains=q)) == 0:
            abbrs = Abbr.objects.all()
            possible_matches = get_close_matches(q, [abbr.description for abbr in abbrs])

            if possible_matches:
                context["possible_matches"] = Abbr.objects.filter(description__in=possible_matches)

        return context


def save_wiki_summary(name, description):
    abbr = get_object_or_404(Abbr, name=name, description=description)
    try:
        wiki = wiki_summary(abbr.description)
        if len(wiki) <= 0:
            print(f"wiki summary NOT retrieved: {abbr.name} ({abbr.description})", "RED")
            return
        abbr.wiki = wiki
        abbr.save()
        print(f"wiki summary saved: {abbr.name} ({abbr.description})", "GREEN")
    except:
        """
        make this exception specific
        """
        print(f"wiki summary NOT saved: {abbr.name} ({abbr.description})", "RED")


def save_wiki_summary_for_all(request):
    print("save_wiki_summary_for_all", "YELLOW")
    if get_rqworker_count() <= 0:
        messages.error(request, f"rqworker not on!")
        return HttpResponseRedirect(reverse("abbr:list"))
    queue = django_rq.get_queue("default")

    count = 1
    abbrs = Abbr.objects.all()
    for abbr in abbrs:
        # print(f'{count} - {abbr.name}: {abbr.description}')
        queue.enqueue(save_wiki_summary, abbr.name, abbr.description)
        count += 1

    messages.success(request, f"{count} wiki summaries enqueued for saving")
    return HttpResponseRedirect(reverse("abbr:list"))


def generate_json(request):
    data = []
    DATA_PATH = "./frontend/data.json"

    abbrs = Abbr.objects.all()
    for a in abbrs:
        row = {
            "id": a.id,
            "name": a.name,
            "description": a.description,
            # "wiki": a.wiki,
        }
        data.append(row)

    with open(DATA_PATH, "w") as file:
        file.write(json.dumps(data))

    messages.success(request, f"Json({len(data)}) generated to {DATA_PATH}")

    return HttpResponseRedirect(reverse("abbr:list"))


def download_json(request):

    with open(BACKUP_FILE_FULLPATH, "w") as out:
        try:
            queryset = Abbr.objects.all()
            count = queryset.count()
            if count > 0:
                jsonSerializer = serializers.get_serializer("json")
                json_serializer = jsonSerializer()
                # json_serializer.serialize(Abbr.objects.all(), stream=out, fields=('name', 'description'))
                json_serializer.serialize(queryset, stream=out)
                messages.success(request, f"{count} abbrs downloaded in '{BACKUP_FILE_FULLPATH}'")
            else:
                messages.warning(request, "no abbrs to download")

        except Exception as e:
            messages.warning(request, "download_json failed:" + e)

    return HttpResponseRedirect(reverse("abbr:list"))


def upload_json(request):
    if not os.path.exists(BACKUP_FILE_FULLPATH):
        messages.error(request, f"path doesn't exist: {BACKUP_FILE_FULLPATH}")
        return HttpResponseRedirect(reverse("abbr:list"))

    # print(filename)
    data = open(BACKUP_FILE_FULLPATH)
    try:
        json_data = json.load(data)
    except:
        # possibly no data inside the json file
        messages.error(request, "upload_json: json.load(data) failed - check backup file")
        return HttpResponseRedirect(reverse("abbr:list"))

    for row in json_data:
        name = row["fields"]["name"]
        description = row["fields"]["description"]
        description_ae = row["fields"]["description_ae"]

        Abbr.objects.get_or_create(name=name, description=description, description_ae=description_ae)

    messages.success(request, "upload_json: " + str(len(json_data)) + " abbrs saved")
    return HttpResponseRedirect(reverse("abbr:list"))
