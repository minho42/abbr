from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from abbrapp.models import TimeStampedModel


class Abbr(TimeStampedModel):
    # name & description, should be unique case insensitive
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, help_text="british english")
    wiki = models.CharField(max_length=9999, null=True, blank=True, help_text="wikipedia summary")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", "description"]
        # comment unique_together before /uploadjson/
        unique_together = [["name", "description"]]

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    def last_change_date(self):
        if Abbr.objects.count() <= 0:
            return None
        return Abbr.objects.order_by("-modified").first().modified

    def days_since_last_change(self):
        now = timezone.now()
        last_mofify = self.last_change_date()
        days = (now - last_mofify).days
        return days
