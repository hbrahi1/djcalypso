# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=20)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=20)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parties.Party'),
        ),
    ]
