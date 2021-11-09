# Generated by Django 2.2.10 on 2021-11-08 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_closed', models.DateTimeField(null=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type', models.CharField(choices=[('TEXT', 'Ответ текстом'), ('SINGLE_CHOICE', 'Один ответ'), ('MULTIPLE_CHOICE', 'Несколько ответов')], max_length=20)),
                ('deleted', models.DateTimeField(null=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='poller.Poll')),
            ],
        ),
    ]
