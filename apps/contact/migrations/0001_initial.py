# Generated by Django 3.1.3 on 2021-03-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
                ('send_on', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(blank=True, default='False', null=True)),
            ],
        ),
    ]
