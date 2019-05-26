# Generated by Django 2.2.1 on 2019-05-18 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='amount',
            field=models.DecimalField(decimal_places=2, help_text='loan amount in dollars.', max_digits=12),
        ),
        migrations.AlterField(
            model_name='loan',
            name='client_id',
            field=models.ForeignKey(default=None, help_text='unique id of a client. ', on_delete=django.db.models.deletion.PROTECT, related_name='loans', to='clients.Client'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='date',
            field=models.DateTimeField(help_text='when the loan was requested (origination date as an ISO 8601 string).'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='instalment',
            field=models.DecimalField(decimal_places=2, help_text='monthly loan payment.', max_digits=12),
        ),
        migrations.AlterField(
            model_name='loan',
            name='rate',
            field=models.DecimalField(decimal_places=4, help_text='interest rate as decimal.', max_digits=4),
        ),
        migrations.AlterField(
            model_name='loan',
            name='term',
            field=models.DecimalField(decimal_places=0, help_text='number of months that will take until the loan gets paid-off.', max_digits=3),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, help_text='amount of the payment made or missed in dollars.', max_digits=8),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(help_text='payment date.'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='loan_id',
            field=models.ForeignKey(help_text='unique id of the loan.', on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='loan_app.Loan'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment',
            field=models.CharField(choices=[('made', 'made'), ('missed', 'missed')], default='made', help_text='type of payment: made or missed.', max_length=6),
        ),
    ]
