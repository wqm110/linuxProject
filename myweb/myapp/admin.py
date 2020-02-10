from django.contrib import admin

# Register your models here.
from myapp.models import Stu, menu, Spider_p, Movie, MyDoc


# Stu模型的管理器(装饰器写法)
@admin.register(Stu)
class StuAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'name', 'age', 'sex', 'classid')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'name')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序

    # list_editable 设置默认可编辑字段
    # list_editable = ['age','sex','classid']

    # 其他请详见手册文档说明


@admin.register(menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order')
    list_display_links = ('name', 'url')
    list_per_page = 10
    ordering = ('id', 'order')
    list_editable = ['order']


@admin.register(Spider_p)
class ScrapyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'spider_dir', 'context', 'order_p')
    list_editable = ('name', 'spider_dir', 'context', 'order_p')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'clas', 'htmurl', 'm3u8url', 'upLoadTime', 'states', 'img')
    list_display_links = ('title',)


@admin.register(MyDoc)
class MyDocAdmin(admin.ModelAdmin):
    list_display = ('docName', 'docContext', 'docLink', 'docLocalurl', 'docClas', 'docState', 'docOrder')
    list_display_links = ('docName',)