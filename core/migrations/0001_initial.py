# Generated by Django 3.0.8 on 2020-11-09 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(choices=[('IT', 'IT'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('ME', 'ME'), ('EE', 'EE'), ('CE', 'CE')], default='IT', max_length=25)),
                ('year', models.CharField(choices=[('Freshie', 1), ('2nd', 2), ('3rd', 3), ('Godfather', 4), ('Alumni', 5)], default='Freshie', max_length=25)),
                ('subject', models.CharField(max_length=50)),
                ('comments', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Contact us Records',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=25, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='level_images')),
                ('audio', models.FileField(blank=True, null=True, upload_to='level_images')),
                ('author', models.CharField(blank=True, max_length=25, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('quote', models.CharField(blank=True, max_length=100, null=True)),
                ('hint', models.TextField(blank=True, max_length=250, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_last', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='QuizTakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answers', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clear', models.IntegerField(default=0)),
                ('department', models.CharField(choices=[('IT', 'IT'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('ME', 'ME'), ('EE', 'EE'), ('CE', 'CE')], default='IT', max_length=25)),
                ('year', models.CharField(choices=[('Freshie', 1), ('2nd', 2), ('3rd', 3), ('Godfather', 4), ('Alumni', 5)], default='Freshie', max_length=25)),
                ('college', models.CharField(default='JGEC', max_length=60)),
                ('picture_url', models.URLField(blank=True, null=True)),
                ('is_previously_logged', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Answer')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Level')),
                ('quiztaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.QuizTakers')),
            ],
        ),
        migrations.AddField(
            model_name='quiztakers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LevelPublish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=False)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Level')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'Level Published',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Level'),
        ),
    ]
