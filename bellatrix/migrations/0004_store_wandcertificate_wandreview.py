# Generated by Django 5.0.7 on 2024-07-21 08:43

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bellatrix', '0003_wandvariety_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('wand_varieties', models.ManyToManyField(related_name='stores', to='bellatrix.wandvariety')),
            ],
        ),
        migrations.CreateModel(
            name='WandCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(max_length=100)),
                ('issued_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_untill', models.DateTimeField()),
                ('wand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='bellatrix.wandvariety')),
            ],
        ),
        migrations.CreateModel(
            name='WandReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='bellatrix.wandvariety')),
            ],
        ),
    ]
