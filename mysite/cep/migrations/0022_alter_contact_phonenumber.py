# Generated by Django 4.0.3 on 2022-05-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cep', '0021_contact_delete_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phonenumber',
            field=models.IntegerField(),
        ),
    ]
