# Generated by Django 3.2.21 on 2024-08-27 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cpunca', '0006_auto_20240827_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(default='#')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpunca.categoria1')),
                ('categoria2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpunca.categoria2')),
                ('categoria3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpunca.categoria3')),
            ],
        ),
    ]