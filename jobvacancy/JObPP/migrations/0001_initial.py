# Generated by Django 4.1.4 on 2023-04-10 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('jobdescription', models.CharField(max_length=50)),
                ('vacancy', models.IntegerField()),
                ('applied', models.IntegerField()),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JObPP.city')),
            ],
        ),
    ]
