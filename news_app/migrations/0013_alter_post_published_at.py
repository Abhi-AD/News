# Generated by Django 4.2.3 on 2023-08-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0012_alter_newsletter_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
