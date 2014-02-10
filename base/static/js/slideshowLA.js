// Vars to change to local project directory
// Var names need to be changed on the siteCall function too

var jsonFile = "static/js/json/localcode_la.json";
var imageDirectory = "static/images/LA/"

$(function(){
    SlideShow = {
        imageSlide: '',
        sites: [],
        timer: '',

        // Fields
        street: "roads-fename",
        local: "localwaterbasin-hu_12_name",
        medium: "mediumwaterbasin-hu_10_name",
        regional: "largewaterbasin-hu_8_name",
        ground: "hydrography",
        soil: "soils-name",

        jsonFile: '',
        imageDirectory: '',

        createTimer: function(){
            // This is an automatic counter
            // var refreshSlide = setInterval(function() {
            //       startSlides($('#siteslides'),1);
            // }, 1000 * slideDuration);
            var that = this;
            this.timer = setInterval(function(){
                that.starSlides(1);
            }, 1000 * 5);
        },

        initialize : function(element, jsonFile, imageDirectory) {
            var that = this;
            this.imageSlide = $(element);
            this.jsonFile = jsonFile;
            this.imageDirectory = imageDirectory;

            $.get(jsonFile, function(data) {
                // Save data
                that.sites = data;
                // This initiates the counter
                that.imageSlide.data('siteindex', 0);
                // Create timer

                that.createTimer();

                // Binding events
                that.imageSlide.hover(function(){
                    clearInterval(that.timer)
                }, function(){
                    that.createTimer();
                });
                // This Pauses the slideshow when hovering over the image
                // $('#siteslides').hover(function() {
                //     clearInterval(refreshSlide);
                // }, function() {
                //     refreshSlide = setInterval(function() {
                //         startSlides($('#siteslides'),1);
                //     }, 1000 * slideDuration);
                // });
                that.imageSlide.on('click', '.slide .galleria-image-nav-right', function(event){
                    event.preventDefault();
                    that.starSlides(1);
                });

                that.imageSlide.on('click', '.slide .galleria-image-nav-left', function(event){
                    event.preventDefault();
                    that.starSlides(-1);
                });
                that.starSlides(1);
                // // This goes forward if clicked
                // $('#forwardtab').click(function(){
                //     startSlides($('#siteslides'),1);
                // });
                // // This goes backwards if clicked
                // $('#backwardtab').click(function(){
                //     startSlides($('#siteslides'),-1);
                // });
            });
        },

        starSlides: function(step){
            var idx = this.imageSlide.data('siteindex') + step;
            if (idx < 0){
                idx = this.sites.length - 1;
            }
            if (idx == this.sites.length){
                idx = 0;
            }
            this.imageSlide.data('siteindex', idx);
            newSite = this.sites[idx];
            // swap image
            // console.log(this.imageSlide.find('.galleria img').attr('src'));
            this.imageSlide.find('.galleria img')
            .fadeOut('fast', this.siteCall(this.imageSlide, newSite));
        },

        siteCall: function(imageSlide, newSite){
            var that = this;
            return function(){
                var img = that.imageSlide.find('.galleria img');
                img.bind("load", function(){
                    $(this).fadeIn();
                });
                img.attr('src', that.imageDirectory + newSite.images);
                // swap text bits
                // Here we need to add a . + the name of the var....
                // We also need to switch the name of the var inside the [ ]
                that.imageSlide.find('.street').html(newSite[that.street]);
                that.imageSlide.find('.local').html(newSite[that.local]);
                that.imageSlide.find('.medium').html(newSite[that.medium]);
                that.imageSlide.find('.regional').html(newSite[that.regional]);
                that.imageSlide.find('.ground').html(newSite[that.ground]);
                that.imageSlide.find('.soil').html(newSite[that.soil]);
            }
        },
    };
    sliders = [];

    $.each($('.slide'), function(){
        var id = '#' + $(this).attr('id'),
            slider = $.extend(true, {}, SlideShow),
            element = $(id);
        slider.initialize(id, element.data('json'), element.data('image'));
        sliders.push(slider);
    });
});