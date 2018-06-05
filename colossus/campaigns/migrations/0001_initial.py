# Generated by Django 2.0.6 on 2018-06-05 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('campaign_type', models.PositiveSmallIntegerField(choices=[(1, 'Regular'), (2, 'Automated')], default=1, verbose_name='type')),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='lists.MailingList', verbose_name='mailing list')),
            ],
            options={
                'verbose_name': 'campaign',
                'verbose_name_plural': 'campaigns',
            },
        ),
    ]
