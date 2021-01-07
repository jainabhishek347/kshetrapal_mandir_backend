# Register your models here.
from django.contrib import admin
from .models import UserDonation, BhaktamberCategories, BhaktamberUser, User
from .utils import broadcast_sms
# Register your models here.


@admin.register(UserDonation)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "mobile_number", "donation_amount", "donation_status")
    list_filter = ("donation_status", "city")
    search_fields = ("name__startswith", "mobile_number")

    def get_fields(self, request, obj=None):
        fields = super(PersonAdmin, self).get_fields(request, obj)
        if request.user.is_superuser:
            print(fields )
            #fields += ('approve',)

        return fields

    def save_model(self, request, obj, form, change):
        name = form.cleaned_data['name']
        mobile_number = form.cleaned_data['mobile_number']
        donation_amount = form.cleaned_data['donation_amount']
        broadcast_sms(name, mobile_number, donation_amount)
        super(PersonAdmin, self).save_model(request, obj, form, change)

@admin.register(BhaktamberUser)
class BhaktamberUserAdmin(admin.ModelAdmin):
    list_display = ("applicant_name", "bhaktamber_date", "special_reason", 'applicant_mobile_number')
    list_filter = ("bhaktamber_date",)
    search_fields = ("user_id__startswith", "bhaktamber_date",)


admin.site.register(BhaktamberCategories)


admin.site.register(User)





