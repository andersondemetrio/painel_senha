# Generated by Django 4.0.5 on 2022-06-20 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totem', '0006_alter_totem_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totem',
            name='horario',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]