# Generated by Django 4.0.5 on 2022-06-16 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('my_order', models.PositiveIntegerField(db_index=True, default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('my_order', models.PositiveIntegerField(db_index=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.book')),
            ],
        ),
        migrations.CreateModel(
            name='Book1',
            fields=[
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books (ordered by model, no inlines)',
                'ordering': ['my_order'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.book',),
        ),
        migrations.CreateModel(
            name='Book2',
            fields=[
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books (reverse ordered by model, no inlines)',
                'ordering': ['-my_order'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.book',),
        ),
        migrations.CreateModel(
            name='Book3',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.book',),
        ),
        migrations.CreateModel(
            name='Book4',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.book',),
        ),
        migrations.CreateModel(
            name='Book5',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.book',),
        ),
        migrations.CreateModel(
            name='Book6',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.book',),
        ),
        migrations.CreateModel(
            name='Book7',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.book',),
        ),
        migrations.CreateModel(
            name='Chapter1',
            fields=[
            ],
            options={
                'ordering': ['my_order'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.chapter',),
        ),
        migrations.CreateModel(
            name='Chapter2',
            fields=[
            ],
            options={
                'ordering': ['-my_order'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.chapter',),
        ),
        migrations.CreateModel(
            name='Book11',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.book1',),
        ),
        migrations.CreateModel(
            name='Book22',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.book2',),
        ),
    ]