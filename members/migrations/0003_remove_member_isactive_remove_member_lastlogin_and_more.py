# Generated by Django 4.2.16 on 2024-12-02 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0002_member_delete_memberlogin"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="member",
            name="IsActive",
        ),
        migrations.RemoveField(
            model_name="member",
            name="LastLogin",
        ),
        migrations.RemoveField(
            model_name="member",
            name="MembershipID",
        ),
    ]
