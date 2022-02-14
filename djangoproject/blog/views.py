from django.shortcuts import render
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
from .models import Post
posts=[
    {
        'author':'Daniyal Malik',
        'title': 'I Love Django',
        'content':'First post',
        'date_posted':'August 19 2021'
    },
    {
        'author':'Haji Abdul-Rehman',
        'title': 'I Love Machine Learning',
        'content':'Second Post post',
        'date_posted':'August 14 2021'
    }
]
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)
def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
class PositiveListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
class PostDetailView(DetailView):
    model=Post
    template_name='blog/post_detail.html'
class PostCreateview(LoginRequiredMixin,CreateView):
    model=Post
    template_name='blog/post_form.html'
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    template_name='blog/post_form.html'
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name='blog/post_confirm_delete.html'
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
