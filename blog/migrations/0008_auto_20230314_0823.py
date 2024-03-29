# Generated by Django 3.2.18 on 2023-03-14 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20230314_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=80, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AlterField(
            model_name='about',
            name='post',
            field=models.TextField(max_length=500),
        ),
    ]
