var otpArray = [];
// ======================================================================================================================================================
// ======================================================================================================================================================
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
// ======================================================================================================================================================
// ======================================================================================================================================================
function sendOTP(){
    $('#loginOTPfield').css('opacity',0.2);
    $('#loginOTPfield').css('pointer-events','none');
    $('#resendOTPsection').css('opacity',0.2);
    $('#resendOTPsection').css('pointer-events','none');

    var mobileNumber = $('#otpContact').val().trim();
    console.log('OTO',mobileNumber)
    if(mobileNumber.length != 10){
        alert('Enter a valid 10 digit mobile number!');
        return false;
    }
    // ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/send_OTP",
        headers: { 'X-CSRFToken': csrftoken },
        data: {'mobileNumber': mobileNumber},
        success: function (response) {
            console.log(response['filteredData']);
            if(response['filteredData']['message'] == 'user verified'){
                otpArray.push(response['filteredData']['mobileVerificationOTP']);
                $('#otpContact').attr('readonly',true);
                $('#sendOTPbtnn').css('display','none')
                $('#loginOTPfield').css('opacity',1);
                $('#loginOTPfield').css('pointer-events','');
                $('#resendOTPsection').css('opacity',1);
                $('#resendOTPsection').css('pointer-events','');
                $('#sendOTPbtnn').attr('disabled',true);
                $('#sendOTPbtnn').css('cursor','not-allowed');

                $('#otpTimerDiv').css('display','');

                var fiveMinutes = 60 * 2,
                display = document.querySelector('#otpTimer');
                startTimer(fiveMinutes, display);

            }else{
                alert('Invalid User!');
                $('#otpTimerDiv').css('display','none');
                return false;
            }
        }
    });
// -------------------------------------------------------- 
}
// ======================================================================================================================================================
// ======================================================================================================================================================
function verifyOtpAuto(){
    var otp1 = $('#otp1').val().trim();
    var otp2 = $('#otp2').val().trim();
    var otp3 = $('#otp3').val().trim();
    var otp4 = $('#otp4').val().trim();


    if(otp1.length == 0){
        alert('Enter valid OTP!');
        return false;
    }if(otp2.length == 0){
        alert('Enter valid OTP!');
        return false;
    }if(otp3.length == 0){
        alert('Enter valid OTP!');
        return false;
    }if(otp4.length == 0){
        alert('Enter valid OTP!');
        return false;
    }

    otp = otp1+otp2+otp3+otp4;
    console.log('otp >> ',otp,'tfdtfdt',otp.length,'555',$('#otpContact').val().trim(),$('#otpContact').val().trim().length);
    console.log('mobile number >>> ',$('#otpContact').val().trim());
    // ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/verifyOTP",
        headers: { 'X-CSRFToken': csrftoken },
        data: {mobileNumber : $('#otpContact').val().trim(),'otp': otp},
        success: function (response) {
            console.log(response['responseData']);
            if(response['responseData']['message'] == 'success'){
                window.location.href = '/';
            }else{
                alert(response['responseData']['message']);
                $('#otp1').val('');
                $('#otp2').val('');
                $('#otp3').val('');
                $('#otp4').val('');

                $('#otp1').focus().select()

                return false;
            }
        }
    });
// -------------------------------------------------------- 
}
// ======================================================================================================================================================
// ======================================================================================================================================================
function resendOTP(){
    $('#loginOTPfield').css('opacity',0.2);
    $('#loginOTPfield').css('pointer-events','none');
    $('#resendOTPsection').css('opacity',0.2);
    $('#resendOTPsection').css('pointer-events','none');

    var mobileNumber = $('#otpContact').val().trim();

    if(mobileNumber.length != 10){
        alert('Enter a valid 10 digit mobile number!');
        return false;
    }
    $('#otpTimerDiv').css('display','');

    var fiveMinutes = 60 * 2,
    display = document.querySelector('#otpTimer');
    startTimer(fiveMinutes, display);

    $('#otp1').val('');
    $('#otp2').val('');
    $('#otp3').val('');
    $('#otp4').val('');
    // ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/send_OTP",
        headers: { 'X-CSRFToken': csrftoken },
        data: {'mobileNumber': mobileNumber},
        success: function (response) {
            console.log(response['filteredData']);
            if(response['filteredData']['message'] == 'user verified'){
                $('#otpContact').attr('readonly',true);
                $('#sendOTPbtnn1').css('display','none')
                otpArray.push(response['filteredData']['mobileVerificationOTP']);
                $('#loginOTPfield').css('opacity',1);
                $('#loginOTPfield').css('pointer-events','');
                $('#resendOTPsection').css('opacity',1);
                $('#resendOTPsection').css('pointer-events','');
                $('#sendOTPbtnn').attr('disabled',true);
                $('#sendOTPbtnn').css('cursor','not-allowed');

            }else{
                alert('Invalid User!');
                return false;
            }
        }
    });
// -------------------------------------------------------- 
}
// ======================================================================================================================================================
// ======================================================================================================================================================
function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;
        // console.log('duration >>> ',minutes + ":" + seconds);

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);
}

// ======================================================================================================================================================
// ======================================================================================================================================================
function sendSignupOTP(){
    $('#signupOTPfield').css('opacity',0.2);
    $('#signupOTPfield').css('pointer-events','none');
    $('#resendSignupOTPsection').css('opacity',0.2);
    $('#resendSignupOTPsection').css('pointer-events','none');

    var mobileNumber = $('#otpSignupContact').val().trim();
    console.log('OTO',mobileNumber)
    if(mobileNumber.length != 10){
        alert('Enter a valid 10 digit mobile number!');
        return false;
    }
    // ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/send_signup_OTP",
        headers: { 'X-CSRFToken': csrftoken },
        data: {'mobileNumber': mobileNumber},
        success: function (response) {
            console.log(response['filteredData']);
            if(response['filteredData']['message'] == 'user verified'){
                $('#otpSignupContact').attr('readonly',true);
                $('#sendOTPbtnn1').css('display','none');
                otpArray.push(response['filteredData']['mobileVerificationOTP']);
                $('#signupOTPfield').css('opacity',1);
                $('#signupOTPfield').css('pointer-events','');
                $('#resendSignupOTPsection').css('opacity',1);
                $('#resendSignupOTPsection').css('pointer-events','');
                $('#sendOTPbtnn').attr('disabled',true);
                $('#sendOTPbtnn').css('cursor','not-allowed');

                $('#otpsignupTimerDiv').css('display','');
                $('#otpSignupTimerDiv').css('display','');


                var fiveMinutes = 60 * 2,
                display = document.querySelector('#otpSignupTimer');
                startTimer(fiveMinutes, display);

            }else{
                alert('Invalid User!');
                $('#otpsignupTimerDiv').css('display','none');
                return false;
            }
        }
    });
// -------------------------------------------------------- 

}
// ======================================================================================================================================================
// ======================================================================================================================================================
function resendSignupOTP(){
    $('#signupOTPfield').css('opacity',0.2);
    $('#signupOTPfield').css('pointer-events','none');
    $('#resendSignupOTPsection').css('opacity',0.2);
    $('#resendSignupOTPsection').css('pointer-events','none');

    var mobileNumber = $('#otpSignupContact').val().trim();

    // if(mobileNumber.length != 10){
    //     alert('Enter a valid 10 digit mobile number!');
    //     return false;
    // }
    $('#otpSignupTimerDiv').css('display','');

    $('#signup_otp1').val('');
    $('#signup_otp2').val('');
    $('#signup_otp3').val('');
    $('#signup_otp4').val('');
    // ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/send_signup_OTP",
        headers: { 'X-CSRFToken': csrftoken },
        data: {'mobileNumber': mobileNumber},
        success: function (response) {
            console.log(response['filteredData']);
            if(response['filteredData']['message'] == 'user verified'){
                $('#otpSignupContact').attr('readonly',true);
                $('#sendOTPbtnn1').css('display','none');
                otpArray.push(response['filteredData']['mobileVerificationOTP']);
                $('#signupOTPfield').css('opacity',1);
                $('#signupOTPfield').css('pointer-events','');
                $('#resendSignupOTPsection').css('opacity',1);
                $('#resendSignupOTPsection').css('pointer-events','');
                $('#sendOTPbtnn').attr('disabled',true);
                $('#sendOTPbtnn').css('cursor','not-allowed');

                $('#otpsignupTimerDiv').css('display','');

                var fiveMinutes = 60 * 2,
                display = document.querySelector('#otpSignupTimer');
                startTimer(fiveMinutes, display);

            }else{
                alert('Invalid User!');
                $('#otpsignupTimerDiv').css('display','none');
                return false;
            }
        }
    });
// -------------------------------------------------------- 
}
// ======================================================================================================================================================
// ======================================================================================================================================================
function verifySighUpOtpAuto(){
    var otp1 = $('#signup_otp1').val().trim();
    var otp2 = $('#signup_otp2').val().trim();
    var otp3 = $('#signup_otp3').val().trim();
    var otp4 = $('#signup_otp4').val().trim();


    if(otp1.length == 0){
        alert('Enter valid OTP!');
        return false;
    }if(otp2.length == 0){
        alert('Enter valid OTP!');
        return false;
    }if(otp3.length == 0){
        alert('Enter valid OTP!');
        return false;
    }if(otp4.length == 0){
        alert('Enter valid OTP!');
        return false;
    }

    otp = otp1+otp2+otp3+otp4;
    console.log('otp >> ',otp,'tfdtfdt',otp.length,'555',$('#otpContact').val().trim(),$('#otpContact').val().trim().length);
    console.log('mobile number >>> ',$('#otpContact').val().trim());
    // ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/verifySignUpOTP",
        headers: { 'X-CSRFToken': csrftoken },
        data: {mobileNumber : $('#otpSignupContact').val().trim(),'otp': otp},
        success: function (response) {
            console.log(response['responseData']);
            // return false;
            if(response['responseData']['message'] == 'success'){
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: '<small>Your Mobile has been verified</small>',
                    showConfirmButton: false,
                    timer: 1500
                  })
                // otpArray.push(response['filteredData']['mobileVerificationOTP']);
                $('#loginOTPfield').css('opacity',1);
                $('#loginOTPfield').css('pointer-events','');
                $('#resendOTPsection').css('opacity',1);
                $('#resendOTPsection').css('pointer-events','');
                $('#sendOTPbtnn').attr('disabled',true);
                $('#sendOTPbtnn').css('cursor','not-allowed');

                // $('#otpTimerDiv').css('display','');

                // var fiveMinutes = 60 * 2,
                // display = document.querySelector('#otpTimer');
                // startTimer(fiveMinutes, display);
                $('#signin_section_container').css('display','none');
                $('#signin_section_container1').css('display','');
                $('#registerContact').val($('#otpSignupContact').val().trim());

            }
            else{
                $('#otpTimerDiv').css('display','none');
                $('#signin_section_container').css('display','');
                $('#signin_section_container1').css('display','none');
                alert(response['responseData']['message']);
                $('#otpSignupTimerDiv').css('display','');
                $('#registerContact').val();


                $('#signup_otp1').val('');
                $('#signup_otp2').val('');
                $('#signup_otp3').val('');
                $('#signup_otp4').val('');

                $('#signup_otp1').focus().select()

                return false;
            }
        }
    });
// -------------------------------------------------------- 
}
// ======================================================================================================================================================
// ======================================================================================================================================================
