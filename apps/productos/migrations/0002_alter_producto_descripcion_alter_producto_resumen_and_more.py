# Generated by Django 5.0.2 on 2024-02-29 20:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=ckeditor.fields.RichTextField(max_length=256),
        ),
        migrations.AlterField(
            model_name='producto',
            name='resumen',
            field=ckeditor.fields.RichTextField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='producto',
            name='resumen_2',
            field=ckeditor.fields.RichTextField(blank=True, max_length=256),
        ),
    ]