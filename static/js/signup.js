$(function(){
	//adminlist();
	$('#user_button_register').click(function(){

		var name = $("#user_first_name"); //done

		var name_span = $("#user_first_name_span");



		name.blur(validate_name);

		name.keyup(validate_name);

		if(validate_name()){
			$.ajax({
				url: '/addusertyps',
				data: $('#form_signin_add').serialize(),
				type: 'POST',
				//contentType: 'application/json',
				success: function(response){
					//if(response.status == 'OK'){
						//$("#form_signin")
						usertypselist();
						$('#form_signin_add')[0].reset();
						if($("#form_signin_input").val() == 'update'){
							$( "#usermsgpage" ).html('User Type Updated successfully!');
						}else{
							$( "#usermsgpage" ).html('User Type inserted successfully!');
						}

						//setTimeout($( "#button_Close" ).trigger( "click" ), 11000);
						//$('#sticky-form-box').model('hide');
						//$('#sticky-form-box').dialog('close');

					//}

				},
				error: function(error){
					console.log(error);
				}
			});
		}

		function validate_name(){
			if($("#user_first_name").val() == ''){
				name_span.text("This field is required.");
				name_span.addClass("message_error2");
				return false;
			}else{
				name_span.text("");
				name_span.removeClass("message_error2");
				return true;
			}
		}

	});

	$('#button_register').click(function(){
		//var user = $('#inputUsername').val();
		//var pass = $('#inputPassword').val();
		var firstName = $("#input_first_name"); //done
		var lastName = $("#input_last_name");
		var phone =$("#input_phone");
		var username = $("#inputUsername");
		var password = $("#inputPassword");
		var usertype = $("#inputuser_type");

		var firstName_span = $("#input_first_name_span");
		var lastName_span = $("#input_last_name_span");
		var phone_span = $("#input_phone_span");
		var username_span = $("#inputUsername_span");
		var password_span = $("#inputPassword_span");
		var usertype_span = $("#inputuser_type_span");

		firstName.blur(validate_FirstName);
		lastName.blur(validate_lastName);
		phone.blur(validate_phone);
		username.blur(validate_username);
		password.blur(validate_password);
		usertype.blur(validate_usertype);

		firstName.keyup(validate_FirstName);
		lastName.keyup(validate_lastName);
		phone.keyup(validate_phone);
		username.keyup(validate_username);
		password.keyup(validate_password);
		usertype.keyup(validate_usertype);
		if(validate_FirstName() & validate_lastName() & validate_phone() & validate_username() & validate_password() & validate_usertype()){
			$.ajax({
				url: '/signUpUser',
				data: $('#form_signin').serialize(),
				type: 'POST',
				//contentType: 'application/json',
				success: function(response){
					//if(response.status == 'OK'){
						//$("#form_signin")
						adminlist();
						$('#form_signin')[0].reset();
						$( "#msgpage" ).html('Recode added successfully');
						setTimeout($( "#button_Close" ).trigger( "click" ), 11000);
						//$('#sticky-form-box').model('hide');
						//$('#sticky-form-box').dialog('close');

					//}

				},
				error: function(error){
					console.log(error);
				}
			});
		}


		function validate_FirstName(){
			if($("#input_first_name").val() == ''){
				firstName_span.text("This field is required.");
				firstName_span.addClass("message_error2");
				return false;
			}else{
				firstName_span.text("");
				firstName_span.removeClass("message_error2");
				return true;
			}
		}

		function validate_lastName(){
			if($("#input_last_name").val() == ''){
				lastName_span.text("This field is required.");
				lastName_span.addClass("message_error2");
				return false;
			}else{
				lastName_span.text("");
				lastName_span.removeClass("message_error2");
				return true;
			}
		}

		function validate_phone(){
			if($("#input_phone").val() == ''){
				phone_span.text("This field is required.");
				phone_span.addClass("message_error2");
				return false;
			}else{
				phone_span.text("");
				phone_span.removeClass("message_error2");
				return true;
			}
		}

		function validate_username(){

			if($("#inputUsername").val() == ''){
				//isvalidemailflag = 1;
				username_span.text("This field is required.");
				username_span.addClass("message_error2");
				return false;
			}else if($("#inputUsername").val() != ''){
				var a = $("#inputUsername").val();
				var filter = /^[_a-z_A-Z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$/;
				//if it's valid email
				if(filter.test(a)){
					isvalidemailflag = 0;
				}else{
					isvalidemailflag = 1;
				}
			}

			if(isvalidemailflag)
			{
				username_span.text("Enter valid email address.");
				username_span.addClass("message_error2");
				return false;
			}
			else{
				username_span.text("");
				username_span.removeClass("message_error2");
				return true;
			}
		}

		function validate_password(){
			if($("#inputPassword").val() == ''){
				password_span.text("This field is required.");
				password_span.addClass("message_error2");
				return false;
			}else{
				password_span.text("");
				password_span.removeClass("message_error2");
				return true;
			}
		}

		function validate_usertype(){
			if($("#inputuser_type").val() == ''){
				usertype_span.text("This field is required.");
				usertype_span.addClass("message_error2");
				return false;
			}else{
				usertype_span.text("");
				usertype_span.removeClass("message_error2");
				return true;
			}
		}


	});
});

 $(document).ready(function () {
  			adminlist();

        });
	 function adminlist(){
	 	$("#display_example").dataTable().fnDestroy();
	 	var table =  $('#display_example').DataTable({
                "info": true,
                /* Set pagination as false or
                true as per need */
                "paging": true,

                /* Name of the file source
                for data retrieval */
                "ajax": '/adminlist',
                "columns": [
                    /* Name of the keys from
                    data file source */
                    { data: 'id' },
                    { data: 'first' },
					{ data: 'last_name' },
					{ data: 'phone' },
					{ data: 'email' },
					{ data: null, "defaultContent":"<button>Edit</button>" },

                ]
            });
	 	 $('#display_example tbody').on('click', 'button', function () {
	        var data = table.row($(this).parents('tr')).data();
	        console.log(data.id);
	        $("#input_first_name").val(data.first); //done
			$("#input_last_name").val(data.last_name);
			$("#input_phone").val(data.phone);
			$("#inputUsername").val(data.email);
			$("#inputPassword").val(data.password);
			$("#inputuser_type").val(data.user_type);
			$("#signin_input").val(data.id);
	        $("#signininput").val('update');
			adduser()
	        return false;
	        //alert(data[0] + "'s salary is: " + data[1]);
	    });
	 }


function adduser(){
	$( "#msgpage" ).html('');
	 $('#sticky-form-box').bPopup();
}

function usertype(){
	usertypselist();
	$( "#usermsgpage" ).html('');
	 $('#sticky_adduser_type').bPopup();
}
let  table;
function usertypselist(){
		$("#form_signin_input").val('add');
	 	$("#user_display_example").dataTable().fnDestroy();
	 	 table = $('#user_display_example').DataTable({
                "info": false,
                /* Set pagination as false or
                true as per need */
                "paging": false,

                "searching":false,

                /* Name of the file source
                for data retrieval */
                "ajax": '/userlist',
                "columns": [
                    /* Name of the keys from
                    data file source */
                    { data: 'id' },
                    { data: 'name' },
                    { data: null, "defaultContent":"<button>Edit</button>" },


                ],

            });

	 	 $('#user_display_example tbody').on('click', 'button', function () {
	        var data = table.row($(this).parents('tr')).data();
	        console.log(data.id);
	        $("#user_first_name").val(data.name);
	        $("#formsignininput").val(data.id);
	        $("#form_signin_input").val('update');
	        usertypselist();
	        return false;
	        //alert(data[0] + "'s salary is: " + data[1]);
	    });
	 }
                                                   