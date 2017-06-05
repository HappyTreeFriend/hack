# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-04 15:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dialogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.CharField(default='', max_length=10)),
                ('activity_id', models.CharField(default='', max_length=10)),
                ('is_internal', models.CharField(default='', max_length=10)),
                ('editable', models.CharField(default='', max_length=10)),
                ('type', models.CharField(default='', max_length=10)),
                ('message', models.TextField(default='', null=True)),
                ('markdown_message', models.TextField(default='', null=True)),
                ('automated_response', models.CharField(default='', max_length=10)),
                ('created_at', models.CharField(default='', max_length=40)),
                ('updated_at', models.CharField(default='', max_length=40)),
                ('actor_username', models.CharField(default='', max_length=40)),
                ('actor_url', models.CharField(default='', max_length=40)),
                ('genius_execution_id', models.CharField(max_length=40, null=True)),
                ('team_handle', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.CharField(default='', max_length=20)),
                ('title', models.CharField(default='', max_length=100)),
                ('url', models.CharField(default='', max_length=100)),
                ('username', models.CharField(default='', max_length=100)),
                ('username_url', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=20)),
                ('substate', models.CharField(default='', max_length=20)),
                ('severity_rating', models.CharField(default='', max_length=20)),
                ('created_at', models.CharField(default='', max_length=40)),
                ('team_name', models.CharField(default='', max_length=100)),
                ('team_url', models.CharField(default='', max_length=40)),
                ('team_about', models.TextField(default='')),
                ('has_bounty', models.CharField(default='', max_length=20)),
                ('can_view_team', models.CharField(default='', max_length=20)),
                ('is_external_bug', models.CharField(default='', max_length=20)),
                ('is_participant', models.CharField(default='', max_length=20)),
                ('public', models.CharField(default='', max_length=20)),
                ('visibility', models.CharField(default='', max_length=20)),
                ('cve_ids', models.CharField(default='', max_length=40)),
                ('singular_disclosure_disabled', models.CharField(default='', max_length=40)),
                ('disclosed_at', models.CharField(default='', max_length=40)),
                ('bug_reporter_agreed_on_going_public_at', models.CharField(default='', max_length=40, null=True)),
                ('team_member_agreed_on_going_public_at', models.CharField(default='', max_length=40, null=True)),
                ('comments_closed', models.CharField(default='', max_length=40)),
                ('vulnerability_information', models.TextField(default='')),
                ('vulnerability_information_html', models.TextField(default='')),
                ('original_report_id', models.CharField(max_length=40, null=True)),
                ('original_report_url', models.CharField(max_length=40, null=True)),
                ('allow_singular_disclosure_at', models.CharField(default='', max_length=40)),
                ('allow_singular_disclosure_after', models.CharField(default='', max_length=40)),
                ('singular_disclosure_allowed', models.CharField(default='', max_length=40)),
                ('vote_count', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='summaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.CharField(max_length=20)),
                ('summaries_id', models.CharField(default='', max_length=30)),
                ('content', models.TextField(default='')),
                ('content_html', models.TextField(default='')),
                ('category', models.CharField(default='', max_length=30)),
                ('can_view', models.CharField(default='', max_length=30)),
                ('can_create', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pages', models.CharField(default='', max_length=30)),
                ('total_reports', models.CharField(default='', max_length=30)),
                ('create_time', models.DateTimeField(default=datetime.datetime(2017, 6, 4, 23, 40, 25, 311000))),
            ],
        ),
    ]