# Generated by Django 4.2.19 on 2025-05-01 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A'),
        ),
    ]
