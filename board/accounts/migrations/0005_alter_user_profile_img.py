# Generated by Django 4.0 on 2022-02-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_color_user_point_user_profile_img_delete_mypage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, default='accounts/person.png', null=True, upload_to='accounts/'),
        ),
    ]
