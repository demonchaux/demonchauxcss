// Vars to change to local project directory
var jsonFile = "static/js/json/localcode_la.json";
var imageDirectory = "static/images/LA/"
// Duration of slideshow in seconds
var slideDuration = 5;

var street = "roads-fename";
var local = "localwaterbasin-hu_12_name";
var medium = "mediumwaterbasin-hu_10_name";
var regional = "largewaterbasin-hu_8_name";
var ground = "hydrography";
var soil = "soils-name";


$(function(){
        $.get(jsonFile, function( data ) {
                var sites = data;
                                                                
                function startSlides(imageSlide, step){
                        var idx = imageSlide.data('siteindex') + step;
                        
                        if (idx < 0){
                                idx = sites.length - 1;
                        }
                        if (idx == sites.length){
                                idx = 0;
                        }
                        
                        imageSlide.data('siteindex',idx);								
                        newSite = sites[idx];
                        // swap image
                        imageSlide.children('.siteimage')
                        .fadeOut('fast', siteCall(imageSlide, newSite));
                };
                
                function siteCall(imageSlide, newSite){
                        return function(){
                                var img = imageSlide.children('.siteimage');
                                img.bind("load",function(){
                                        $(this).fadeIn();
                                });
                                img.attr('src', imageDirectory + newSite.images);
                                // swap text bits
                                
                                // Here we need to add a . + the name of the var....
                                // We also need to switch the name of the var inside the [ ]
                                imageSlide.find('.street').html(newSite[street]);
                                imageSlide.find('.local').html(newSite[local]);
                                imageSlide.find('.medium').html(newSite[medium]);
                                imageSlide.find('.regional').html(newSite[regional]);
                                imageSlide.find('.ground').html(newSite[ground]);
                                imageSlide.find('.soil').html(newSite[soil]);
                        }
                }
                
                // This initiates the counter
                $('#siteslides2').data('siteindex',0)
                
                // This is an automatic counter
                var refreshSlide = setInterval(function() {
                      startSlides($('#siteslides2'),1);
                }, 1000 * slideDuration);
                
                // This Pauses the slideshow when hovering over the image
                $('#siteslides2').hover(function() {
                    clearInterval(refreshSlide);
                }, function() {
                        refreshSlide = setInterval(function() {
                                startSlides($('#siteslides2'),1);
                                }, 1000 * slideDuration);
                });
                
                // This goes forward if clicked
                $('#forwardtab2').click(function(){
                        startSlides($('#siteslides2'),1);
                });
                // This goes backwards if clicked
                $('#backwardtab2').click(function(){
                        startSlides($('#siteslides2'),-1);
                });
        });
});