import requests
from news_app.models import Story, Job, Comment
from datetime import datetime


def get_item_by_id(id):
    url = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty'
    rep = requests.get(url)
    reps = rep.json()
    return reps


def get_stories_id():
    url = "https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty"
    rep = requests.get(url)
    reps = rep.json()
    return reps


def get_latest_hundred_items():
    latest_100 = []
    id = get_stories_id()
    count = 0
    while id > 0:
        url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"
        rep = requests.get(url)
        reps = rep.json()
        latest_100.append(reps)
        id -= 1
        count += 1
        if count == 100:
            break
    return latest_100


def save_latest_item_to_db():
    items = get_latest_hundred_items()
    for item in items:
        print(item)
        if item['type'] == 'job':
            job_id = item['id']
            item_type = item['type']
            try:
                job_poster = item['by']
                job_title = item['title']
                job_link = item['url']
            except KeyError:
                job_poster = 'Anonymous'
                job_title = ''
                job_link = ''
            time = convert_unix_time(item['time'])

            save_to_job(job_id, job_poster, job_title,
                        job_link, item_type, time)
        elif item['type'] == 'story':
            story_id = item['id']
            item_type = item['type']
            try:
                story_author = item['by']
                story_title = item['title']
                story_link = item['url']
            except KeyError:
                story_author = 'Anonymous'
                story_title = ''
                story_link = ''
            time = convert_unix_time(item['time'])

            save_to_story(story_id, story_author, story_title,
                          story_link, item_type, time)
            try:
                comments = item['kids']
            except KeyError:
                continue
            for comment_id in comments:
                comment = get_item_by_id(comment_id)
                try:
                    story = Story.objects.get(id=comment['parent'])
                    commenter = comment['by']
                    text = comment['text']
                except KeyError:
                    commenter = 'Anonymous'
                    text = ''
                except TypeError:
                    continue
                save_to_comment(comment['id'], story, commenter, text,
                                comment['type'], convert_unix_time(comment['time']))
        elif item['type'] == 'comment':
            # comment_id = item['id']
            story = get_item_by_id(item['parent'])
            if story['type'] == 'story':
                try:
                    story_link = story['url']
                except KeyError:
                    story_link = ''
                save_to_story(story['id'], story['by'], story['title'],
                              story_link, story['type'], convert_unix_time(story['time']))
                try:
                    comments = story['kids']
                except KeyError:
                    continue
                for comment_id in comments:
                    comment = get_item_by_id(comment_id)
                    try:
                        story = Story.objects.get(id=comment['parent'])
                        commenter = comment['by']
                        text = comment['text']
                    except KeyError:
                        commenter = 'Anonymous'
                        text = ''
                    except TypeError:
                        continue
                    save_to_comment(comment['id'], story, commenter, text,
                                    comment['type'], convert_unix_time(comment['time']))
            else:
                continue
            # commenter = item['by']
            # comment = item['text']
            # item_type = item['type']
            # time = convert_unix_time(item['time'])

            # save_to_comment(comment_id, story_id,
            #                 commenter, comment, item_type, time)
            # except ValueError:
            #     comment_id = item['id']
            #     story_id = item['parent']
            #     story = get_item_by_id(story_id)
            #     if story['type'] == 'story':
            #         save_to_story(story['id'], story['by'], story['title'],
            #                     story['descendants'], story['url'], story['type'], convert_unix_time(story['time']))
            #     commenter = item['by']
            #     comment = item['text']
            #     item_type = item['type']
            #     time = convert_unix_time(item['time'])

            #     save_to_comment(comment_id, story_id,
            #                     commenter, comment, item_type, time)


def save_to_story(story_id, author, title, link, item_type, time):
    story = Story(
        id=story_id,
        author=author,
        title=title,
        story_link=link,
        item_type=item_type,
        created=time
    )
    story.save()


def save_to_comment(comment_id, story, commenter, comment, item_type, time):
    comment = Comment(
        id=comment_id,
        story_id=story,
        commenter=commenter,
        comment=comment,
        item_type=item_type,
        created=time
    )
    comment.save()


def save_to_job(job_id, poster, title, post, link, item_type, time):
    job = Job(
        id=job_id,
        job_poster=poster,
        job_title=title,
        jon_link=link,
        item_type=item_type,
        created=time
    )
    job.save()


def convert_unix_time(unix_time):
    time = int(unix_time)
    dt = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    return dt
