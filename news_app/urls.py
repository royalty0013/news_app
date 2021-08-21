from django.urls import path
from .views import (
    index,
    job_view,
    detail_view,
    search,
)

app_name = 'news_app'

urlpatterns = [
    path('', index, name="index"),
    path('job/', job_view, name="job-view"),
    path('detail/<int:pk>/', detail_view, name='detail'),
    path('search/', search, name='search')
]
