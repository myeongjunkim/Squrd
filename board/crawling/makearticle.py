from bs4 import BeautifulSoup
import os, django, sys, io, requests, urllib3
from django.utils import timezone
import schedule, time

from apscheduler.schedulers.background import BlockingScheduler, BackgroundScheduler

sys.path.append('../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "board.settings")
django.setup()

from crawling.models import *

# -*- coding: utf-8 -*-
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') 
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 경고창 제거
urllib3.disable_warnings()


# 사이트별 class name 조사
ENTERTAIN={
    "스포츠조선":{"url":"https://sports.chosun.com","main_div":".welcome-post","title":".post-title","img_div":".post-thumb"},
    "탠아시아":{"url":"https://tenasia.hankyung.com","main_div":".news-top","title":".news-tit","img_div":".thumb"},
    "스포츠월드":{"url":"https://www.sportsworldi.com","main_div":"#wps_layout1_box1","title":".tit","img_div":".pic"},
    "imbc":{"url":"https://enews.imbc.com","main_div":".article-first","title":".title","img_div":"a"},
    "sbs연예":{"url":"https://ent.sbs.co.kr","main_div":".news_wide_list","title":".nwl_title","img_div":".nwl_image_w"},
    "스포츠동아":{"url":"https://sports.donga.com","main_div":".large","title":".txt","img_div":".thumb"},
    "티비리포트":{"url":"https://www.tvreport.co.kr","main_div":"#homepage-feature-banner-1","title":".main-img-title","img_div":".banner-image"},
    "티비데일리":{"url":"http://tvdaily.co.kr","main_div":".head_0","title":".ellipsis_txt1","img_div":".thum"},
    "뉴스엔":{"url":"https://www.newsen.co.kr","main_div":".index_headline","title":"dd p a","img_div":"dt"},
    "스포츠한국":{"url":"https://sports.hankooki.com","main_div":".head1","title":".gisa_list_rel","img_div":"dt"},
    
    # "스타뉴스":{"url":"https://star.mt.co.kr","main_div":".bundle.bthum","title":".tit","img_div":".thum"},
    # "스포츠경향":{"url":"https://sports.khan.co.kr","main_div":".box_topnews","title":".caption","img_div":"picture"},
    # "오센":{"url":"https://osen.mt.co.kr","main_div":".news_list","title":".txt_title","img_div":"dt"},
       
}


def check_url(url, domain):
    if url[0:2] == "//":
       url = "https:" + url
    elif url[0:1] == "/":
       url = domain+url
    elif url[0:4] != "http":
        url = domain+"/"+url
    return url


def get_htmlsoup(entertain_name):
    source = requests.get(ENTERTAIN[entertain_name]["url"], verify=False)
    source.raise_for_status()
    source.encoding=None
    # soup = BeautifulSoup(source.content.decode('euc-kr','replace'), 'html.parser')
    soup = BeautifulSoup(source.text, 'html.parser')
    return soup


def update_article(entertain_name, title, href, img_url):
    try:
        update_article = Article.objects.get(entertain_name= entertain_name)
    except Article.DoesNotExist:
        update_article = Article()
        update_article.entertain_name = entertain_name
        print("생성!!")

    print(timezone.now())
    
    update_article.pub_date = timezone.now()
    update_article.save()
    
    if update_article.title != title:
        print("업데이트!")
        print("이전", update_article.title)
        print("이후", title)
        update_article.title = title
        update_article.href = href
        update_article.img_url = img_url
        update_article.save()



def get_source(soup, entertain_name):
    main_div = soup.select_one(ENTERTAIN[entertain_name]["main_div"])
    # data
    title = main_div.select_one(ENTERTAIN[entertain_name]["title"]).text.strip()
    href = main_div.select_one("a")["href"]
    img_url = main_div.select_one(ENTERTAIN[entertain_name]["img_div"]+" img")["src"]

    href = check_url(href, ENTERTAIN[entertain_name]["url"])
    img_url = check_url(img_url, ENTERTAIN[entertain_name]["url"])

    # push data 
    update_article(entertain_name, title, href, img_url)


def crawling_main():
    for entertain_name in ENTERTAIN:
        soup = get_htmlsoup(entertain_name)
        get_source(soup, entertain_name)

    
sched = BackgroundScheduler(timezone='Asia/Seoul')
sched.add_job(crawling_main,'interval', seconds=300, id='test')
sched.start()


# crawling_main()


# schedule.every(1).minutes.do(crawling_main)
# while True:
#     schedule.run_pending()
#     time.sleep(1)





