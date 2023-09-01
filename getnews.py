import requests as req
import json

accesskey = ""
with open("G:/NewsAPIaccesskey.txt", "r") as file:
    text = file.read()
    accesskey += text

news = json.loads(req.get(f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={accesskey}').text)

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
        <h1>Tech News</h1>
        <h2>from NewsAPI</h2>
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

print(f'status:  {news["status"]}')
print(f'total results:  {news["totalResults"]}')
print('\n')
pagecontent = ""
for newsitem in news['articles']:
    if newsitem["title"] == None:
        continue
    print(f'author: {newsitem["author"]}')
    print(f'title: {newsitem["title"]}')
    print(f'source: {newsitem["source"]}')
    print(f'description: {newsitem["description"]}')
    print(f'url: {newsitem["url"]}')
    print(f'image url: {newsitem["urlToImage"]}')
    print(f'date: {newsitem["publishedAt"]}')
    print('\n')
    

    article = """
    <article>
        <header>
            <hgroup>
                <h2>{title}</h2>
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
    
    pagecontent += article.format(title = newsitem["title"].replace("’","'").replace("‘","'").replace("…","..."),
                   author = newsitem["author"] if newsitem["author"] != None else '', 
                   source = newsitem["source"]["name"], 
                   description = newsitem["description"].replace("’","'").replace("‘","'").replace("…","...") if newsitem["description"] != None else '', 
                   imageUrl = newsitem["urlToImage"] if newsitem["urlToImage"] != None else '', 
                   date = newsitem["publishedAt"][:10],
                   url = newsitem["url"])
htmlfinal = htmlpagetemplate.format(pagecontent = pagecontent)


with open('news.html', 'w') as file:
    file.write(htmlfinal)
