# Generated by Django 5.2.1 on 2025-05-25 03:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('cover', models.ImageField(upload_to='covers/')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='manga.manga')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pages/')),
                ('page_number', models.PositiveIntegerField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='manga.chapter')),
            ],
            options={
                'ordering': ['page_number'],
            },
        ),
    ]
