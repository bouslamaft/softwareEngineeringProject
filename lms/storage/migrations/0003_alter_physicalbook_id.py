# Generated by Django 4.1.5 on 2023-01-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_author_category_book_authors_book_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalbook',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
