# Generated by Django 3.0.2 on 2020-07-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_member_testimony'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('summary', models.TextField()),
            ],
        ),
    ]