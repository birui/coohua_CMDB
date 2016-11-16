#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField
from django.conf import settings
from django import forms

# class Blog(models.Model):
#     Name=models.CharField(max_length=100,blank=True)
#     Content=UEditorField(u'内容   ',width=600, height=300, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000},
#              settings={},command=None,event_handler=myEventHander(),blank=True)


class Modelname(models.Model):
    name = models.CharField(max_length=70)
    lead = models.CharField(max_length=50)
    remark = models.CharField(max_length=250)
    def __unicode__(self):
        return self.name

class Server(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Hosts(models.Model):
    instance_id = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    lip = models.CharField(max_length=15)
    wip = models.CharField(max_length=15,blank=True)
    config = models.CharField(max_length=250)
    #1青岛,2杭州,3北京
    data_center = models.IntegerField()
    Modelname = models.ManyToManyField(Modelname,blank=True)
    server = models.ManyToManyField(Server,blank=True)
    environment = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    cost = models.FloatField(blank=True)
    remark = models.CharField(max_length=250,blank=True)
    def __unicode__(self):
        return self.hostname
    class Meta:
        ordering = ['hostname']

class Brothers(models.Model):
    name = models.CharField(max_length=20)
    #1研发
    department = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20,blank=True)
    service = models.ManyToManyField(Modelname)
    #pic = models.ImageField(upload_to = 'uploadimages')
    def __unicode__(self):
        return self.name


class History(models.Model):
    date_time = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(Brothers)
    host = models.ForeignKey(Hosts)
    remark = models.CharField(max_length=250)

class Domain(models.Model):
    date_time = models.DateTimeField(auto_now_add = True)
    usename = models.CharField(max_length=20,blank=True)
    domain = models.CharField(max_length=100)
    remark = models.CharField(max_length=250,blank=True)
    service_model = models.ForeignKey(Modelname,blank=True)
    def __unicode__(self):
        return self.domain

class CalendarEvent(models.Model):
    title = models.CharField(blank=True, max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    all_day = models.BooleanField(default=False)
    class Meta:
        verbose_name = ('Event')
        verbose_name_plural = ('Events')

    def __unicode__(self):
        return self.title

class iterms(models.Model):
    hostid = models.IntegerField()
    hostname = models.CharField(blank=True, max_length=200)
    cpu_itemid = models.IntegerField(blank=True,null=True)
    cpu_idle = models.FloatField(blank=True,null=True)
    cpu_graphs_itemsid = models.IntegerField(blank=True,null=True)
    eth0_graphs_itemsid = models.IntegerField(blank=True,null=True)
    eth1_graphs_itemsid = models.IntegerField(blank=True,null=True) 
    memory_total_itemsid = models.IntegerField(blank=True,null=True)
    memory_total = models.FloatField(null=True)
    memory_available_itemsid = models.IntegerField(blank=True,null=True)
    memory_available = models.FloatField(null=True)
    eth0_in_itemsid = models.IntegerField(blank=True,null=True)
    eth0_in = models.FloatField(null=True)
    eth0_out_itemsid = models.IntegerField(blank=True,null=True)
    eth0_out = models.FloatField(null=True)
    eth1_in_itemsid = models.IntegerField(blank=True,null=True)
    eth1_in = models.FloatField(null=True)
    eth1_out_itemsid = models.IntegerField(blank=True,null=True)
    eth1_out = models.FloatField(null=True)
    cpu_load_itemsid= models.IntegerField(blank=True,null=True)
    cpu_load = models.FloatField(null=True)

    def __unicode__(self):
       return str(self.hostname) #返回的数据
       # return self.hostname

class online(models.Model):
    models_name = models.CharField(blank=True,max_length=20)
    version = models.CharField(blank=True,max_length=20)
    describe = models.CharField(blank=True,max_length=250)
    date_time = models.DateTimeField(auto_now_add = True)

    # def __unicode__(self):
    #    return str(self.models_name)

class config(models.Model):
    name = models.CharField(blank=True,max_length=50,null=True)
    models_name = models.CharField(blank=True,max_length=50)
    path = models.CharField(blank=True,max_length=100)
    describe = models.CharField(blank=True,max_length=250)
    date_time = models.DateTimeField(auto_now_add=True,)
    remote_user = models.CharField(blank=True, max_length=50)
    playbook_path = models.CharField(blank=True, max_length=250)
    # def __unicode__(self):
    #     return self.models_name
    # class Meta:
    #     ordering = ['models_name']

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class UploadFile(models.Model):
	file = models.FileField(upload_to='files/%Y/%m/%d')

#上传作品表:作品名称，用户名
class Upload(models.Model):
    #注意这里的用户名是FileField类型
    name = models.FileField(upload_to = './upload/')
    username = models.CharField(max_length = 20)
    def __str__(self):
        return self.name

class dbsize(models.Model):
    hostname = models.CharField(max_length=50)
    bj_ip = models.CharField(max_length=50,blank=True)
    qd_size = models.IntegerField(blank=True,null=True)
    bj_size = models.IntegerField(blank=True,null=True)

    def __unicode__(self):
        return str(self.hostname)