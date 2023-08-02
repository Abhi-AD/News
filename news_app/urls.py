from django.urls import path
from news_app import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path(
        "post-by-category/<int:category_id>/",
        views.PostByCategoryView.as_view(),
        name="post-by-category",
    ),
    path(
        "post-by-tag/<int:tag_id>/", views.PostByTagView.as_view(), name="post-by-tag"
    ),
    path(
        "post-comment/", views.CommentView.as_view(), name="post-comment"
        ),
    path(
        "post-search/", views.PostSearchView.as_view(), name="post-search"
    )
]
