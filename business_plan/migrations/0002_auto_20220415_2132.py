# Generated by Django 3.2 on 2022-04-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_plan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='offered_answer',
        ),
        migrations.AddField(
            model_name='question',
            name='offered_answer',
            field=models.ManyToManyField(to='business_plan.OfferedAnswer', verbose_name='Offered Answer'),
        ),
    ]
