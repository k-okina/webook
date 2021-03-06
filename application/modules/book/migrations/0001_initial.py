# Generated by Django 2.0.1 on 2018-02-19 18:27

from django.db import migrations, models
import modules.book.constants


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('thumbnail_url', models.ImageField(blank=True, null=True, upload_to='images')),
                ('orderd_page_url', models.URLField(blank=True, null=True)),
                ('book_url', models.URLField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(1, 'paper'), (2, 'ebook')], default=modules.book.constants.BookTypes(1))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(blank=True, to='book.Category'),
        ),
    ]
