from django.db import models


class User(models.Model):
    # userid = models.IntegerField('编号', auto_created=True, primary_key=True)
    username = models.CharField('用户名', max_length=100, primary_key=True)
    password = models.CharField('密码', max_length=100)
    email = models.CharField('email', max_length=100)


# Create your models here.
class Stu(models.Model):
    '''自定义Stu表对应的Model类'''
    # 定义属性：默认主键自增id字段可不写
    id = models.AutoField("学号", primary_key=True)
    name = models.CharField("姓名", max_length=100)
    age = models.SmallIntegerField("年龄")
    sex = models.CharField("性别", max_length=1)
    classid = models.CharField("班级", max_length=8)

    # 定义默认输出格式
    def __str__(self):
        return "%d:%s:%d:%s:%s" % (self.id, self.name, self.age, self.sex, self.classid)

    # 自定义对应的表名，默认表名：myapp_stu

    # class Meta:
    #     db_table = "stu"
    #     verbose_name = '浏览学生信息'
    #     verbose_name_plural = '学生信息管理'


class menu(models.Model):
    id = models.AutoField("菜单编号", primary_key=True)
    name = models.CharField("菜单名称", max_length=20)
    url = models.CharField('链接地址', max_length=20)
    order = models.CharField('排序', max_length=20)

    # 定义默认输出格式
    def __str__(self):
        return "%s" % self.url

    class Meta:
        db_table = "menu"
        verbose_name = '浏览菜单信息'
        verbose_name_plural = '菜单信息管理'


class Sv(models.Model):
    item_id = models.CharField('m3u8地址', max_length=200, primary_key=True)
    url = models.TextField('m3u8地址', max_length=255)
    name = models.TextField('标题', max_length=255)
    time = models.TimeField('创建时间', )
    img = models.TextField('图片地址', max_length=150)

    def __str__(self):
        return "%s" % self.url

    class Meta:
        db_table = "sswgvideo_"


class Dhouse(models.Model):
    city_name = models.CharField('城市名称', max_length=100)
    url = models.CharField('链接', max_length=100)
    city_id = models.CharField('城市编号', max_length=100)
    gardenId = models.CharField('小区编号', max_length=100)
    gardenName = models.CharField('', max_length=100)
    roomId = models.CharField('', max_length=100)
    house_id = models.CharField('', max_length=100)
    house_type = models.CharField('', max_length=100)
    bildingname = models.CharField('', max_length=100)
    volume_ratio = models.CharField('', max_length=100)
    region = models.CharField('', max_length=100)
    greening_rate = models.CharField('', max_length=100)
    reference_price = models.CharField('', max_length=100)
    totle_house = models.CharField('', max_length=100)
    decoration_situation = models.CharField('', max_length=100)
    parking_place = models.CharField('', max_length=100)
    area = models.CharField('', max_length=100)
    property_company = models.CharField('', max_length=100)
    property_fee = models.CharField('', max_length=100)
    developers = models.CharField('', max_length=100)
    ts = models.CharField('', max_length=100)
    price_sum = models.CharField('', max_length=100)
    price_time = models.CharField('', max_length=100)
    use = models.CharField('', max_length=100)
    property_right = models.CharField('', max_length=100)
    opening_time = models.CharField('', max_length=100)
    delivery_time = models.CharField('', max_length=100)
    bh = models.CharField('', max_length=100)
    address = models.CharField('', max_length=100)
    types = models.CharField('', max_length=100)
    latitude = models.CharField('', max_length=100)
    longitude = models.CharField('', max_length=100)

    def __str__(self):
        return "%s" % self.url

    class Meta:
        db_table = "dhouse"


class Spiderpitem(models.Model):
    item_id = models.TextField('标题', max_length=255)  # , primary_key=True)
    longitude = models.TextField('标题', max_length=255)
    latitude = models.TextField('标题', max_length=255)
    city_name = models.TextField('标题', max_length=255)
    gardenId = models.TextField('标题', max_length=255)
    gardenName = models.TextField('标题', max_length=255)
    roomId = models.TextField('标题', max_length=255)
    city_id = models.TextField('标题', max_length=255)
    house_id = models.TextField('标题', max_length=255)
    volume_ratio = models.TextField('标题', max_length=255)
    region = models.TextField('标题', max_length=255)
    greening_rate = models.TextField('标题', max_length=255)
    reference_price = models.TextField('标题', max_length=255)
    totle_house = models.TextField('标题', max_length=255)
    decoration_situation = models.TextField('标题', max_length=255)
    parking_place = models.TextField('标题', max_length=255)
    area = models.TextField('标题', max_length=255)
    property_company = models.TextField('标题', max_length=255)
    property_fee = models.TextField('标题', max_length=255)
    developers = models.TextField('标题', max_length=255)
    ts = models.TextField('标题', max_length=255)
    price_sum = models.TextField('标题', max_length=255)
    price_time = models.TextField('标题', max_length=255)
    use = models.TextField('标题', max_length=255)
    property_right = models.TextField('标题', max_length=255)
    opening_time = models.TextField('标题', max_length=255)
    delivery_time = models.TextField('标题', max_length=255)
    bh = models.TextField('标题', max_length=255)
    address = models.TextField('标题', max_length=255)
    url = models.TextField('标题', max_length=255)
    house_type = models.TextField('标题', max_length=255)

    class Meta:
        db_table = "spiderpitem_"


class Spider_p(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('爬虫名称', max_length=50)
    spider_dir = models.CharField('文件路径', max_length=100)
    context = models.TextField('描述', max_length=500)
    order_p = models.IntegerField('优先级')

    class Meta:
        db_table = "spider_p"
        verbose_name_plural = "爬虫管理"
        # managed = False


# class City_count(models.Model):
#     """这个model类对应你所建立好的视图"""

#     class Meta(object):
#         """同理，该方法可用于使用mysql中任何已有的表，不仅是视图"""
#         db_table = 'city_count'  # 显式指定表名，也就是你建立的视图的名字
#         managed = False  # 默认是ture，设成false django将不会执行建表和删表操作
# 建立字段间的映射
#  需要注意的是，必须设一个字段为主键
#  不然django会自动创建一个id字段为主键，引发错误
class Movie(models.Model):
    item_id = models.TextField("主键", max_length=200, primary_key=True)
    title = models.CharField('标题', max_length=100)
    clas = models.TextField('类别', max_length=100)
    htmurl = models.CharField('网页地址', max_length=100)
    m3u8url = models.TextField('视频地址', max_length=200)
    upLoadTime = models.CharField('上传时间', max_length=50)
    states = models.CharField('描述', max_length=50)
    img = models.CharField('图片', max_length=127)

    class Meta:
        db_table = "movie_"
        managed = False


class MyDoc(models.Model):
    docid = models.TextField("文档编号", max_length=100);
    docName = models.TextField("文档名称", max_length=100);
    docContext = models.TextField("文档简介", max_length=100);
    docLink = models.TextField("网络链接", max_length=100);
    docLocalurl = models.TextField("本地地址", max_length=100);
    docClas = models.TextField("分裂", max_length=100);
    docState = models.TextField("状态", max_length=100);
    docOrder = models.TextField("排序", max_length=100);

    class Meta:
        db_table = 'myDoc'
        verbose_name = '文档管理'

    def __repr__(self):
        return self.docName + "" + self.docContext
