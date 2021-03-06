function random(owlSelector) {
        owlSelector.children().sort(function () {
            return Math.round(Math.random()) - 0.5;
        }).each(function () {
            $(this).appendTo(owlSelector);
        });
    }

$(document).ready(function () {
    $("#my-pic-carousel").owlCarousel({
        autoPlay: 5000,
        slideSpeed: 500,
        items: 1,
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [979, 1],
        itemsTablet: [768, 1],
        itemsMobile: [479, 1],
        autoHeight: true,
        pagination: false,
        navigation: true,
        navigationText: [
        "<i class='fa fa-angle-left'></i>",
        "<i class='fa fa-angle-right'></i>"
        ],
        //Call beforeInit callback, elem parameter point to $("#our-team")
       /* beforeInit: function (elem) {
            random(elem);
        }*/

    });

    $("#myskills-carousel").owlCarousel({
        autoPlay: 5000,
        slideSpeed: 500,
        items: 5,
        itemsDesktop: [1199, 5],
        itemsDesktopSmall: [979, 4],
        itemsTablet: [768, 2],
        itemsMobile: [479, 1],
        autoHeight: false,
        pagination: true,
        navigation: false,
        navigationText: [
        "<i class='fa fa-angle-left'></i>",
        "<i class='fa fa-angle-right'></i>"
        ],
        //Call beforeInit callback, elem parameter point to $("#our-team")
       /* beforeInit: function (elem) {
            random(elem);
        }*/

    });

    $("#services-carousel").owlCarousel({
        autoPlay: 5000,
        slideSpeed: 500,
        items: 4,
        itemsDesktop: [1199, 3],
        itemsDesktopSmall: [979, 3],
        itemsTablet: [768, 2],
        itemsMobile: [479, 1],
        autoHeight: true,
        pagination: true,
        navigation: false,
        navigationText: [
        "<i class='fa fa-angle-left'></i>",
        "<i class='fa fa-angle-right'></i>"
        ],
        //Call beforeInit callback, elem parameter point to $("#our-team")
       /* beforeInit: function (elem) {
            random(elem);
        }*/

    });

    $("#awards-carousel").owlCarousel({
        autoPlay: 5000,
        slideSpeed: 500,
        items: 4,
        itemsDesktop: [1199, 3],
        itemsDesktopSmall: [979, 3],
        itemsTablet: [768, 2],
        itemsMobile: [479, 1],
        autoHeight: true,
        pagination: true,
        navigation: false,
        navigationText: [
        "<i class='fa fa-angle-left'></i>",
        "<i class='fa fa-angle-right'></i>"
        ],
        //Call beforeInit callback, elem parameter point to $("#our-team")
       /* beforeInit: function (elem) {
            random(elem);
        }*/

    });

    $("#testimonials-carousel").owlCarousel({
        autoPlay: 5000,
        slideSpeed: 500,
        items: 1,
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [979, 1],
        itemsTablet: [768, 1],
        itemsMobile: [479, 1],
        autoHeight: true,
        pagination: true,
        navigation: false,
        navigationText: [
        "<i class='fa fa-angle-left'></i>",
        "<i class='fa fa-angle-right'></i>"
        ],
        //Call beforeInit callback, elem parameter point to $("#our-team")
       /* beforeInit: function (elem) {
            random(elem);
        }*/

    });

    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('.scrollup').fadeIn();
        } else {
            $('.scrollup').fadeOut();
        }
    });

    $('.scrollup').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });

    $('.nav').onePageNav({
        filter: ':not(.external)',
        begin: function() {
            console.log('start')
        },
        end: function() {
            console.log('stop')
        }
    });

    $(document).delegate('*[data-toggle="lightbox"]', 'click', function(event) {
        event.preventDefault();
        return $(this).ekkoLightbox({
            onShown: function() {
                if (window.console) {
                    return console.log('Checking our the events huh?');
                }
            }
        });
    });

    //Programatically call
    $('#open-image').click(function (e) {
        e.preventDefault();
        $(this).ekkoLightbox();
    });
    $('#open-youtube').click(function (e) {
        e.preventDefault();
        $(this).ekkoLightbox();
    });

    $('.animated').appear(function() {
        var elem = $(this);
        var animation = elem.data('animation');
        if ( !elem.hasClass('visible') ) {
            var animationDelay = elem.data('animation-delay');
            if ( animationDelay ) {

                setTimeout(function(){
                    elem.addClass( animation + " visible" );
                }, animationDelay);

            } else {
                elem.addClass( animation + " visible" );
            }
        }
    });

    $('#preloader').fadeOut('slow');

    $('.image').click(function (event) {
        event.preventDefault();

        if ($('.portfolio-detail').hasClass('open-box')) {
            $('.portfolio-detail').addClass('closed-box');
            $('.portfolio-detail').removeClass('open-box');
        }

        var fileID = $(this).attr('data-project');

        if (fileID != null) {
            $('html,body').animate({
                scrollTop: $('.portfolio-detail').offset().top - 66
            }, 500);

        }

        $.ajax({
            url: fileID
        }).success(function (data) {
            $('.portfolio-detail').addClass('open-box');
            $('.portfolio-detail').html(data);
            $('.portfolio-detail').removeClass('closed-box');

            $('.close-detail').click(function () {
                $('.portfolio-detail').addClass('closed-box');
                $('.portfolio-detail').removeClass('open-box');
                $('html,body').animate({
                    scrollTop: $('#portfolio').offset().top - 66
                }, 500);
                setTimeout(function () {
                    $('.portfolio-detail').html('');
                }, 1000);
            });
        });

    });

});

$(window).load(function(){
    $("#navigation").sticky({ topSpacing: 0 });
});
