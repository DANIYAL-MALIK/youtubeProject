from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
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
        'posts':posts
    }
    return render(request, 'blog/home.html',context)
def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
