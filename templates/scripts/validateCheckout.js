// 
//	jQuery Validate example script
//
//	Prepared by David Cochran
//	
//	Free for your use -- No warranties, no guarantees!
//

$(document).ready(function(){

	// Validate
	// http://bassistance.de/jquery-plugins/jquery-plugin-validation/
	// http://docs.jquery.com/Plugins/Validation/
	// http://docs.jquery.com/Plugins/Validation/validate#toptions
	
		$('#checkout_form').validate({
	    rules: {
	      phone: {
	      	required: true,
	        minlength: 2,
	        number: true
	      },
	      email: {
	        required: true,
	        email: true
	      },
	      shipping_name: {
	      	minlength: 1,
	        required: true
	      },
	      shipping_address_1: {
	        required: true
	      }
	    },
	    highlight: function(label) {
	    	$(label).closest('.accordion-heading').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.accordion-heading').addClass('success');
	    }
	  });
	  
}); // end document.ready