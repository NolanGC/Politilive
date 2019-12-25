# Generated by Django 3.0.1 on 2019-12-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politilive', '0002_auto_20191222_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='agree_change',
            new_name='agree_xchange',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='disagree_change',
            new_name='agree_ychange',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='neutral_change',
            new_name='disagree_xchange',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='strong_agree_change',
            new_name='disagree_ychange',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='strong_disagree_change',
            new_name='neutral_xchange',
        ),
        migrations.AddField(
            model_name='question',
            name='neutral_ychange',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='strong_agree_xchange',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='strong_agree_ychange',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='strong_disagree_xchange',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='strong_disagree_ychange',
            field=models.IntegerField(default=0),
        ),
    ]
