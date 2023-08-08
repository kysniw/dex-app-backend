# Generated by Django 4.2.3 on 2023-08-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('window_sill', '0010_windowsill_sill_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='windowsill',
            name='price',
        ),
        migrations.AddField(
            model_name='sillthickness',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='sillwidth',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='sillcategory',
            name='manufacturer',
            field=models.CharField(choices=[('wiech', 'wiech'), ('kobax', 'kobax'), ('dex', 'dex')], default='dex'),
        ),
        migrations.AlterField(
            model_name='sillcategory',
            name='max_width',
            field=models.PositiveSmallIntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='sillcategory',
            name='min_width',
            field=models.PositiveSmallIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='sillcategory',
            name='price_unit',
            field=models.CharField(choices=[('mb', 'mb'), ('m2', 'm2')], default='mb'),
        ),
    ]
