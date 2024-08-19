import requests as req
import json


jobnews = json.loads(req.get('https://hacker-news.firebaseio.com/v0/jobstories.json').text)
print(jobnews)

pagecontent=""
for item in jobnews:
    job = json.loads(req.get(f'https://hacker-news.firebaseio.com/v0/item/{item}.json').text)
    print(f'{item}: title: {type(job.keys())}')
    title = job["title"]
    date = job["time"]

    article = """
    <article>
        <header>
            <hgroup>
                <h2>{}</h2>
                <h3>{author} - {source} - {date}</h3>
            </hgroup>
        </header>
        <div class="grid">
            <p>{description}</p>
            <img src="{imageUrl}" alt="Picture from {source}">
        </div>
        <footer>
            <a href="{url}" role="button">Source: {source}</a>
        </footer>
    </article>
    """