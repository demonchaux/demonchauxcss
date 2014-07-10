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

    function getColumns() {
        var columns = $('#measure span'),
            choosen = 4;
        console.log('check');
        $.each(columns, function(index, item){
            var el = $(item);
            console.log(el.css('display'));
            if (el.css('display') == 'block') {
                console.log(el.prop('class') + " " + parseInt(el.html()));
                choosen = parseInt(el.html());
            }
        });
        return choosen;
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

    function initGallery() {
        var gallerias = $('.galleria');
        if (gallerias.length == 0) {
            return false;
        }
        $.each(gallerias, function(index, item){
            var id = '#' + $(item).attr('id');
            $(id).bxSlider({
                pager: false
            });
        });
    }
    initGallery();

    function paperLayout(columns) {
        Array.prototype.repeat= function(what, L){
            while(L) this[--L]= what;
            return this;
        }
        Array.prototype.max = function(comparer) {
            if (this.length === 0) return null;
            if (this.length === 1) return this[0];
            comparer = (comparer || Math.max);
            var v = this[0];
            for (var i = 1; i < this.length; i++) {
                v = comparer(this[i], v);
            }
            return v;
        }
        var blocks = $('.cblock'),
            columns,
            perLine,
            indent,
            left,
            top,
            maxHeight = [];

        columns = getColumns();
        console.log("choosen = " + columns);
        indent = 20;
        currCount = columns;
        bWidth = $(blocks).first().width();
        maxHeight.repeat(0, columns);

        var matrix = [],
            arr = [];

        $.each(blocks, function(index, item){
            arr.push($(item));
            currCount -= 1;
            if (currCount == 0) {
                currCount = columns;
                matrix.push(arr);
                arr = [];
            }
        });
        if (arr.length != 0) {
            matrix.push(arr);
        }

        top = 0;
        $.each(matrix, function(i, line) {
            left = 0;
            $.each(line, function(j, item) {
                maxHeight[j] += item.height() + parseInt(item.css('padding-top')) + parseInt(item.css('padding-bottom'));
                if (i != 0) {
                    // Calculate top
                    var el = matrix[i - 1][j],
                        height;
                    height = el.height() + parseInt(el.css('padding-top')) + parseInt(el.css('padding-bottom'));
                    top = height + indent;
                }
                if (j != 0) {
                    // Calculate left
                    var el = matrix[i][j - 1],
                        width;
                    width = el.width() + parseInt(el.css('padding-left')) + parseInt(el.css('padding-right'));
                    left += width + indent;
                }
                item.css({
                    'position': 'absolute',
                    'left': left,
                    'top': top
                });
            });
        });
        $('.main').css({
            'height': maxHeight.max() + 2 * indent
        });
    }
    $(window).resize(function(){
        paperLayout();
    });

    paperLayout();
});
