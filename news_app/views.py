from django.shortcuts import render
from .models import Story, Job, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def index(request):
    context = {}
    stories = Story.objects.all().order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(stories, 15)
    try:
        mystories = paginator.page(page)
    except PageNotAnInteger:
        mystories = paginator.page(1)
    except EmptyPage:
        mystories = paginator.page(paginator.num_pages)

    context['stories'] = mystories
    context['total_stories'] = stories.count()
    # context['total_stories'] = stories

    return render(request, 'news_app/index.html', context)


def job_view(request):
    context = {}
    jobs = Job.objects.all().order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(jobs, 15)
    try:
        myjobs = paginator.page(page)
    except PageNotAnInteger:
        myjobs = paginator.page(1)
    except EmptyPage:
        myjobs = paginator.page(paginator.num_pages)

    context['jobs'] = myjobs
    context['total_jobs'] = jobs.count()
    return render(request, 'news_app/job.html', context)


def detail_view(request, pk):
    context = {}
    story_detail = Story.objects.get(pk=pk)
    comments = Comment.objects.filter(story_id=pk)

    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 5)
    try:
        comment = paginator.page(page)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment = paginator.page(paginator.num_pages)

    context['story_detail'] = story_detail
    context['story_comments'] = comment

    return render(request, 'news_app/detail.html', context)


def search(request):
    context = {}
    stories = Story.objects.all().order_by('-created')

    search = request.POST['search']
    if search == 'job':
        context['job_results'] = Job.objects.filter(
            item_type=search).order_by('-created')
    else:
        stories = Story.objects.filter(Q(author__icontains=search) | Q(
            item_type__icontains=search) | Q(title__icontains=search)).order_by('-created')
        page = request.GET.get('page', 1)
        paginator = Paginator(stories, 15)
        try:
            story_results = paginator.page(page)
        except PageNotAnInteger:
            story_results = paginator.page(1)
        except EmptyPage:
            story_results = paginator.page(paginator.num_pages)

    context['story_results'] = story_results
    context['stories'] = stories

    return render(request, 'news_app/search.html', context)


