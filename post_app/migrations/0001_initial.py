# Generated by Django 4.0.4 on 2022-05-21 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.CharField(max_length=155, verbose_name='имя')),
            ],
            options={
                'verbose_name': 'Директория',
                'verbose_name_plural': 'Директории',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='названия')),
                ('descriptions', models.TextField(verbose_name='Описания')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_app.movie')),
            ],
            options={
                'verbose_name': 'Отзыв',
            },
        ),
        migrations.CreateModel(
            name='Movie_commits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=12)),
                ('text', models.TextField()),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_app.movie')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(blank=True, to='post_app.tag', verbose_name='Тэги'),
        ),
    ]