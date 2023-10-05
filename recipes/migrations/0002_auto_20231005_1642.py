# Generated by Django 3.2.21 on 2023-10-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='dish_type',
            field=models.CharField(choices=[('Main', 'Main'), ('Snack', 'Snack'), ('Dessert', 'Dessert')], default='main', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.CharField(choices=[('10 minutes', '10 min'), ('15 minutes', '15 min'), ('20 minutes', '20 min'), ('25 minutes', '25 min'), ('30 minutes', '30 min'), ('35 minutes', '35 min'), ('40 minutes', '40 min'), ('45 minutes', '45 min'), ('50 minutes', '50 min'), ('55 minutes', '55 min'), ('1 hour', '1h'), ('1+ hour', 'more than 1h')], default='10 minutes', max_length=50),
        ),
    ]