baseURL = 'http://13.233.247.133:1000/'
# baseURL = 'http://127.0.0.1:5000/'
# ======================================================================= 
# STUDENT LOGIN URLS
# ======================================================================= 
Login_URL = baseURL + 'api/login/'
resetPassword_URL = baseURL + 'api/password_reset/'
updateProfile_URL = baseURL + 'api/userProfile_detail/'

sendOtp_URL = baseURL + 'api/loginviaotp/'
verifyOtp_URL = baseURL + 'api/loginviaVerifyotp/'

sendSignUpOtp_URL = baseURL + 'api/signUPviaotp/'
verifySignUpOtp_URL = baseURL + 'api/signUPviaVerifyotp/'
# ======================================================================= 
customerRegistrationUrls = baseURL + 'api/register/'
getExistingCustomer_URL  = baseURL + 'api/check_existing_data'
# ======================================================================= 
# Category DATA URLs
# ======================================================================= 
createCategory_URL = baseURL + 'api/productCategory_list/'
getCategoryList_URL = baseURL + 'api/productCategory_list/'
specificCategoryUpdate_URL = baseURL + 'api/productCategory_detail/'

# ======================================================================= 
# Product DATA URLs
# ======================================================================= 
productList_URL = baseURL + 'api/product_list_web/'
specificProduct_URL = baseURL + 'api/product_detail_web/'
relatedProduct_URL = baseURL + 'api/product_detail_related_web/'
bannerList_URL = baseURL + 'api/dashboard_list_web/'
productCategoryList_URL = baseURL + 'api/productCategory_list_web/'

productSearchFilter_URL = baseURL + 'api/filterproduct_web/'
# ======================================================================= 
## ENQUIRY DATA URLs
# ======================================================================= 
createProductEnquiry_URL = baseURL + 'api/enquiryformdata_list_web/'
createContactEnquiry_URL = baseURL + 'api/contactUs_list_web/'
# ======================================================================= 
# ======================================================================= 
## CUSTOMER ADDRESS DATA URLs
# ======================================================================= 
addNewAddress_URL = baseURL + 'api/address_list/'
getAllAddressByUser_URL = baseURL + 'api/getAllAddressByUser/'
userOrderList_URL = baseURL + 'api/enquiry_status/'
updateAddress_URL = baseURL + 'api/address_detail/'
# ======================================================================= 
addTocart_list_URL = baseURL + 'api/addTocart_list/'
cartDetail_URL  = baseURL + 'api/addTocartUser_list/'
delete_cart_item_URL  = baseURL + 'api/addTocart_detail/'
check_cart_item_URL  = baseURL + 'api/checkCurrentlyAddOrNot/'
check_wish_item_URL  = baseURL + 'api/checkCurrentlyAddOrNotproduct/'

removeCartItem_URL = baseURL + 'api/checkAdd_cart/'
updateCart_URL =  baseURL + 'api/addTocart_detail/'
addToWish_list_URL = baseURL + 'api/addToWishlist_list/'
Wishlist_list_URL = baseURL + 'api/addToWishlist_detail/'
deleteWishlistProduct_URL = baseURL + 'api/addToWishlist_detail/'
moveToCart_URL = baseURL + 'api/movetocart/'


