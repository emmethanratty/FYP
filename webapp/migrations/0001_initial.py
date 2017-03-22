# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tweets_app',
            fields=[
                ('created_at', models.CharField(blank=True, max_length=200, null=True)),
                ('id', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, max_length=1000, null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('user_id', models.IntegerField(blank=True, default=0, null=True)),
                ('truncated', models.CharField(blank=True, max_length=200, null=True)),
                ('in_reply_to_status_id', models.BigIntegerField(blank=True, default=0, null=True)),
                ('in_reply_to_user_id', models.BigIntegerField(default=0)),
                ('in_reply_to_screen_name', models.CharField(max_length=200)),
                ('retweeted_status_id', models.BigIntegerField(blank=True, default=0, null=True)),
                ('geo', models.CharField(blank=True, max_length=200, null=True)),
                ('place', models.CharField(blank=True, max_length=200, null=True)),
                ('retweet_count', models.IntegerField(blank=True, default=0, null=True)),
                ('reply_count', models.IntegerField(blank=True, default=0, null=True)),
                ('favorite_count', models.IntegerField(blank=True, default=0, null=True)),
                ('num_hashtags', models.IntegerField(blank=True, default=0, null=True)),
                ('num_urls', models.IntegerField(blank=True, default=0, null=True)),
                ('num_mentions', models.IntegerField(blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bot', models.NullBooleanField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='users_app',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('screen_name', models.CharField(blank=True, max_length=200, null=True)),
                ('statuses_count', models.IntegerField(blank=True, default=0, null=True)),
                ('followers_count', models.IntegerField(blank=True, default=0, null=True)),
                ('friends_count', models.IntegerField(blank=True, default=0, null=True)),
                ('favourites_count', models.IntegerField(blank=True, default=0, null=True)),
                ('listed_count', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('lang', models.CharField(blank=True, max_length=200, null=True)),
                ('time_zone', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('default_profile', models.CharField(blank=True, max_length=200, null=True)),
                ('default_profile_image', models.CharField(blank=True, max_length=200, null=True)),
                ('geo_enabled', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_image_url', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_banner_url', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_use_background_image', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_background_image_url_https', models.CharField(blank=True, max_length=500, null=True)),
                ('profile_text_color', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_image_url_https', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_sidebar_border_color', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_background_tile', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_sidebar_fill_color', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_background_image_url', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_background_color', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_link_color', models.CharField(blank=True, max_length=200, null=True)),
                ('utc_offset', models.CharField(blank=True, max_length=200, null=True)),
                ('protected', models.CharField(blank=True, max_length=200, null=True)),
                ('verified', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('dataset', models.CharField(blank=True, max_length=5, null=True)),
                ('bot', models.NullBooleanField(default=None)),
            ],
        ),
    ]