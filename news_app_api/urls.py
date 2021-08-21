from django.urls import path
from .views import (
    ItemsList,
    JobDetail,
    StoryDetail,
    CommentDetail
 
)


app_name = 'news_app_api'

urlpatterns = [
    path('items/<str:item>/', ItemsList.as_view(), name='items'),
    path('job-detail/', JobDetail.as_view(), name='job-detail'),
    path('story-detail/', StoryDetail.as_view(), name='story-detail'),
    path('comment-detail/', CommentDetail.as_view(), name='comment-detail')
    # path('post-story/', PostStory.as_view(), name='post-story')
]