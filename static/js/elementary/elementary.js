

// repeated variables
var $window = $(window);
var $root = $('html, body');

$(document).ready(function () {

    "use strict";
    colorScheme();
    ColorPallet();
    PillMenuToggler();
    menuToggler();
    sliderOwlCarousel();
    typedJS();
    skills();
    countUp();
    portfolioPopup();
    clientCarousel();
    BlogCarousel();

});

$window.on("load", (function() {
    $("#overlayer").delay(500).fadeOut('slow');
    $(".loader").delay(1000).fadeOut('slow');
    portfolioIsotop();
}));

/*-------------------------
        Color Scheme
-------------------------*/
function colorScheme(){
    var $darkLogo = $('.dark-logo');
    $('.color-scheme').click(function() {
        $("body").toggleClass('arshia-dark');
        $('.color-scheme').removeClass('d-none').addClass('d-inline-block');
        $(this).removeClass('d-inline-block').addClass('d-none');
    });
}
/*-----------------------------------------------------------------------------
                                   FUNCTIONS
-----------------------------------------------------------------------------*/
$("#menu > li a").on("click" , function () {
    $("#main > section.active, #menu > li a").removeClass("active");
    $(this).addClass('active');
    var $id = $(this).attr('href');
    $('#main').children($id).addClass('active');
});

// -------------------------------------------------------------
//   Color Panel
// -------------------------------------------------------------
function ColorPallet() {

    "use strict";

    $("ul.pattern .color1").click(function () {
        return $("#option-color").attr("href", "/static/css/elementary/color/default.css")
    });
    $("ul.pattern .color2").click(function () {
        return $("#option-color").attr("href", "/static/css/elementary/color/orange-color.css")
    });
    $("ul.pattern .color3").click(function () {
        return $("#option-color").attr("href", "/static/css/elementary/color/blue-color.css")
    });
    $("ul.pattern .color4").click(function () {
        return $("#option-color").attr("href", "/static/css/elementary/color/green-color.css")
    });
    $("ul.pattern .color5").click(function () {
        return $("#option-color").attr("href", "/static/css/elementary/color/yellow-color.css")
    });
    $("ul.pattern .color6").click(function () {
        return $("#option-color").attr("href", "/static/css/elementary/color/pink-color.css")
    });
    $("#color-switcher .pallet-button").click(function () {
        $("#color-switcher .color-pallet").toggleClass('show')
    })

}

// /*-------------------------
//     MENU TOGGLER
// -------------------------*/
function PillMenuToggler() {

    "use strict";
    $(".overlay-menu-toggler").click(function(){
        $(".overlay-menu").addClass("show");
    });
    $(".overlay-menu").click(function(){
        $(this).removeClass("show");
    });
}

function  menuToggler() {
    "use strict";
    var $menuToggler = $(".menu-toggler");
    var $header = $('header');
    $menuToggler.click(function () {
        $(this).toggleClass('open').find('i').toggleClass('lni-menu lni-close ');
        $header.toggleClass('open');
        $('.color-scheme, .pallet-button, .color-pallet').toggleClass('hide');
    });
    if ($window.width() < 1200){
        $('header li a').click(function () {
            $header.removeClass('open');
            $('.color-scheme, .pallet-button, .color-pallet').toggleClass('hide');
            $menuToggler.removeClass('open').find('i').removeClass('lni-close').addClass('lni-menu');
        })
    }
}
/*-----------------------------
      SLIDER OWL CAROUSEL
------------------------------*/
function sliderOwlCarousel(){
    $('.hero-03 .owl-carousel').owlCarousel({
        loop:true,
        items: 1,
        nav: false,
        dots: false,
        autoplay:true,
        touchDrag: true,
        smartSpeed: 5000,
        animateOut: 'fadeOut',
        //autoplayHoverPause: true,
    });
    $('#hero-slider').on("translate.owl.carousel", function(){
        setTimeout(function(){
            $('.hero-slide').removeClass("zoom");
        }, 1000)
    });
    $('#hero-slider').on("translated.owl.carousel", function(){
        $('.owl-item.active .hero-slide').addClass("zoom");
    });
}
/*-------------------------
        TYPED JS
-------------------------*/
function typedJS() {

    "use strict";

    var options = {
        strings: $(".element").attr('data-elements').split(','),
        typeSpeed: 100,
        backDelay: 3000,
        backSpeed: 50,
        loop: true
    };
    var typed = new Typed(".element", options);
}
/*-------------------------
          Skills
-------------------------*/
function skills() {

    "use strict";
    $('.skillbar').each(function () {
        $(this).find('.skillbar-bar').animate({
            width: $(this).attr('data-percent')
        }, 6000);
    });
}

/*-------------------------
         Count up
-------------------------*/
function countUp() {

    "use strict";

    $('.timer').countTo();
    $('.count-number').removeClass('timer');

}
/*-------------------------
     MAGNIFIC POPUP JS
-------------------------*/
function portfolioPopup() {

    "use strict";

    if (('.portfolio-items').length > 0) {
        $('.portfolio-items').each(function() {
            $(this).magnificPopup({
                delegate: '.js-zoom-gallery',
                type: 'image',
                gallery: {
                    enabled:true
                }
            });
        });
    }
}
/*-------------------------
        ISOTOPE JS
-------------------------*/
function portfolioIsotop() {

    "use strict";

    var $container = $('.portfolio-items');
    var $filter = $('#portfolio-filter');
    $container.isotope({
        filter: '*',
        layoutMode: 'masonry',
        animationOptions: {
            duration: 750,
            easing: 'linear'
        }
    });
    $filter.find('a').on("click",function() {
        var selector = $(this).attr('data-filter');
        $filter.find('a').removeClass('active');
        $(this).addClass('active');
        $container.isotope({
            filter: selector,
            animationOptions: {
                animationDuration: 750,
                easing: 'linear',
                queue: false,
                touchSensitivity: 2,
            }
        });
        return false;
    });
}

/*-------------------------
  Testimonial CAROUSEL JS
-------------------------*/
function clientCarousel() {
    $(".testimonial .owl-carousel").owlCarousel({
        loop: true,
        margin: 30,
        stagePadding: 5,
        nav: false,
        autoplay: false,
        dots: true,
        mouseDrag: true,
        touchDrag: true,
        smartSpeed: 700,
        autoplayHoverPause: false,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: false
            },
            992: {
                items: 3,
                nav: false,
            },

        }
    });
}
/*-------------------------
     Blog CAROUSEL JS
-------------------------*/
function BlogCarousel() {

    "use strict";

    $(".blog .owl-carousel").owlCarousel({
        items: 1,
        nav: false,
        autoplay: false,
        loop: true,
        dots: true,
        margin: 30,
        mouseDrag: true,
        touchDrag: true,
        smartSpeed: 1000,
        autoplayHoverPause: true,

    });
}
/*-------------------------
     AJAX CONTACT FORM
-------------------------*/
function validateEmail(email) {

    "use strict";

    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}
function sendEmail() {

    "use strict";

    var name     = $('#name').val();
    var email    = $('#email').val();
    var subject  = $('#subject').val();
    var comments = $('#comments').val();

    if(!name){
        $('#message').toast('show').addClass('bg-danger').removeClass('bg-success');
        $('.toast-body').html('Name is  required');
    } else if(!email){
        $('#message').toast('show').addClass('bg-danger').removeClass('bg-success');
        $('.toast-body').html('Email is  required');
    } else if(!validateEmail(email)){
        $('#message').toast('show').addClass('bg-danger').removeClass('bg-success');
        $('.toast-body').html('Email is not valid');
    } else if(!subject){
        $('#message').toast('show').addClass('bg-danger').removeClass('bg-success');
        $('.toast-body').html('Subject is  required');
    }else if(!comments){
        $('#message').toast('show').addClass('bg-danger').removeClass('bg-success');
        $('.toast-body').html('Comments is  required');
    }else {
        $.ajax({
            type: 'POST',
            data: $("#contactForm").serialize(),
            url:  "/play/",
            beforeSend: function() {
                $('#submit-btn').html('<span class="spinner-border spinner-border-sm"></span> Loading..');
            },
            success: function(data) {
                $('#submit-btn').html('Submit');
                $("#contactForm")[0].reset();
                var myObj = data;
                if(myObj['status']=='Congratulation'){
                    $('#message').toast('show').addClass('bg-success').removeClass('bg-danger bg-warning');
                    $('.toast-body').html('<strong>'+ myObj['status'] +' : </strong> '+ myObj['message']);
                }else if(myObj['status']=='Error'){
                    $('#message').toast('show').addClass('bg-danger').removeClass('bg-success bg-warning');
                    $('.toast-body').html('<strong>'+ myObj['status'] +' : </strong> '+ myObj['message']);
                }else if(myObj['status']=='Warning'){
                    $('#message').toast('show').addClass('bg-warning').removeClass('bg-success bg-danger');
                    $('.toast-body').html('<strong>'+ myObj['status'] +' : </strong> '+ myObj['message']);
                }
            },
            error: function(xhr) {
                $('#submit-btn').html('Submit');
                $('#message').toast('show').addClass('bg-danger').removeClass('bg-success bg-warning');
                $('.toast-body').html('<strong> Error : </strong> Something went wrong, Please try again.');
            },
        });
    }
}

