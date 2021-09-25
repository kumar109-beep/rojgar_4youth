from django.contrib import admin

# Register your models here.
# from .models.aboutUsModels import *
# from .models.contactUsModels import *
# from .models.dashboardModels import *
# from .models.enquiryFormModels import *
# from .models.productsListingModels import *
# from .models.userProfileModels import *
# from .models.settingModel import *
# from .models.addressUserModel import *
# from .models.addTocartModels import *
from .models.__init__ import *

@admin.register(AboutUs)
class Rojgar_AboutUs(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(ContactUs)
class Rojgar_ContactUs(admin.ModelAdmin):
    list_display = ('id',)



@admin.register(Dashboard)
class Rojgar_Dashboard(admin.ModelAdmin):
    list_display = ('id',)



@admin.register(EnquiryForm)
class Rojgar_EnquiryForm(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(EnquiryFormData)
class Rojgar_EnquiryFormData(admin.ModelAdmin):
    list_display = ('id',)


    


@admin.register(ProductsListing)
class Rojgar_ProductsListing(admin.ModelAdmin):
    list_display = ('id',)



@admin.register(ProductsCategory)
class Rojgar_ProductsCategory(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(UserProfile)
class Rojgar_UserProfile(admin.ModelAdmin):
    list_display = ('id','mobileNO',)


@admin.register(AddressListedBYUser)
class Rojgar_AddressListedBYUser(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(AddToCart)
class Rojgar_AddToCart(admin.ModelAdmin):
    list_display = ('created_at',)


@admin.register(OrderDetail)
class Rojgar_OrderDetail(admin.ModelAdmin):
    list_display = ('orderID',)

@admin.register(OtpDbModel)
class Rojgar_OtpDbModel(admin.ModelAdmin):
    list_display = ('mobNO',)