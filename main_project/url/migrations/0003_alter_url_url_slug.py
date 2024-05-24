from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0002_url_url_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url_slug',
            field=models.SlugField(max_length=10, unique=True),
        ),
    ]
