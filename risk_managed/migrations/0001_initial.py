# Generated by Django 2.2.4 on 2019-08-15 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date_of_event', models.DateField()),
                ('time_of_event', models.CharField(choices=[('', 'Hour of Event'), ('12 PM', '12 PM'), ('01 PM', '01 PM'), ('02 PM', '02 PM'), ('03 PM', '03 PM'), ('04 PM', '04 PM'), ('05 PM', '05 PM'), ('06 PM', '06 PM'), ('07 PM', '07 PM'), ('08 PM', '08 PM'), ('09 PM', '09 PM'), ('10 PM', '10 PM'), ('11 PM', '11 PM'), ('12 AM', '12 AM'), ('01 AM', '01 AM'), ('02 AM', '02 AM'), ('03 AM', '03 AM'), ('04 AM', '04 AM'), ('05 AM', '05 AM'), ('06 AM', '06 AM'), ('07 AM', '07 AM'), ('08 AM', '08 AM'), ('09 AM', '09 AM'), ('10 AM', '10 AM'), ('11 AM', '11 AM')], max_length=40)),
                ('event_location', models.CharField(choices=[('', 'Where is the event located?'), ('Chapter House', 'Chapter House'), ('Other Campus Venue', 'Other Campus Venue'), ('Off Campus', 'Off Campus')], max_length=100)),
                ('event_location_other', models.CharField(blank=True, max_length=100, null=True)),
                ('name_of_planner', models.CharField(max_length=100)),
                ('phone_number_of_planner', models.CharField(max_length=40)),
                ('email_of_planner', models.CharField(max_length=40)),
                ('expected_number_guests', models.IntegerField()),
                ('affiliated_council', models.CharField(choices=[('', 'Affiliated Council'), ('Interfraternity Council', 'Interfraternity Council'), ('Panhellenic', 'Panhellenic'), ('NPHC', 'NPHC'), ('Non-Affiliated', 'Non-Affiliated')], max_length=40)),
                ('type_of_event', models.CharField(choices=[('', 'Type of Event'), ('Social', 'Social'), ('Date Function', 'Date Function'), ('Formal', 'Formal'), ('Other', 'Other')], max_length=40)),
                ('type_event_other', models.CharField(blank=True, max_length=100, null=True)),
                ('event_description', models.TextField()),
                ('invitation_type', models.CharField(choices=[('', 'Choose One'), ('Invitation Only', 'Invitation Only'), ('Open to the Public', 'Open to the Public'), ('Open to Faculty, Staff, Students', 'Open to Faculty, Staff, Students')], max_length=100)),
                ('transportation', models.TextField(blank=True, null=True)),
                ('one_entry_point', models.CharField(choices=[('', 'Will there be one entry point?'), ('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('entry_point_location', models.CharField(max_length=100)),
                ('co_sponsored_description', models.TextField(blank=True, null=True)),
                ('alcohol_distribution', models.TextField(blank=True, null=True)),
                ('sober_monitors', models.TextField()),
                ('presidents_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('event', models.ManyToManyField(to='risk_managed.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('acronym', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='risk_managed.Administrator')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_managed.Organization')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_managed.University')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuestImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/guests')),
                ('date_time_taken', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_managed.Event')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_managed.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(choices=[('', 'Select severity of violation'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=10)),
                ('category', models.CharField(choices=[('', 'Select category for flag'), ('Underage Drinking', 'Underage Drinking'), ('Stealing', 'Stealing'), ('Vandalism', 'Vandalism'), ('Violence', 'Violence'), ('Other', 'Other')], max_length=20)),
                ('other_description', models.CharField(blank=True, help_text='If you chose other, fill in description', max_length=30, null=True)),
                ('administrator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='risk_managed.Administrator')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_managed.Guest')),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='risk_managed.Host')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_managed.Host'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk_managed.University'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
