# Generated by Django 3.0.1 on 2019-12-22 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(choices=[('Strongly Agree', 'Strongly Agree'), ('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree'), ('Strongly Disagree', 'Strongly Disagree')], max_length=200)),
                ('strong_agree_change', models.IntegerField(default=0)),
                ('agree_change', models.IntegerField(default=0)),
                ('neutral_change', models.IntegerField(default=0)),
                ('disagree_change', models.IntegerField(default=0)),
                ('strong_disagree_change', models.IntegerField(default=0)),
            ],
        ),
    ]