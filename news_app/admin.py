from django.contrib import admin
from news_app.models import Job, Story, Comment

# Register your models here.

admin.site.index_title = 'News App'
admin.site.site_header = 'News App'
admin.site.site_title = 'News App'


class StoryAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'story_link',
                    'item_type', 'news_image', 'created']


admin.site.register(Story, StoryAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ['job_poster', 'job_title',
                    'item_type', 'job_link', 'created']


admin.site.register(Job, JobAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['story_id', 'commenter', 'comment', 'item_type', 'created']


admin.site.register(Comment, CommentAdmin)
