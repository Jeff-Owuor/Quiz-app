# Generated by Django 4.1 on 2022-08-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('topic', models.CharField(max_length=150)),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='duration of the test in minutes')),
                ('required_score_to_pass', models.IntegerField(help_text='required score in %')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=6)),
            ],
        ),
    ]
