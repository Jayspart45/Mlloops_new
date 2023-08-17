# Generated by Django 3.1.4 on 2021-03-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('io_storages', '0001_squashed_0002_auto_20210302_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='azureblobexportstorage',
            name='last_sync',
            field=models.DateTimeField(blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync'),
        ),
        migrations.AddField(
            model_name='azureblobexportstorage',
            name='last_sync_count',
            field=models.PositiveIntegerField(blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count'),
        ),
        migrations.AddField(
            model_name='azureblobimportstorage',
            name='last_sync',
            field=models.DateTimeField(blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync'),
        ),
        migrations.AddField(
            model_name='azureblobimportstorage',
            name='last_sync_count',
            field=models.PositiveIntegerField(blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count'),
        ),
        migrations.AddField(
            model_name='gcsexportstorage',
            name='last_sync',
            field=models.DateTimeField(blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync'),
        ),
        migrations.AddField(
            model_name='gcsexportstorage',
            name='last_sync_count',
            field=models.PositiveIntegerField(blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count'),
        ),
        migrations.AddField(
            model_name='gcsimportstorage',
            name='last_sync',
            field=models.DateTimeField(blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync'),
        ),
        migrations.AddField(
            model_name='gcsimportstorage',
            name='last_sync_count',
            field=models.PositiveIntegerField(blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count'),
        ),
        migrations.AddField(
            model_name='redisexportstorage',
            name='last_sync',
            field=models.DateTimeField(blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync'),
        ),
        migrations.AddField(
            model_name='redisexportstorage',
            name='last_sync_count',
            field=models.PositiveIntegerField(blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count'),
        ),
        migrations.AddField(
            model_name='redisimportstorage',
            name='last_sync',
            field=models.DateTimeField(blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync'),
        ),
        migrations.AddField(
            model_name='redisimportstorage',
            name='last_sync_count',
            field=models.PositiveIntegerField(blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count'),
        ),
        migrations.AddField(
            model_name='s3exportstorage',
            name='last_sync',
            field=models.DateTimeField(blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync'),
        ),
        migrations.AddField(
            model_name='s3exportstorage',
            name='last_sync_count',
            field=models.PositiveIntegerField(blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count'),
        ),
        migrations.AddField(
            model_name='s3importstorage',
            name='last_sync',
            field=models.DateTimeField(blank=True, help_text='Last sync finished time', null=True, verbose_name='last sync'),
        ),
        migrations.AddField(
            model_name='s3importstorage',
            name='last_sync_count',
            field=models.PositiveIntegerField(blank=True, help_text='Count of tasks synced last time', null=True, verbose_name='last sync count'),
        ),
    ]
