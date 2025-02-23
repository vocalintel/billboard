# Generated by Django 4.1.7 on 2023-02-19 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('email', models.CharField(max_length=150, verbose_name='Email')),
                ('options', models.CharField(choices=[('Send me a brochure', 'Send me a brochure'), ('I want more details from Keesha Billboard', 'I want more details from Keesha Billboard'), ('I want to partner with Keesha Billboard', 'I want to partner with Keesha Billboard')], max_length=150, verbose_name='Informations')),
                ('info', models.TextField(max_length=150, verbose_name='More Information')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='SetUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compname', models.CharField(max_length=50, verbose_name='Company Name')),
                ('compemail', models.CharField(default='youremail@gmail.com', max_length=50, verbose_name='Company Email')),
                ('phone', models.CharField(max_length=150, verbose_name='Company Phone Number')),
                ('pricing', models.CharField(choices=[('100000', '100000'), ('200000', '200000'), ('300000', '300000')], max_length=150, verbose_name='Select Subscription Billings')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.OneToOneField(default='nouser', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50, verbose_name='Product name')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.OneToOneField(default='nouser', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Advert name')),
                ('desc', models.CharField(max_length=150, verbose_name='Description')),
                ('time', models.CharField(choices=[('1s', '1s'), ('2s', '2s'), ('3s', '3s'), ('4s', '4s'), ('5s', '5s'), ('6s', '6s'), ('7s', '7s'), ('8s', '8s'), ('9s', '9s'), ('10s', '10s'), ('11s', '11s'), ('12s', '12s'), ('13s', '13s'), ('14s', '14s'), ('15s', '15s'), ('16s', '16s'), ('17s', '17s'), ('18s', '18s'), ('19s', '19s'), ('20s', '20s'), ('21s', '21s'), ('22s', '22s'), ('23s', '23s'), ('24s', '24s'), ('25s', '25s'), ('26s', '26s'), ('27s', '27s'), ('28s', '28s'), ('29s', '29s'), ('30s', '30s')], max_length=150, verbose_name='Time Frame')),
                ('plan', models.CharField(choices=[('Fade', 'Fade'), ('Cross Fade', 'Cross Fade'), ('Fade With Black', 'Fade With Black'), ('Fade With White', 'Fade With White'), ('Fade With Color', 'Fade With Color')], max_length=150, verbose_name='Advert Transition')),
                ('date', models.DateField(verbose_name='start Date to Display Advert')),
                ('options', models.CharField(choices=[('Digital(Gantry)', 'Digital(Gantry)'), ('Digital(Mega Site)', 'Digital(Mega Site)'), ('Digital(Light Box)', 'Digital(Light Box)'), ('Digital(Unipole)', 'Digital(Unipole)'), ('Digital(Wall Drape)', 'Digital(Wall Drape)'), ('Digital(Roof Top)', 'Digital(Roof Top)'), ('Digital(Super 48 Sheet)', 'Digital(Super 48 Sheet)'), ('Traditional(Gantry)', 'Traditional(Gantry)'), ('Traditional(Mega Site)', 'Traditional(Mega Site)'), ('Traditional(Light Box)', 'Traditional(Light Box)'), ('Traditional(Unipole)', 'Traditional(Unipole)'), ('Traditional(Wall Drape)', 'Traditional(Wall Drape)'), ('Traditional(Roof Top)', 'Traditional(Roof Top)'), ('Traditional(Super 48 Sheet)', 'Traditional(Super 48 Sheet)')], max_length=150, verbose_name='Type of Billboard')),
                ('Sunday', models.BooleanField(default=False)),
                ('Monday', models.BooleanField(default=False)),
                ('Tuesday', models.BooleanField(default=False)),
                ('Wednesday', models.BooleanField(default=False)),
                ('Thursday', models.BooleanField(default=False)),
                ('Friday', models.BooleanField(default=False)),
                ('Saturday', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='', verbose_name='Select Advert Image to Upload')),
                ('location', models.CharField(max_length=150, verbose_name='Location')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.OneToOneField(default='nouser', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
