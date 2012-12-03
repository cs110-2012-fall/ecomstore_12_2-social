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
	
		$('.cart').validate({
	    rules: {
	      quantity: {
	      	required: true,
	        minlength: 2,
	        number: true
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