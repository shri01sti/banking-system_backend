# Generated by Django 4.1.3 on 2022-12-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_transaction_transactiondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transactionDate',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
