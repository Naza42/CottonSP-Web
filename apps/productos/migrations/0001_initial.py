# Generated by Django 5.0.2 on 2024-03-12 12:52

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_principal', models.ImageField(upload_to='productos/')),
                ('imagen_2', models.ImageField(blank=True, default='img/hero-banner.jpg', null=True, upload_to='productos/')),
                ('imagen_3', models.ImageField(blank=True, default='img/hero-banner.jpg', null=True, upload_to='productos/')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', ckeditor.fields.RichTextField(max_length=700)),
                ('resumen', ckeditor.fields.RichTextField(blank=True, max_length=256)),
                ('resumen_2', ckeditor.fields.RichTextField(blank=True, max_length=700)),
                ('url', models.URLField(blank=True, null=True)),
                ('categoria', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='noticias.categoria')),
            ],
        ),
    ]