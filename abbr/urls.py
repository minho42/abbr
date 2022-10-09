from django.urls import path

from . import views

app_name = "abbr"

urlpatterns = [
    path("", views.AbbrListView.as_view(), name="list"),
    path("<int:pk>/", views.AbbrDetailView.as_view(), name="detail"),
    path("uploadjson/", views.upload_json, name="uploadjson"),
    path("generate-json/", views.generate_json, name="generatejson"),
    path("downloadjson/", views.download_json, name="downloadjson"),
    path(
        "save_wiki_summary_for_all/",
        views.save_wiki_summary_for_all,
        name="save_wiki_summary_for_all",
    ),
]
