# Generated by Django 2.2.10 on 2021-11-09 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poller', '0013_auto_20211109_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answers', to='poller.PollQuestion'),
        ),
    ]
