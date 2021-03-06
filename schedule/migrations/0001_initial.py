# Generated by Django 3.2.4 on 2021-06-28 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.CharField(max_length=255)),
                ('place', models.IntegerField(default=60)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.film')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.film')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.schedule')),
            ],
        ),
    ]
