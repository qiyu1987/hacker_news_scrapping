from bs4 import BeautifulSoup
import requests
from pprint import pprint


def get_stories(*urls):
    stories = []
    for url in urls:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        story_links = soup.select('.storylink')
        subtexts = soup.select('.subtext')
        for idx, story_link in enumerate(story_links):
            if len(subtexts[idx].select('.score')):
                title = story_link.text
                link = story_link.get('href')
                score = int(subtexts[idx].select('.score')[0].text.replace(' points', ''))
                if score > 99:
                    stories.append({
                        'title': title,
                        'link': link,
                        'score': score
                    })
    stories = sorted(stories, key=lambda story: story['score'], reverse=True)
    return stories


pprint(get_stories('https://news.ycombinator.com/', 'https://news.ycombinator.com/news?p=2'))
