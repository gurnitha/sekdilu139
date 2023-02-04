# Generated by Django 4.1.5 on 2023-01-24 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekdilu139', '0002_alter_category_options_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rank', to='sekdilu139.category')),
                ('sub_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_rank', to='sekdilu139.category')),
            ],
            options={
                'verbose_name_plural': 'Ranks',
            },
        ),
    ]
