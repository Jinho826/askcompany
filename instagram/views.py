from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html',{
        'post_list' : qs,
        'q' : q
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'instagram/post_detail.html',{
        'post' : post
    })

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")