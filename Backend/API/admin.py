from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserDevice)
admin.site.register(SessionReport)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ColorOptions)
admin.site.register(PhoneTypeOptions)
admin.site.register(SizeOptions)

# class UserAdmin(admin.ModelAdmin):
#     fields = [
#         "apartment",
#         "flat",
#         "phonenumber",
#         "expoToken",
#         "isPrimary",
#         "otp",
#         "isGuard",
#         "loggedOut",
#     ]


# admin.site.register(User, UserAdmin)

# admin.site.register(VisitPurpose)
# admin.site.register(Visitor)
# admin.site.register(Amenity)
# admin.site.register(LoginReport)
# admin.site.register(Notice)