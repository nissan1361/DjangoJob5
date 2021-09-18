# Generated by Django 3.2.7 on 2021-09-18 08:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('date_published', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='QuestionCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Вопрос с чек боксами')),
                ('date_published', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Вопрос (чек бокс)',
                'verbose_name_plural': 'Вопросы (чек бокс)',
            },
        ),
        migrations.CreateModel(
            name='QuestionText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Вопрос с текстовым ответом')),
                ('date_published', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Вопрос (ответ текст)',
                'verbose_name_plural': 'Вопросы (ответ текст)',
            },
        ),
        migrations.CreateModel(
            name='AnswerText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, verbose_name='Текст ответа')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.questiontext')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='AnswerCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, verbose_name='Ответ')),
                ('votes', models.IntegerField(default=0, verbose_name='Голосов')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.questioncheck')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, verbose_name='Ответ')),
                ('votes', models.IntegerField(default=0, verbose_name='Голосов')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
