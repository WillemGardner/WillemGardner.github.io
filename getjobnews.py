import requests as req
import json
import datetime


jobnews = json.loads(req.get('https://hacker-news.firebaseio.com/v0/jobstories.json').text)
#print(jobnews)

htmlpagetemplate = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<link rel="icon" type="image/x-icon" href="images/favicon/favicon.ico">
<title>WG Tech News</title>
<meta name="description" content="Willem Gardner: Sample Webpage on GitHub">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="css/pico.min.css">
<link rel="stylesheet" href="css/mystyles.css">
<script src="script.js" type="text/javascript"></script>
</head>
<body>
<header class="container">
    <nav class="navbar">
        <ul>
            <li><a href="#" class="outline icon" onclick="toggleDropdown()" role="button" style="font-size:x-large;">&#9776;</a></li>
        </ul>
        <ul>
            <li><strong class="biggerfont">Willem Gardner</strong></li>
        </ul>
        <ul class="fix">
            <li><a href="https://www.linkedin.com/in/willem-gardner-064160181/" class="secondary"><img class="icon" src="images/LinkedIn-Logos/LI-In-Bug.png" alt="LinkedIn Logo"></a></li>
        </ul>
    </nav>
    <aside class="hidden" id="dropdown">
        <nav>
            <ul>
                <li><a href="index.html"><button>About Me</button></a></li>
                <li><a href="resume.html"><button>Resume</button></a></li>
            </ul>
        </nav>
    </aside>
    <hgroup>
        <h1>Jobs</h1>
        <h2>from <a href="https://news.ycombinator.com/">Hacker News</a></h2>
    </hgroup>
</header>
<main class="container">{pagecontent}
    
</main>
<footer class="container">
    <nav class="navbar">
        <ul>
            <li><a href="https://github.com/WillemGardner" class="secondary icon"><img class="icon circle" style="background-color: black;padding: 2px;" src="images/github-mark/github-mark-white.svg" alt="GitHub Logo"></a></li>
        </ul>
        <ul>
            <li><strong class="biggerfont">Willem Gardner</strong></li>
        </ul>
        <ul class="fix">
            <li><a href="https://www.linkedin.com/in/willem-gardner-064160181/" class="secondary"><img class="icon" src="images/LinkedIn-Logos/LI-In-Bug.png" alt="LinkedIn Logo"></a></li>
        </ul>
    </nav>
</footer>

</body>
</html> 
"""

pagecontent=""
for item in jobnews:
    job = json.loads(req.get(f'https://hacker-news.firebaseio.com/v0/item/{item}.json').text)
    #print(f'{item}: title: {list(job.keys())}')
    title = job["title"]
    date = datetime.datetime.fromtimestamp(job["time"])
    print(type(date))
    print(date)
    text = job["text"] if ("text" in list(job.keys())) else ""
    url = job["url"] if ("url" in list(job.keys())) else ""
    #print(f'item: {item}, title: {job["title"]}, date: {date}, text: {text}, url: {url}')
    article = """
    <article>
        <header>
            <hgroup>
                <h2>{title}</h2>
                <h3>{date}</h3>
            </hgroup>
        </header>
        <div>
            <p>{text}</p>
        </div>
        <footer>
            <a href="{url}" role="button">{url}</a>
        </footer>
    </article>
    """
    pagecontent += article.format(title = title, date = date, text = text, url = url)

htmlfinal = htmlpagetemplate.format(pagecontent = pagecontent)

with open('jobnews.html', 'w') as file:
    file.write(htmlfinal)