# Generated by Django 3.1.14 on 2024-01-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('0', 'カスタマー'), ('1', 'スタッフ')], default='0', max_length=1),
        ),
    ]
