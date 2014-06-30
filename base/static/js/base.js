$(document).ready(function(){
    // $('.slides').slidesjs({
    //     width: 241,
    //     height: 241,
    //     play: {
    //         active: false,
    //         // [boolean] Generate the play and stop buttons.
    //         // You cannot use your own buttons. Sorry.
    //         effect: "slide",
    //         // [string] Can be either "slide" or "fade".
    //         interval: 5000,
    //         // [number] Time spent on each slide in milliseconds.
    //         auto: true,
    //         // [boolean] Start playing the slideshow on load.
    //         swap: false,
    //         // [boolean] show/hide stop and play buttons
    //         pauseOnHover: true,
    //         // [boolean] pause a playing slideshow on hover
    //         restartDelay: 2500
    //         // [number] restart delay on inactive slideshow
    //     },
    //     callback: {
    //         loaded: function(number) {
    //             $.each($('.slides'), function() {
    //                 $(this).find('.slidesjs-navigation').wrapAll('<div class="slides_navigation"></div>');
    //             });
    //             $('a.slidesjs-previous').attr('id', 'backwardtab').html('&lt;')
    //             $('a.slidesjs-next').attr('id', 'forwardtab').html('&gt;');
    //             $('.slidesjs-pagination').css('display', 'none');
    //         }
    //     }
    // });
    if ($('.galleria').length > 0) {

        Galleria.run(".galleria", {
            thumbnails: "false",
            imageCrop: "width"
        });
        Galleria.ready(function(){
            $('.slide .galleria > img').remove();
        });
    }

    function scrollHeader() {
        if ($('.contentpage').length == 0) {
            return false;
        }
        var maxScroll = 50;
        $(window).scroll(function(event){
            var st = $(this).scrollTop(),
                header = $('.header'),
                content = $('.content');

            if (st > maxScroll){
                console.log('Down ' + st.toString());
                header.addClass('scrolled');
                content.addClass('scrolled');
            }
            else {
                console.log('Up ' + st.toString());
                header.removeClass('scrolled');
                content.removeClass('scrolled');
            }
        });
    }
    scrollHeader();
});
