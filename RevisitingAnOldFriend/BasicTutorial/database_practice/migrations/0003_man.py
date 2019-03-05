# Generated by Django 2.1.7 on 2019-03-04 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database_practice', '0002_auto_20190304_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_practice.Person')),
            ],
        ),
    ]
