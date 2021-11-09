# Generated by Django 2.2.10 on 2021-11-08 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('voter_id', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='poller.PollQuestion')),
            ],
        ),
    ]
