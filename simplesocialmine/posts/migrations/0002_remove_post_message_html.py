# Generated by Django 2.2.5 on 2020-03-02 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='message_html',
        ),
    ]