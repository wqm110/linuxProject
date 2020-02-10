import os
import sys

import requests
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
from django.urls import reverse
from .downloadm3u8_m import downloadm3u8
from pyecharts.globals import ChartType, SymbolType

from pyecharts.charts import Geo, Bar
from pyecharts import options as opts
from pyecharts.faker import Faker

from pyecharts.charts import Page
from .models import menu, Dhouse, Stu, Sv, User, Spiderpitem, Spider_p, Movie, MyDoc

menulist = menu.objects.filter(order__contains='main_').order_by("order")
print(menulist)


# print(menulist)
def movie(request, page=1):
    movies = Sv.objects.all().order_by('-time')[(page - 1) * 15:page * 15]
    return render(request, 'movie.html',
                  {'menulist': menulist, 'movies': movies, 'currentpage': page, 'nextpage': page + 1,
                   'lastpage': page - 1})


def dytt(request, page=1):
    movies = Movie.objects.filter(states="OK").order_by('-upLoadTime')[(page - 1) * 15:page * 15]
    intpage = page
    return render(request, 'dytt.html',
                  {'menulist': menulist, 'movies': movies, 'currentpage': intpage, 'nextpage': page + 1,
                   'lastpage': page - 1})


def holly(request, page=1):
    movies = Movie.objects.filter(states="Download").order_by('-upLoadTime')[(page - 1) * 15:page * 15]
    intpage = page
    return render(request, 'dytt.html',
                  {'menulist': menulist, 'movies': movies, 'currentpage': intpage, 'nextpage': page + 1,
                   'lastpage': page - 1})


def movie_detail(re):
    m3u8url = re.GET.get('m3u8url')

    return render(re, 'movie1.html', {'menulist': menulist, 'url': m3u8url})


def check_menulist():
    # menulist = menu.objects.all()
    #
    print(menulist)
    for m in menulist:
        print(m.url, m.name)
    return menulist


def index(request):
    # return HttpResponse("Hello world!")
    # menulist = check_menulist()
    return render(request, "index.html", {'menulist': menulist})


def login(request):
    # print('--------')
    username = request.GET.get('loginUsername')
    pwd = request.GET.get('loginPassword')
    try:
        u = User.objects.get(username=username)
        if u.password == pwd:
            return render(request, 'index.html', {'menulist': menulist})
        else:
            return render(request, 'login.html')
    except Exception as e:
        print(e)
    # print('+++++++++',u)
    # print('login user name:',username)
    # return HttpResponse("Hello world!")
    # menulist = check_menulist()
    return render(request, "login.html", {'menulist': menulist})


def toregiste(request):
    return render(request, 'register.html')


def registe(request):
    # print('--------')
    username = request.GET.get('registerUsername')
    useremail = request.GET.get('registerEmail')
    password = request.GET.get('registerPassword')
    # print('registe:',useremail)
    user = User()
    user.email = useremail
    user.username = username
    user.password = password
    resultid = user.save()

    # print('resultuserid:', resultid)
    # return HttpResponse("Hello world!")
    # menulist = check_menulist()
    return render(request, "login.html")


def forms(request):
    # return HttpResponse("Hello world!")
    # menulist = check_menulist()
    return render(request, "forms.html", {'menulist': menulist})


def charts(request):
    # menulist = check_menulist()
    # return HttpResponse("Hello world!")
    return render(request, "charts.html", {'menulist': menulist})


def tables(request):
    # menulist = menu.objects.all()
    # return HttpResponse("Hello world!")
    return render(request, "tables.html", {'menulist': menulist})


def house(request, a):
    # menulist = menu.objects.all()
    if not (a == 0 or a == ''):
        page = int(a)
        houses = Spiderpitem.objects.all()[(page - 1) * 15:page * 15]
    else:
        houses = Spiderpitem.objects.all()[: 15]
    # return HttpResponse("Hello world!")
    return render(request, "house.html",
                  {'houses': houses, 'menulist': menulist, 'currentpage': page, 'nextpage': page + 1,
                   'lastpage': page - 1})


def house_de(request):
    houses = Spiderpitem.objects.all()[: 15]
    citynames = Spiderpitem.objects.values('city_name')
    print(citynames)
    print('citynames')
    # return HttpResponse("Hello world!")
    return render(request, "house.html", {'houses': houses, 'menulist': menulist, 'currentpage': 1, 'nextpage': 2})


def house_redirect(a, city):
    return HttpResponseRedirect(
        reverse('house_city', args=(a, city)))


def house_city(request, city):
    print(city)
    houses = Spiderpitem.objects.filter(city_name=city)[:15]
    citynames = Spiderpitem.objects.values('city_name').annotate(count=Count('city_name'))[:1]
    print(citynames)
    # return HttpResponse("Hello world!")
    return render(request, "house.html",
                  {'houses': houses, 'citynames': citynames, 'menulist': menulist, 'city': city, 'currentpage': 1,
                   'nextpage': 2})


def house_city_page(request, city, page):
    print(city, page)
    if (page > 2):
        print('page:', page)
        houses = Spiderpitem.objects.filter(city_name=city)[(page - 1) * 15:page * 15]
    else:
        print('page￥￥￥:', type(page))

        houses = Spiderpitem.objects.filter(city_name=city)[:15]
    citynames = Spiderpitem.objects.values('city_name').annotate(count=Count('city_name'))
    print(citynames)
    # return HttpResponse("Hello world!")
    return render(request, "house.html",
                  {'houses': houses, 'citynames': citynames, 'menulist': menulist, 'city': city, 'currentpage': page,
                   'nextpage': int(page) + 1,
                   'lastpage': int(page) - 1})


def anlize_city(request, city):
    from pyecharts.charts import Bar
    from pyecharts import options as opts

    # V1 版本开始支持链式调用
    bar = (
        Bar()
            .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
            .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
            .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
    )
    bar.render()

    # 不习惯链式调用的开发者依旧可以单独调用方法
    bar = Bar()
    bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
    bar.render('templates/render.html')
    # Dhouse.objects.
    return render(request, 'anlize_city.html', {'menulist': menulist})


def geo(request, city):
    citynames = Spiderpitem.objects.values('city_name').annotate(count=Count('city_name'))
    # city_hose = Dhouse.objects.filter(city_name=city).filter(region__isnull=True).filter(latitude__isnull=True).filter(
    city_hose = Dhouse.objects.filter(city_name=city).filter(region__isnull=True).values('region', 'latitude',
                                                                                         'longitude').annotate(
        count=Count('region'))
    # print(city_hose)
    tuple_list = []
    tuple_s = ()
    for b in city_hose.all():
        # tuple_s = (b['city_name'], b['count'])
        tuple_s = (b['region'].split(' ')[0], b['count'])
        # if b['city_name'] != None:
        if b['region'] != None:
            tuple_list.append(tuple_s)
    print(tuple_list)
    # c = geo_example.geo_heatmap
    c = (
        Geo()
            .add_schema(maptype='%s' % city)
            .add(
            "geo",
            # [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)],
            [x for x in tuple_list],

            # citynames.radiansdict.items(),
            # type_=ChartType.HEATMAP,
            type_=ChartType.EFFECT_SCATTER,
        )
            .add("geo",
                 [{
                     "阿城": [126.58, 45.32],
                     "阿克苏": [180.19, 41.09]
                 }],
                 type_=ChartType.EFFECT_SCATTER,
                 )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-%s地图" % city),
        )
    )
    # return render(request )
    c.render('templates/render.html')
    return render(request, 'anlize_city.html', {'menulist': menulist}, )


def spider(request, id=0):
    spiders = Spider_p.objects.all()
    print(id)
    if id != 0:
        s = Spider_p.objects.get(id=id)
        print(s.spider_dir)
        # from SpiderP.SpiderP import spiders as sp
        line = 'cd ' + s.spider_dir + '&&' + 'scrapy crawl %s' % s.name
        result = os.popen(line, 'r')

    return render(request, 'spiders.html', {'spiders': spiders, 'menulist': menulist})


def spider_stop(request, id=1, stop='stop'):
    spiders = Spider_p.objects.all()
    s = Spider_p.objects.get(id=id)
    print(s.spider_dir)

    line = 'cd ' + s.spider_dir + '&&' + 'exit'
    result = os.popen(line, 'r')
    return render(request, 'spiders.html', {'spiders': spiders, 'menulist': menulist})


def e_charts(request):
    return render(request, 'e_charts.html', {'menulist': menulist})


def bar(request):
    c = (
        Bar()
            .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [10, 15, 23, 15, 19, 46, 150])
            # .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    c.render('templates/render.html')
    return render(request, 'bar.html', {'menulist': menulist})


def download_m3u8(request):
    url = request.GET.get('m3u8url')

    print(url)
    downloadm3u8(m3u8url=url)
    return render(request, 'movie.html')


def dataview(request, page=1):
    fl = menu.objects.filter(order__contains='data_')
    return render(request, 'datavalue_list.html', {'menulist': menulist, 'functionlist': fl})


def dataview1(request, page=1):
    try:
        print(page)
        houses = Dhouse.objects.values('city_name').annotate(count=Count('city_name'))
        print(houses)
        city_names = []
        times = []
        for h, c in zip(houses.values('city_name'), houses.values('count')):
            print(h, c)
            city_names.append(h['city_name'])
            times.append(c['count'])
        c = (
            Bar()
                # .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
                .add_xaxis(city_names)
                .add_yaxis("商家A", times)
                .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
        )
        c.render('templates/bar.html')
    except Exception as e:
        print(e)
        raise Http404(e)
    return render(request, 'bar.html', {'menulist': menulist})


def mydocs(request, current_page=1):
    # 列表
    mydocs = MyDoc.objects.filter(docState='ok')

    return render(request, "mydocs.html", {"mydocs": mydocs, "menulist": menulist, 'currentpage': current_page})


def mydocDetail(request, id=0):
    # 列表

    doc = MyDoc.objects.filter(id=id)
    url = doc[0].docLink
    response = requests.get(url)
    with open('templates/temp.html','w',encoding="utf-8") as f:
        f.write(response.text)
    return render(request,'mydocDetail.html')
