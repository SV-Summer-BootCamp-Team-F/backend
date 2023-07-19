# Generated by Django 3.2.6 on 2023-07-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('phone_num', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]