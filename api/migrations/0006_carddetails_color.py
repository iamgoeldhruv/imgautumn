# Generated by Django 4.2.5 on 2023-10-02 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='carddetails',
            name='color',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
