from django.contrib import admin
from django.urls import path
from . import views
from .views import PositiveListView,PostDetailView,PostCreateview
urlpatterns = [
    path("",PositiveListView.as_view(), name="blog-home"),
    path("about/",views.about, name="blog-about"),
    path("post/new",PostCreateview.as_view(), name="post-create"),
    path("post/<int:pk>/",PostDetailView.as_view() , name="post-detail")
]
