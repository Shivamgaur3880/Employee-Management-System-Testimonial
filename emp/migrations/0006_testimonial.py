# Generated by Django 4.2 on 2023-05-15 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0005_alter_employee_address_alter_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('testimonial', models.TextField()),
                ('picture', models.ImageField(upload_to='testimonial/')),
                ('rating', models.IntegerField(max_length=1)),
            ],
        ),
    ]