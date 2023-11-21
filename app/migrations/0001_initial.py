# Generated by Django 4.2.7 on 2023-11-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.CharField(blank=True, max_length=40, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TMS_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
