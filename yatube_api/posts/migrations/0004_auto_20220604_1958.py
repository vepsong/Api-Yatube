# Generated by Django 2.2.16 on 2022-06-04 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220604_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={},
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique',
        ),
    ]