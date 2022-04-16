# Generated by Django 3.2 on 2022-04-15 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTimestamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfferedAnswer',
            fields=[
                ('basetimestamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='business_plan.basetimestamp')),
                ('text', models.CharField(max_length=255, unique=True, verbose_name='Text')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Offered Answer',
                'verbose_name_plural': 'Offered Answers',
            },
            bases=('business_plan.basetimestamp',),
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('basetimestamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='business_plan.basetimestamp')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Question Type',
                'verbose_name_plural': 'Question Types',
            },
            bases=('business_plan.basetimestamp',),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('basetimestamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='business_plan.basetimestamp')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
            bases=('business_plan.basetimestamp',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, unique=True, verbose_name='Text')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('offered_answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='business_plan.offeredanswer', verbose_name='Offered Answer')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='business_plan.section', verbose_name='Section')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='business_plan.questiontype', verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='BusinessPlan',
            fields=[
                ('basetimestamp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='business_plan.basetimestamp')),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='business_plans', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Business Plan',
                'verbose_name_plural': 'Business Plans',
            },
            bases=('business_plan.basetimestamp',),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_postive_int', models.PositiveIntegerField(blank=True, null=True, verbose_name='Answer Positive Integer')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers', to='business_plan.question', verbose_name='Question')),
                ('business_plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers', to='business_plan.businessplan', verbose_name='Business Plan')),
                ('offered_answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='answers', to='business_plan.offeredanswer', verbose_name='Offered Answer')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
    ]