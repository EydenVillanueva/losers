# Generated by Django 2.0.4 on 2018-06-13 22:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
