import json
import requests
from bs4 import BeautifulSoup as BS

import os
import sys

# I find the absolute path
proj = os.path.dirname(os.path.abspath('manage.py'))

# I register a variable in the system
sys.path.append(proj)

# setup for application interaction with django

os.environ['DJANGO_SETTINGS_MODULE'] = 'abduParser.settings'
import django
django.setup()

from jobs.models import Job

# An example of receiving data via POST and Network
# res = requests.post('https://www', headers={'pf_keywords': 'python'})


def job_parsing():
    url = 'https://www.karriere-suedniedersachsen.de/jobboerse?s=python&zipcity=37083+G%C3%B6ttingen&perimeter=50'
    jobs = []
    res = requests.get(url)
    if res.status_code == 200:
        soup = BS(res.content, 'html.parser')
        div = soup.find('div', class_='job-board-results')
        articles = div.find_all('article', class_='job-board-result')
        for item in articles:
            title = item.h2.a.text.strip()
            url = 'https://www.karriere-suedniedersachsen.de' + item.h2.a['href']
            firma = item.find_all('a')[2].text.strip()
            firma_link = 'https://www.karriere-suedniedersachsen.de' + item.find_all('a')[2]['href']
            jobs.append({'title': title, 'url': url, 'firma': firma, 
                        'firma_link': firma_link})
            
    return jobs


def save_jobs():
    sued_karriere = job_parsing()
    for job in sued_karriere:
        j = Job(**job)
        j.save()
        
        
if __name__ == '__main__':
    save_jobs()
    
    
# As a example         
# with open('jobs.json', 'w', encoding='utf-8') as file:
#     json.dump(jobs, file, indent=4, ensure_ascii=False)