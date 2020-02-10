from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^$', views.index, name="index"),
    # 基础
    path('', views.login, name="login"),
    path('registe', views.registe, name="registe"),
    path('toregiste', views.toregiste, name="toregiste"),
    path('login', views.login, name="login"),
    path('index.html', views.index, name="index"),
    # 高级功能
    # url(r'forms.html', views.forms, name="forms"),
    path('forms.html', views.forms, name="forms"),
    path('charts.html', views.charts, name="charts"),
    path('tables.html', views.tables, name="tables"),
    path(r'echarts/', views.e_charts, name="et"),
    path(r'bar/', views.bar, name="bar"),
    path(r'dataView', views.dataview, name="da"),
    path(r'dataView/<int:page>', views.dataview, name="da"),

    # 房产
    path(r'house.html/<int:a>', views.house, name="house_page"),
    path(r'house.html', views.house_de, name="house_de"),
    path(r'house.html/<str:city>', views.house_city, name="house_city"),
    path(r'house.html/<str:city>/<int:page>', views.house_city_page, name="house_city_page"),
    path(r'anlize_city/<str:city>', views.anlize_city, name="anlize_city"),

    # 地图
    path(r'geo/<str:city>', views.geo, name="geo"),
    path(r'scrapy/<int:id>', views.spider, name="sp"),
    path(r'scrapy/stop', views.spider_stop, name="stp"),
    path(r'scrapy/', views.spider, name="sp"),

    # 娱乐
    path(r'holly', views.holly, name="holly"),
    path(r'holly/<int:page>', views.holly, name="holly"),
    path(r'movie', views.movie, name="movie"),
    path(r'movie/<int:page>', views.movie, name="movie"),
    path(r'movie1', views.dytt, name="dytt"),
    path(r'movie1/<int:page>', views.dytt, name="dytt"),
    path(r'downloadm3u8', views.download_m3u8, name="m38"),
    path(r'movie_detail/', views.movie_detail, name="movie_detail"),
    # 常用文档
    path(r'docs', views.mydocs, name="mydocs"),
    path(r'mydoc/<int:id>', views.mydocDetail, name="mydocsD"),

]
