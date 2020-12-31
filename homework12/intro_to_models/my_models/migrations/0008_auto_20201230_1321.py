# Generated by Django 3.1.4 on 2020-12-30 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_models", "0007_auto_20201230_1319"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homeworkresult",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="my_models.student",
            ),
        ),
        migrations.AlterField(
            model_name="homeworkresult",
            name="homework",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="my_models.homework",
            ),
        ),
    ]