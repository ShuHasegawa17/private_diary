from django.urls import path
from . import views

app_name = "diary"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("inquiry/", views.InquiryView.as_view(), name="inquiry"),
    path("diary_list/", views.DiaryListView.as_view(), name="diary_list"),
    path(
        "diary-detail/<int:id>/", views.DiaryDetailView.as_view(), name="diary_detail"
    ),
]
