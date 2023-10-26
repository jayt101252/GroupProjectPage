# Generated by Django 4.2.6 on 2023-10-26 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_director_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geeks_field', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='director',
            name='director_photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
