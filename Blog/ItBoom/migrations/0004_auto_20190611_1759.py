# Generated by Django 2.2.2 on 2019-06-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItBoom', '0003_auto_20190611_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runablednews',
            name='title',
            field=models.TextField(),
        ),
    ]
