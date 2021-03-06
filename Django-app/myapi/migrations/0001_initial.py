# Generated by Django 3.0.5 on 2020-04-23 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='approvals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('dependants', models.IntegerField()),
                ('applicant_income', models.IntegerField()),
                ('coapplicant_income', models.IntegerField()),
                ('loan_amount', models.IntegerField()),
                ('loan_term', models.IntegerField()),
                ('credit_history', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=15)),
                ('married', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
                ('graduate_education', models.CharField(choices=[('Graduate', 'Graduate'), ('Not_Graduate', 'Not_Graduate')], max_length=15)),
                ('self_employed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
                ('area', models.CharField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')], max_length=15)),
            ],
        ),
    ]
