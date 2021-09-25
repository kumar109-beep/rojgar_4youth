// -----------------------------------------------------------------------------------------------------------
// ==========================   FUNCTIONs FOR ENQUIRY FORM VALIDATION    =====================================
// -----------------------------------------------------------------------------------------------------------
function checkEmail() {
    var emailData = $('#custEmail').val();
    
    var mailformat = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (emailData.match(mailformat)) {
        $('#custEmail').css('color', 'green');
        $('#custEmail').css('border', '');
        $('#enquiryButton').attr('disabled', false);
    }else if(emailData.length == 0){
        $('#custEmail').css('border', '');
        $('#enquiryButton').attr('disabled', false);
    }
    else {
        $('#custEmail').css('color', 'red');
        $('#custEmail').css('border', '1px solid red');
        $('#enquiryButton').attr('disabled', true);
    }
}
// -----------------------------------------------------------------------------------------------------------
// ==========================   FUNCTIONs FOR ENQUIRY FORM SUBMISSION    =====================================
// -----------------------------------------------------------------------------------------------------------
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

function send_enquiry(thisTxt){
    var productID = $(thisTxt).attr('productID')
    // console.log(productID);

    var customerName = $('#customerName').val().trim();
    var customerContact= $('#customerContact').val().trim();

    var customerEmail = $('#custEmail').val().trim();
    var customerRemark = $('#customerRemark').val().trim();


    var customerAddress = $('#customerAddress').val().trim();

    var custCity = $('#custCity').val().trim();
    var custState = $('#custState').val().trim();
    if(customerName.length == 0){
        alert('Enter Customer Name');
        return false;
    }
    if(customerContact.length == 0 ){
        alert('Enter Customer Contact');
        return false;
    }
    if(customerContact.length != 10 ){
        alert('Enter valid 10 digit Customer Contact');
        return false;
    }
    if(custState.length == 0){
        alert('Select Customer State');
        return false;
    }
    if(custCity.length == 0){
        alert('Select Customer City');
        return false;
    }
    if(customerAddress.length == 0){
        alert('Select Customer Address');
        return false;
    }
    // 'customerAddress': customerAddress,
    else{
        $('#enquiryButton').css('display','none');
        $('#spinnerbtn').css('display','');
        // ---------------   AJAX Call   ---------------------
        const csrftoken = getCookie('csrftoken');
        // swal.showLoading();
        $.ajax({
            type: 'POST',
            url: "/create_enquiry",
            headers: { 'X-CSRFToken': csrftoken },
            data: {
                'customerName': customerName, 'customerContact': customerContact, 
                'customerEmail': customerEmail, 'customerRemark': customerRemark,
                'productID': productID, 'customerAddress': customerAddress,
                'custCity': custCity,'custState': custState
            },
            success: function (response) {
                console.log(response);
                // window.location.href = "/batch_list";
                $('#enquiryButton').css('display','');
                $('#spinnerbtn').css('display','none');
                if(response == 'Success'){
                    alert('Your enquiry send successfully to our team.They will reach you in some time.');
                    location.reload();
                }else{
                    alert('Your enquiry failed.Try Again!');
                    return false;
                }
            }
        });

        // ---------------------------------------------------
    }

}
// -----------------------------------------------------------------------------------------------------------
// ===========================================================================================================
function CheckContactUsEmail(){
    var emailData = $('#cusEmail').val();
    var mailformat = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (emailData.match(mailformat)) {
        $('#cusEmail').css('color', 'green');
        $('#cusEmail').css('border', '');
        $('#submitBtn').attr('disabled', false);
    }else if(emailData.length == 0){
        $('#cusEmail').css('border', '');
        $('#submitBtn').attr('disabled', false);
    }
    else {
        $('#cusEmail').css('color', 'red');
        $('#cusEmail').css('border', '1px solid red');
        $('#submitBtn').attr('disabled', true);
    }
}


function contactUs(thisTxt){

    var customerName = $('#customerName').val().trim();
    var customerEmail = $('#cusEmail').val().trim();
    var Subject= $('#subjectName').val().trim();
    var review = $('#customerReview').val().trim();

    if(customerName.length == 0){
        alert('Enter Customer Name');
        return false;
    }
    if(customerEmail.length == 0){
        alert('Enter Customer Email');
        return false;
    }
    if(Subject.length == 0){
        alert('Enter Subject');
        return false;
    }
    else{
        $('#submitBtn').css('display','none');
        $('#spinnerbtn').css('display','');
        // ---------------   AJAX Call   ---------------------
        const csrftoken = getCookie('csrftoken');
        // swal.showLoading();
        $.ajax({
            type: 'POST',
            url: "/contact",
            headers: { 'X-CSRFToken': csrftoken },
            data: {
                'customerName': customerName, 'customerEmail': customerEmail, 'Subject': Subject,
                'review': review
            },
            success: function (response) {
                console.log(response);
                // window.location.href = "/batch_list";
                $('#submitBtn').css('display','');
                $('#spinnerbtn').css('display','none');
                if(response == 'Success'){
                    alert('Your enquiry send successfully to our team.They will reach you in some time.');
                    location.reload();
                }else{
                    alert('Your enquiry failed.Try Again!');
                    return false;
                }
            }
        });

        // ---------------------------------------------------
    }

}
// -----------------------------------------------------------------------------------------------------------
// ===========================================================================================================