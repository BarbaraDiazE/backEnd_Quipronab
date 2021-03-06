# Generated by Django 2.1 on 2020-03-02 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0003_auto_20200228_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinformation',
            name='MW_high',
            field=models.IntegerField(blank=True, default=10, help_text='high MW', verbose_name='MW'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='generalinformation',
            name='MW_low',
            field=models.IntegerField(blank=True, default=1, help_text='low MW', verbose_name='MW'),
            preserve_default=False,
        ),
    ]
