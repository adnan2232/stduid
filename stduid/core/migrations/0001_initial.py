# Generated by Django 4.0.3 on 2022-03-29 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_id', models.IntegerField()),
                ('college_uid', models.CharField(max_length=70, unique=True)),
                ('college_name', models.CharField(max_length=100)),
                ('college_detail', models.CharField(blank=True, default='No Detail', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_uid', models.CharField(max_length=20, unique=True)),
                ('state_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_id', models.IntegerField()),
                ('uni_uid', models.CharField(max_length=50, unique=True)),
                ('uni_name', models.CharField(max_length=100)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.state')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_grno', models.IntegerField()),
                ('student_uid', models.CharField(max_length=100, unique=True)),
                ('student_name', models.CharField(max_length=100)),
                ('student_detail', models.CharField(blank=True, default='No detail', max_length=10000)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.college')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.state')),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.university')),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.state'),
        ),
        migrations.AddField(
            model_name='college',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.university'),
        ),
    ]
