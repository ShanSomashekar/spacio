# Generated by Django 4.2.16 on 2024-11-22 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("view", "0003_rename_occupation_status_spaces_occupationstatus_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="spaces",
            name="FloorPlan",
        ),
        migrations.RemoveField(
            model_name="spaces",
            name="Location",
        ),
        migrations.AlterField(
            model_name="spaces",
            name="SpaceID",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
