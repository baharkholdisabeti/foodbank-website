# Generated by Django 3.1.1 on 2020-11-22 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_ID', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(default='NULL', max_length=200)),
                ('branch_info', models.TextField(max_length=250)),
            ],
            options={
                'ordering': ['branch_ID'],
            },
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('need_ID', models.AutoField(primary_key=True, serialize=False)),
                ('need_str', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['need_ID'],
            },
        ),
        migrations.CreateModel(
            name='BranchNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodbank.branch')),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodbank.need')),
            ],
            options={
                'ordering': ['branch_ID'],
            },
        ),
    ]
