from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


from phone_field import PhoneField

from .utils import CITIES, state_choices

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    mobile_number = PhoneField(blank=False, help_text='Contact phone number')
    alternate_contact_number = PhoneField(blank=True, help_text='Alternate contact number')
    address = models.CharField(max_length=100, default='')
    adhar_number = models.CharField(max_length=50, default=None)
    state = models.CharField(choices=state_choices, null=False, max_length=100)
    city = models.CharField(choices=CITIES, null=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + str(self.mobile_number.base_number)



class BhaktamberCategories(models.Model):
    id = models.AutoField(primary_key=True)
    reason = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reason


class DonationCategories(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100, blank=False) #eg: shantidhara, abhishek, bhaktamber, Gooshala, Nirvan, Other
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BhaktamberUser(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BhaktamberCategories, on_delete=models.CASCADE)
    bhaktamber_date = models.DateField(default=None)
    special_reason = models.CharField(max_length=100, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id.name + str(self.bhaktamber_date)

    def applicant_name(self):
        return self.user_id.name
    applicant_name.short_description = 'Applicant Name'

    def applicant_mobile_number(self):
        return self.user_id.mobile_number.base_number
    applicant_mobile_number.short_description = 'Applicant Mobile Name'


# Create your models here.
class UserDonation(models.Model):
    """
	"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format:"
                                                                   " '+919993158005'. Up to 12 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=100, default='', blank=True)

    address = models.CharField(max_length=100, default='')
    adhar_number = models.CharField(max_length=50, default=None)
    state = models.CharField(choices=state_choices, null=False, max_length=100)
    city = models.CharField(choices=CITIES, null=False, max_length=100)

    adhar_number = models.CharField(max_length=50, default=None)

    amount_regex = RegexValidator(regex=r'^[1-9][0-9]*$', message="Donation amount should be 1 or > 1 Rs'.")
    donation_amount = models.IntegerField(validators=[amount_regex], default=None, blank=False)
    donation_date = models.DateField(default=now)
    donation_deposit_date = models.DateField(default=None, null=True, blank=True)
    donation_status = models.BooleanField(default=False, help_text='Donation amount deposited or not')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        pass
        # if self.donation_date > self.donation_deposit_date:
        #     raise ValidationError("Dates are incorrect")

        # if self.donation_amount <= 0:
        #     raise ValidationError("Donation amount should be 1 or > 1 Rs")

    def __str__(self):
        return self.mobile_number
