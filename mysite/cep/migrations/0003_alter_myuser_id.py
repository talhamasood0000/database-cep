# Generated by Django 4.0.3 on 2022-04-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cep', '0002_alter_activities_event_id_alter_corebody_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]