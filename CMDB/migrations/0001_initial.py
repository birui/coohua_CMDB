# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brothers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7)),
                ('department', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('remark', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_id', models.CharField(max_length=30)),
                ('hostname', models.CharField(max_length=50)),
                ('lip', models.CharField(max_length=15)),
                ('wip', models.CharField(max_length=15)),
                ('config', models.CharField(max_length=50)),
                ('data_center', models.IntegerField()),
                ('environment', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('cost', models.IntegerField()),
                ('remark', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7)),
                ('lead', models.CharField(max_length=7)),
                ('remark', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='hosts',
            name='server',
            field=models.ManyToManyField(to='CMDB.Server'),
        ),
        migrations.AddField(
            model_name='hosts',
            name='service_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMDB.Services'),
        ),
        migrations.AddField(
            model_name='history',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMDB.Hosts'),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMDB.Brothers'),
        ),
        migrations.AddField(
            model_name='brothers',
            name='service',
            field=models.ManyToManyField(to='CMDB.Services'),
        ),
    ]