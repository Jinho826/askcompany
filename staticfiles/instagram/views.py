from django.http import HttpResponse, HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, ListView, ArchiveIndexView, YearArchiveView
from django.contrib.auth.decorators import login_required

# post_list = ListView.as_view(model=Post, paginate_by=10)

# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html',{
#         'post_list' : qs,
#         'q' : q
#     })

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()



# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'instagram/post_detail.html',{
#         'post' : post
#     })

post_detail = DetailView.as_view(model=Post, )

# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='create_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)