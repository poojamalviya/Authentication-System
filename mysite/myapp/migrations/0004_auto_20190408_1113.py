# Generated by Django 2.2 on 2019-04-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190408_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default='poojamalviya7760@gmail.com', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='pooja', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pooja@123', editable=False, max_length=255),
        ),
    ]