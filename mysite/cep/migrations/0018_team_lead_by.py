# Generated by Django 4.0.3 on 2022-04-30 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cep', '0017_alter_activities_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='lead_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cep.executivemembers'),
            preserve_default=False,
        ),
    ]