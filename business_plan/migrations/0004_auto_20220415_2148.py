# Generated by Django 3.2 on 2022-04-15 19:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_plan', '0003_alter_question_offered_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessplan',
            name='name',
            field=models.CharField(default='business_plan_1', max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('business_plan', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='businessplan',
            unique_together={('name', 'user')},
        ),
    ]
