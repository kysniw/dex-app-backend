# Generated by Django 4.2.3 on 2023-07-31 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('window_sill', '0004_alter_sillcategory_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sillcategory',
            name='manufacturer',
            field=models.CharField(choices=[('kobax', 'kobax'), ('wiech', 'wiech'), ('dex', 'dex')], default='dex'),
        ),
    ]
