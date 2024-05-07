# Generated by Django 4.2.12 on 2024-05-07 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("DjangoProject", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Consumer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="account",
            name="consumer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="DjangoProject.consumer",
            ),
        ),
    ]
