// 
//	jQuery Validate example script
//
//	Prepared by David Cochran
//	
//	Free for your use -- No warranties, no guarantees!
//

$(document).ready(function(){
		 $('.shop_cart').validate({
	    rules: {
	      quantity: {
	      	required: false,
	      	min:1,
	        minlength: 1,
	        number: true
	      }
	    },
	    highlight: function(label) {
	    	$(label).closest('.accordion-heading').addClass('error');
	    }
	  });
}); // end document.ready