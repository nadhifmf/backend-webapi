# Generated by Django 4.1 on 2022-08-26 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField(blank=True, null=True)),
                ('valuation', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
            ],
        ),
    ]
