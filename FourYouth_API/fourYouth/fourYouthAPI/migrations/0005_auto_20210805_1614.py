# Generated by Django 3.1.3 on 2021-08-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourYouthAPI', '0004_auto_20210805_1609'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='addtocart',
            constraint=models.UniqueConstraint(fields=('productfk', 'userfk'), name='AddToCart Constraints'),
        ),
    ]