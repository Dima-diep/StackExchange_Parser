from bs4 import BeautifulSoup
import os
from pyfzf.pyfzf import FzfPrompt

nameserv = ['3D Printing', 'Academia', 'Amateur Radio', 'Android Enthusiasts', 'Anime & Manga', 'Arduino', 'Area51', 'Arqade', 'Artifical Intelligence', 'Arts & Crafts', 'Ask Different', 'Ask Patents', 'Ask Ubuntu', 'Astronomy', 'Aviation', 'Beer, Wine & Spirits', 'Biblical Hermeneutics', 'Bicycles', 'Bioinformatics', 'Biology', 'Bitcoin', 'Blender', 'Board & Card Games', 'Bricks', 'Buddhism', 'Cardano', 'Chemistry', 'Chess', 'Chinese Language', 'Christianity', 'CiviCRM', 'Code Golf', 'Code Review', 'Coffee', 'Community Building', 'Computational Science', 'Computer Graphics', 'Computer Science Educators', 'Computer Science', 'Constructed Languages', 'Craft CMS', 'Cross Validated', 'Crypthography', 'Data Science', 'Database Administrators', 'DevOps', 'Drones and Models Aircraft', 'Drupal Answers', 'Earth Science', 'Ebooks', 'Economics', 'Electrical Engineering', 'elementary OS', 'emacs', 'Engineering', 'English Language & Usage', 'English Language Learners'

stacklink = "https://ru.stackoverflow.com"

fzf = FzfPrompt()
global num
global lnk

os.system("curl {stacklink} > .tmp/stack.html")
html_main = open('stack.html', 'r')
bs = BeautifulSoup(html_main, features='lxml')
names = bs.find_all('div', class_='summary')
for name in names:
    for a in bs.find_all('a', class_="question-hyperlink"):
        link = a['href']
        text = a.find(text=True)
        with open('.tmp/questions.txt', 'r') as f:
            quest = f.read()
            if text not in quest:
                with open('.tmp/questions.txt', 'a') as quesd:
                    quesd.write(f"{text}\n")
                    quesd.close()
        with open('.tmp/links.txt', 'r') as links:
            linkd = links.read()
            if link not in linkd:
                with open('.tmp/links.txt', 'a') as lins:
                    lins.write(f"{link}\n")
                    lins.close()

with open('.tmp/questions.txt', 'r') as select:
    sel = select.read().splitlines()
    selt = fzf.prompt(sel)
    nselt = selt[0]
    num = sel.index(nselt)
with open('.tmp/links.txt', 'r') as getlink:
    linkgo = getlink.read().splitlines()
    gorun = linkgo[num]
    print(f"\n\nGo to: {stacklink}{gorun}")
