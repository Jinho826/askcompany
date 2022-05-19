from django.urls import path,register_converter
from . import views

app_name = "instagram"

class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value

register_converter(YearConverter, 'year')

urlpatterns = [
    path('', views.post_list, name = "post_list"),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # path('archives/<year:year>/', views.archives_year),
    path('post_archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year')

]