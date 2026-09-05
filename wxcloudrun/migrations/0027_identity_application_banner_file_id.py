from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxcloudrun', '0026_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='identityapplication',
            name='merchant_banner_file_id',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='商户展示图云文件ID'),
        ),
    ]
