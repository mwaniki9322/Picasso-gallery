# Generated by Django 3.2 on 2021-09-04 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('image_description', models.TextField(max_length=300)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.locations')),
            ],
        ),
    ]
