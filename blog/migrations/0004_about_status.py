# Generated by Django 3.2.18 on 2023-03-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230313_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
