# Generated by Django 4.2.7 on 2023-11-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_form', models.CharField(max_length=250)),
                ('second_form', models.CharField(max_length=250)),
                ('third_form', models.CharField(max_length=250)),
                ('translation_to_uzbek', models.CharField(blank=True, max_length=250)),
                ('example_first', models.TextField(blank=True)),
                ('example_second', models.TextField(blank=True)),
                ('example_third', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-first_form'],
            },
        ),
    ]
