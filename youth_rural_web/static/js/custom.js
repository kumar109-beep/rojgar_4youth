$('.home-slider').owlCarousel({
    loop:false,
    margin:0,
    responsiveClass:true,
    nav:false,
    autoplay:true,
    autoplayTimeout:5000,

    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:1,
            nav:false
        },
        1000:{
            items:1 
            
        }
    }
});

 // mobile menu

 $('.toggle-menu').click(function(){
    $('header .sidebar-menu').addClass('show');
    $('.ovrlay').fadeIn();
 });
  $('header .sidebar-menu .closee').click(function(){
    $('header .sidebar-menu').removeClass('show');
    $('.ovrlay').fadeOut();
 })

  // product detail carausel

   $('.product-carausel').owlCarousel({
    loop:false,
    margin:10,
    responsiveClass:true,
    nav:true,
    dots:false,
    autoplay:false,

    responsive:{
        0:{
            items:4,
             
        },
        600:{
            items:4,
            
        },
        1000:{
            items:4 
            
        }
    }
});