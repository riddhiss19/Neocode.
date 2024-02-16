jQuery(document).ready(function()
{
	 "use strict"

	 $(".slider").ripples({      
	  dropRadius:12 ,
	  perturbance: 0.01,
	  
	});


	$('.work').magnificPopup({
	  delegate: 'a', 
	  type: 'image',
	  gallery:{ enabled:true}
	  // other options
	});

	$('.owl-carousel').owlCarousel();

//   Email notification



	


});