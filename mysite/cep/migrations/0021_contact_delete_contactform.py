# Generated by Django 4.0.3 on 2022-05-14 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cep', '0020_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phonenumber', models.IntegerField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
