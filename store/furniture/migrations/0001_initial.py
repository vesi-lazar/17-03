# Generated by Django 3.0 on 2019-12-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('image_url', models.URLField()),
                ('material', models.CharField(choices=[('P', 'PDC'), ('M', 'MDC'), ('W', 'Wooden')], max_length=1)),
            ],
        ),
    ]
