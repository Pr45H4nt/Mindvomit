# Generated by Django 4.0.6 on 2022-08-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_posts_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=200)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]