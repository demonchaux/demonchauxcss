$.getJSON("static/js/test.json", function(data) {
    //console.log(data);
    //console.log(data[1]);
    for (i in data){
        var site = data[i];
        //console.log(data[i]);
        var sid = parseInt(i)+1; //site['sid'];
        var string_sid = new String(sid);
        
        // This is the right syntax
        //$('#slider').append('<img src="static/images/LA/'+'full13.jpg" alt="" alt="" title="#caption3">');
        var site_img = '<img src="static/images/LA/' + sid +'.jpg"';
        var site_caption = ' alt="" alt="" title='+ '"#' + sid + '">';
        
        // Here I append the image to the other images
        $('#slider').append(site_img + site_caption);
        console.log(site_img + site_caption);

        // This is where I define the captions
        
        var caption_arr = [ ];
        var caption = '<div id='+ string_sid + ' class="nivo-html-caption"> ';
        for (j in site){
            var new_caption = caption + '<strong>' + j + '</strong>  <em>' + site[j] + '</em><br>';
            caption = new_caption;
            caption_arr.push(caption);
            //console.log(j,site[j]);
        //console.log(new_caption);
        //console.log(caption_arr[caption_arr.length - 1]);
        // I need to figure out a way to create new html elements from scratch.... in the right structure... adding them randomly will not work unless they exist
        $.append(caption_arr[caption_arr.length - 1]);
        }
    };
});

//<div id="caption1" class="nivo-html-caption"> <strong>New Project</strong>  <em>Some description here</em><br>Hello World <em>this is a new line.</em>