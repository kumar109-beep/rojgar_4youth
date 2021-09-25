from .enquiryFormModels import *
from .userProfileModels import *
from django.contrib.auth.models import User
from .orderDetail import *


EnquiryForm._meta.get_field("contactNo")._unique = True
UserProfile._meta.get_field("mobileNO")._unique = True
User._meta.get_field("email")._unique = True
UserProfile._meta.get_field("mobileNO")._unique = True
OrderDetail._meta.get_field("orderID")._unique = True