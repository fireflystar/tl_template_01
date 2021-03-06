from django.db import models
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.utils import timezone

from wp_site.models import WpPosts, Tdk, Tag
from math import ceil

def get_tdk(type_id):
    tdk = Tdk.objects.filter(type_id=type_id).first()
    print(tdk)
    return tdk


# Create your views here.

def main(request):
    count = WpPosts.objects.count()
    pages = ceil(count / 16)
    page = int(request.GET.get('page', 1))
    page_one = count-16*(page)
    page_two = count-16*(page-1)
    if page_one < 0:
        page_one = 0
    data = WpPosts.objects.filter(post_date__lt=timezone.now()).filter(is_enable=True)[page_one:page_two][::-1]
    categories = {}
    for i in WpPosts.category:
        categories[i[1]] = i[0]
    page = 0 if page < 1 or page >= (pages + 1) else (page - 1)
    start = page * 10
    end = start + 10
    articles = WpPosts.objects.all()[start:end]
    da = WpPosts.objects.filter(post_date__lt=timezone.now()).filter(is_enable=True)[count-8:][::-1]
    print(da)
    tag = Tag.objects.exclude(tag_name='没有')
    tag = list(tag)
    return render(request, 'index.html',
                  {'data': data,
                   'tdk': get_tdk(1),
                   'categories': categories,
                   'articles': articles,
                   'page': page,
                   'pages': range(pages),
                   'da': da,
                   'tag': tag
                   })

def category(request):
    get_category = request.path.split('/')[1]
    categories = {}
    for i in WpPosts.category:
        categories[i[1]] = i[0]
    type_id = categories[get_category]
    count = WpPosts.objects.filter(post_category=type_id).count()
    print(count)
    pages = ceil(count / 16)
    page = int(request.GET.get('page', 1))
    page_one = count - 16 * (page)
    page_two = count - 16 * (page - 1)
    if page_one < 0:
        page_one = 0
    data = WpPosts.objects.filter(post_category=type_id).all().filter(post_date__lt=timezone.now()).filter(
        is_enable=True)[page_one:page_two][::-1]
    page = 0 if page < 1 or page >= (pages + 1) else (page - 1)
    start = page * 10
    end = start + 10
    articles = WpPosts.objects.all()[start:end]
    count = WpPosts.objects.count()
    da = WpPosts.objects.filter(post_date__lt=timezone.now()).filter(is_enable=True)[count - 8:][::-1]
    tag = Tag.objects.exclude(tag_name='没有')
    cate = data[0].post_category
    print(cate)

    return render(request, 'category.html', {
        'data': data,
        'tdk': get_tdk(2),
        'categories': categories,
        'page': page,
        'pages': range(pages),
        'articles': articles,
        'da': da,
        'tag': tag,
        'cate': cate
    })

def tag(request):
    if request.method == "GET":
        tag = request.path_info[1:]
        print(tag)
        tagList = Tag.objects.all()    #文章列表
        #for tag in tagList:print(tag.id,tag.tag_name)
        l = [(tag.tag_name, tag.id) for tag in tagList]
        d = dict(l)
        print(d[tag])

        wpList = WpPosts.objects.all()
        for wp in wpList:
            print(str(wp.tag_id))
        resList = [wp for wp in wpList if str(d[tag]) in str(wp.tag_id)]

        tag = Tag.objects.exclude(tag_name='没有')
        tag = list(tag)
        return render(request,'sou.html',{
             "queryList":resList,
             "tag":tag
    })



def article(request, aid):
    aid = int(aid)
    categories = {}
    for i in WpPosts.category:
        categories[i[1]] = i[0]
    articles = WpPosts.objects.only('id', 'post_title', 'post_content').filter(is_enable=True)
    max_id = articles.last().id
    min_id = articles.first().id
    if aid < 1 or aid > max_id:
        return HttpResponse('<p><h1 style="color:red;text-align:center">无此文章!</h1></p>')
    article = articles.filter(id=aid)
    article.update(post_read=models.F('post_read') + 1)
    article = article.first()
    if aid == min_id:
        prev = None
        next_article = articles.filter(id__gt=aid).first()
    elif aid == max_id:
        prev = articles.filter(id__lt=aid).first()
        next_article = None
    elif min_id < aid < max_id:
        prev = articles.filter(id__lt=aid).first()
        next_article = articles.filter(id__gt=aid).first()
    count = WpPosts.objects.count()
    pages = ceil(count / 16)
    page = int(request.GET.get('page', 1))
    page_one = count-16*(page)
    page_two = count-16*(page-1)
    if page_one < 0:
        page_one = 0
    data = WpPosts.objects.filter(post_date__lt=timezone.now()).filter(is_enable=True)[page_one:page_two][::-1]
    categories = {}
    for i in WpPosts.category:
        categories[i[1]] = i[0]
    page = 0 if page < 1 or page >= (pages + 1) else (page - 1)
    start = page * 10
    end = start + 10
    articles = WpPosts.objects.all()[start:end]
    return render(request, 'article.html',
                  {'article': article,
                   'prev': prev,
                   'next': next_article,
                   'tdk': get_tdk(4),
                   'categories': categories,
                   'page': page,
                   'pages': range(pages),
                   })


def searchA(request):
    if request.method == "POST":
        wenstr = request.POST.get("wenzhang",None).strip()
        #print(wenstr)
        queryList = WpPosts.objects.filter((
		Q(post_title__icontains=wenstr) |
		Q(post_content__icontains=wenstr)
		))
        print(len(queryList))
        tag = Tag.objects.exclude(tag_name='没有')
        tag = list(tag)
        return render(request,'sou.html',{
             "queryList":queryList,
             "tag":tag
    })





