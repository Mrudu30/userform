$(document).ready(function(){
    // call function id's
    var adduserform = $("#adduserform")
    var fname = $("#fname")
    var lname = $("#lname")
    var email = $("#email")
    var mobile_number = $("#mobile_number")
    var address = $("#address")

    // call span ids
    var fname_span = $("#fname_span")
    var lname_span = $("#lname_span")
    var email_span = $("#email_span")
    var mobile_number_span = $("#mobile_number_span")
    var address_span = $("#address_span")

    // on blur events
    fname.blur(validate_fname)
    lname.blur(validate_lname)
    email.blur(validate_email)
    mobile_number.blur(validate_mobile_number)
    address.blur(validate_address)

    // on key up events
    fname.keyup(validate_fname)
    lname.keyup(validate_lname)
    email.keyup(validate_email)
    mobile_number.keyup(validate_mobile_number)
    address.keyup(validate_address)

    // Validation functions
    function validate_fname(){
		if(jQuery("#fname").val() == '')
		{
            console.log('fname false')
			fname_span.text("This field is required.");
			return false;
		}
		else{
			fname_span.text("");
			return true;
		}
	}

    function validate_lname(){
		if(jQuery("#lname").val() == '')
		{
            console.log('lname false')
			lname_span.text("This field is required.");
			return false;
		}
		else{
			lname_span.text("");
			return true;
		}
	}

    function validate_email(){
        var email_ch = jQuery('#email').val()
		if(email_ch.trim === '')
		{
            console.log('email if false')
			email_span.text("This field is required.");
			return false;
		}
		else{
            // re to check email validation
			var pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
            if (pattern.test(email_ch)){
                email_span.text("")
                return true
            }
            else{
                console.log('email false')
                email_span.text("Please Enter Valid Email")
                return false
            }
		}
	}

    function validate_mobile_number(){
		var mobileNumber = jQuery("#mobile_number").val();

        if (mobileNumber.trim() === '') {
            console.log('mob trim false')
            mobile_number_span.text("This field is required.");
            return false;
        } else {
            // Check if the mobile number has exactly 10 characters
            if (mobileNumber.length === 10 && !isNaN(mobileNumber)) {
                mobile_number_span.text("");
                return true;
            } else {
                console.log('mob false')
                mobile_number_span.text("Mobile number should be exactly 10 numeric characters.");
                return false;
            }
        }
	}

    function validate_address(){
		if(jQuery("#address").val() == '')
		{
            console.log('add false')
			address_span.text("This field is required.");
			return false;
		}
		else{
			address_span.text("");
			return true;
		}
	}

    //  Onsubmit final validation check
    adduserform.submit(
        function(){
            if (validate_fname() & validate_mobile_number() & validate_address() & validate_lname() & validate_email()){
                console.log('all conditions true')
                return true
            }
            else{
                console.log('all conditions false')
                return false
            }
        }
    )
})