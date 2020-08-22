# Generated by Django 2.2 on 2020-08-16 15:03

from django.db import migrations, models
import django.db.models.deletion
import plants.utils


class Migration(migrations.Migration):

    dependencies = [("plants", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="plantpicture",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=plants.utils.upload_image_path
            ),
        ),
        migrations.AlterField(
            model_name="plantpicture",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="plants.Plant",
            ),
        ),
        migrations.AlterField(
            model_name="plantpicture",
            name="profile_plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="plants.ProfilePlant",
            ),
        ),
    ]