from django.contrib import admin
from django.urls import path
from . import views
from .views import PositiveListView,UserPositiveListView,PostDetailView,PostCreateview,PostUpdateview,PostDeleteView
urlpatterns = [
    path("",PositiveListView.as_view(), name="blog-home"),
    path("user/<str:username>",UserPositiveListView.as_view(), name="user-posts"),
    path("about/",views.about, name="blog-about"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/new",PostCreateview.as_view(), name="post-create"),
    path("post/<int:pk>/",PostDetailView.as_view() , name="post-detail"),
    path("post/<int:pk>/update",PostUpdateview.as_view() , name="post-update")

]
