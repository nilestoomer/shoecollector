# Generated by Django 5.0.3 on 2024-04-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_wear'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='wear',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='wear',
            name='date',
            field=models.DateField(verbose_name='Wear Date'),
        ),
    ]
