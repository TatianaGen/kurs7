# Generated by Django 5.0.1 on 2024-09-01 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200, verbose_name='Место привычки')),
                ('time', models.DateTimeField(verbose_name='Дата и время привычки')),
                ('action', models.CharField(max_length=200, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(verbose_name='Приятная')),
                ('frequency_number', models.PositiveIntegerField(verbose_name='Количество раз')),
                ('frequency_unit', models.CharField(choices=[('minutes', 'минуты'), ('hours', 'часы'), ('days', 'дни')], default='days', max_length=10, verbose_name='Единицы измерения')),
                ('reward', models.CharField(blank=True, max_length=200, null=True, verbose_name='Вознаграждение')),
                ('duration', models.DurationField(verbose_name='Длительность действия')),
                ('is_public', models.BooleanField(default=True, verbose_name='Публичная')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
