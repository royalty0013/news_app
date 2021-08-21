from django.db import models
from django.db.models.fields import CharField, URLField
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.

NEWS_TYPE = (
    ('job', 'job'),
    ('story', 'story'),
    ('comment', 'comment'),
    ('poll', 'poll'),
    ('pollopt', 'pollopt'),
)


class Story(models.Model):
    author = models.CharField(max_length=50, null=True,
                              blank=True, default='Anonymous')
    title = models.CharField(max_length=200, null=True, blank=True)
    story_link = models.URLField(max_length=200, null=True, blank=True)
    item_type = models.CharField(
        max_length=30, choices=NEWS_TYPE, default='story')
    news_image = models.ImageField(
        upload_to='news_image', default='no_image.png')
    created = models.DateTimeField(blank=True, default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_app:detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    story_id = models.ForeignKey(
        Story, on_delete=models.CASCADE, null=True, blank=True)
    commenter = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    item_type = models.CharField(
        max_length=30, choices=NEWS_TYPE, default='comment')
    created = models.DateTimeField(blank=True, default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commenter


class Job(models.Model):
    job_poster = models.CharField(
        max_length=50, null=True, default='Anonymous')
    job_title = models.CharField(max_length=200, null=True)
    item_type = models.CharField(
        max_length=50, choices=NEWS_TYPE, default='job')
    job_link = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.job_title
