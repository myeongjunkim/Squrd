# Generated by Django 4.0 on 2022-01-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0002_article_entertain_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
