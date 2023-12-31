# Generated by Django 4.2.4 on 2023-09-11 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('window_sill', '0020_alter_sillcategory_manufacturer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now_add=True)),
                ('order_status', models.CharField(choices=[('waiting', 'oczekuje'), ('accepted', 'zaakceptowane'), ('rejected', 'odrzucone'), ('paid', 'opłacone'), ('awaits_payment', 'oczekuje płatności'), ('in_progress', 'w trakcie realizacji')], default='waiting')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('postal_code', models.CharField(default='00-000', max_length=6)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sill_width', models.PositiveSmallIntegerField(default=0)),
                ('sill_thickness', models.PositiveSmallIntegerField(default=0)),
                ('sill_length', models.PositiveSmallIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(max_length=500)),
                ('technical_draw', models.ImageField(null=True, upload_to=order.models.technical_image_file_path)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='order.order')),
                ('window_sill', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='window_sill.windowsill')),
            ],
        ),
    ]
