$(window).load(function() {
        $('#slider').nivoSlider({
                effect: 'fade',
                directionNavHide: false,
                pauseOnHover: true,
                captionOpacity: 1,
                prevText: '<',
                nextText: '>',
                
                directionNav: true,
                //manualAdvance: true,
                animSpeed: 0,
                pauseTime: 5000,
                startSlide: 0, 
        });
});