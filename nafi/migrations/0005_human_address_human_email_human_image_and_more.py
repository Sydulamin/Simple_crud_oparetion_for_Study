# Generated by Django 5.0.1 on 2024-01-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nafi', '0004_alter_human_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='address',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='human',
            name='email',
            field=models.EmailField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='human',
            name='image',
            field=models.ImageField(blank=True, default='def.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='human',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=7, null=True),
        ),
    ]