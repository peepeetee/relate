# Generated by Django 1.10 on 2016-08-08 22:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0091_changes_found_for_py3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examticket',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='flowaccessexception',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='flowpagevisit',
            name='impersonated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='impersonator', to=settings.AUTH_USER_MODEL, verbose_name='Impersonated by'),
        ),
        migrations.AlterField(
            model_name='flowpagevisit',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visitor', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='flowpagevisitgrade',
            name='grader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Grader'),
        ),
        migrations.AlterField(
            model_name='flowruleexception',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='flowsession',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='gradechange',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='gradechange',
            name='flow_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grade_changes', to='course.FlowSession', verbose_name='Flow session'),
        ),
        migrations.AlterField(
            model_name='participationpreapproval',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
    ]
