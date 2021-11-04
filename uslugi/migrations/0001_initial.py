# Generated by Django 3.2.3 on 2021-11-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uslugi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.TextField()),
                ('foto', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Usługi',
                'verbose_name_plural': 'Usługi',
            },
        ),
    ]