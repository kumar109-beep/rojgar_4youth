function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// =====================    ADD NEW ADDRESS TO CUSTOMER ADDRESS BOOK    ====================================
// =========================================================================================================
function addNewAddress(){
    var fullname = $('#customerfullname').val();
    var contact = $('#customerNewcontact').val();
    var district = $('#customerNewDistrict').val();


    var address = $('#customerNewAddress').val();
    var pincode = $('#customerNewPincode').val();
    var location = $('#customerNewLocation').val();
    var state = $('#customerNewState').val();

    if(fullname.trim().length == 0){
        alert('Enter customer name');
        return false;
    }if(contact.trim().length < 10){
        alert('Enter valid 10 digit contact number');
        return false;
    }
    if(pincode.trim().length < 6){
        alert('Enter valid pincode');
        return false;
    }
    if(location.trim().length == 0){
        alert('Enter valid landmark');
        return false;
    }
    if(district.trim().length == 0){
        alert('Enter valid district');
        return false;
    }
    if(state.trim().length == 0){
        alert('Select valid state');
        return false;
    }
    if(address.trim().length == 0){
        alert('Enter valid address');
        return false;
    }
    
    console.log('fullname >>> ',fullname);
    console.log('contact >>> ',contact);
    console.log('pincode >>> ',pincode);
    console.log('location >>> ',location);
    console.log('district >>> ',district);
    console.log('state >>> ',state);
    console.log('address >>> ',address);

    // ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/customer-management/customer-address",
        headers: { 'X-CSRFToken': csrftoken },
        data: {'fullname': fullname, 'contact': contact, 'pincode': pincode,'location': location,'district': district,'state': state,'address': address},
        success: function (response) {
            console.log(response['responseData']);
            // $('#enquiryButton').css('display','');
            // $('#spinnerbtn').css('display','none');
            if(response['responseData']['message'] == 'success'){
                alert('New Address Added successfully');
                // location.reload();
                // $('#exampleModalCenter').modal('hide');
                window.location.reload()
            }else{
                alert('An Error Occured.Try Again!');
                return false;
            }
        }
    });
    // --------------------------------------------------------
}
// =========================================================================================================




function updateAddress(thisTxt){
        
    var id = $(thisTxt).attr('id');
    // =================================================
        var fullname = $('#fullname_'+id).val().trim();
        var contact = $('#contact_'+id).val().trim();
        var district = $('#district_'+id).val().trim();

        var address = $('#address_'+id).val().trim();
        var landmark = $('#landmark_'+id).val().trim();
        var state = $('#state_'+id).val().trim();
        var pincode = $('#pincode_'+id).val().trim();


        if(fullname.trim().length == 0){
            alert('Enter customer name');
            return false;
        }if(contact.trim().length < 10){
            alert('Enter valid 10 digit contact number');
            return false;
        }
        if(address.trim().length == 0){
        alert('Enter valid address');
        return false;
        }if(landmark.trim().length == 0){
            alert('Enter valid landmark');
            return false;
        }if(state.trim().length == 0){
            alert('Enter valid state');
            return false;
        }if(pincode.trim().length == 0){
            alert('Enter valid pincode');
            return false;
        }if(district.trim().length == 0){
        alert('Enter valid district');
        return false;
    }

    console.log('fullname >>> ',fullname);
    console.log('contact >>> ',contact);
    console.log('pincode >>> ',pincode);
    console.log('location >>> ',location);
    console.log('district >>> ',district);
    console.log('state >>> ',state);
    console.log('address >>> ',address);
// ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/update_address",
        headers: { 'X-CSRFToken': csrftoken },
        data: {'fullname': fullname,'contact': contact,'district': district,'address': address, 'landmark': landmark, 'state': state,'pincode': pincode,'id':id},
        success: function (response) {
            console.log(response['responseData']);
            // $('#enquiryButton').css('display','');
            // $('#spinnerbtn').css('display','none');
            if(response['responseData']['message'] == 'success'){
                alert('Address Updated Successfully');
                // location.reload();
                // $('#exampleModalCenter').modal('hide');
                window.location.reload()
            }else{
                alert('An Error Occured.Try Again!');
                return false;
            }
        }
    });
// --------------------------------------------------------        
// =================================================
}