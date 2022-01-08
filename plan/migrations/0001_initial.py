# Generated by Django 3.1.14 on 2022-01-08 18:29

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_remove_user_phone_num'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Routine', 'Routine'), ('Growth', 'Growth')], max_length=30)),
                ('main_img_url', models.URLField()),
                ('name', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField(default=0)),
                ('writer_name', models.CharField(max_length=20)),
                ('writer_img', models.URLField(blank=True, null=True)),
                ('writer_intro', models.CharField(max_length=30)),
                ('intro_img_url', models.URLField()),
                ('desc', models.TextField()),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img_url', models.URLField()),
                ('date', models.PositiveIntegerField(default=0)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.plan')),
            ],
        ),
        migrations.CreateModel(
            name='User_plan_todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish_flag', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('plan_todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.plan_todo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='User_Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_flag', models.BooleanField(default=False)),
                ('register_flag', models.BooleanField(default=False)),
                ('own_flag', models.BooleanField(default=False)),
                ('finish_flag', models.BooleanField(default=False)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='plan.plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_todo_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('video_url', models.URLField()),
                ('desc', models.TextField()),
                ('plan_todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.plan_todo')),
            ],
        ),
    ]
