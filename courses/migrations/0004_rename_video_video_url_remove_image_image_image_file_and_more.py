# Generated by Django 4.1.4 on 2022-12-28 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('courses', '0003_alter_content_options_alter_module_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='file',
            field=models.FileField(default=0, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('text', 'video', 'image', 'file')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='content',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='courses.module'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
