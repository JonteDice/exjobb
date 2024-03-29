# Generated by Django 5.0.2 on 2024-02-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer_1', models.CharField(max_length=255)),
                ('answer_2', models.CharField(max_length=255)),
                ('answer_3', models.CharField(max_length=255)),
                ('total_1', models.IntegerField(default=0)),
                ('total_2', models.IntegerField(default=0)),
                ('total_3', models.IntegerField(default=0)),
            ],
        ),
    ]
