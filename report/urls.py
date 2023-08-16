from django.urls import path
from report import views

app_name = "report"
urlpatterns = [
     path("users/", views.UserReportView.as_view(), name="users"),
     path("post-pdf-download/", views.PDFFileDownloadView.as_view(), name="post-pdf-download"),
     path("post-pdf-view/", views.PostPdfFileView.as_view(), name="post-pdf-view"),
]