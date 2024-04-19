# Generated by Django 4.2.11 on 2024-04-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(default='goods', max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='image')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('discount', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('archived', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name', 'price'],
            },
        ),
    ]