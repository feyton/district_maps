# Generated by Django 3.0.2 on 2020-08-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20200803_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('notify', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='shapedeleterequest',
            name='notify',
            field=models.BooleanField(default=False, verbose_name='notify me'),
        ),
        migrations.AlterField(
            model_name='shapedeleterequest',
            name='reason',
            field=models.TextField(verbose_name='reason for request'),
        ),
        migrations.AlterField(
            model_name='shapedeleterequest',
            name='user',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
    ]
