let slides = document.querySelectorAll('.trending__article .slide');
let nav_width = $(".navigation").width();
let currentSlide = 0;

if(nav_width > 716){
    $(".cat_wrapper .cat_left_side .forcat_ref a").removeAttr( "href" )
    $(".create_button__inner, .center_text").removeClass("reduced_opc")
    $(window).resize(function(){
    if(nav_width > 716){
        $(".cat_wrapper .cat_left_side .forcat_ref a").removeAttr( "href" ) 
        $("input[name='input_name']").prop("checked", false);
        $("input[name='forcat']").prop("checked", false);
        $("input[name='forvid']").prop("checked", false);
        $("input[name='fortip']").prop("checked", false);
      }     
        
    })
}
else{
    $(".cat_wrapper .cat_left_side .forcat_ref a").attr( "href" )
    $(".create_button__inner, .center_text").removeClass("reduced_opc")
    $(window).resize(function(){    
        $("input[name='input_name']").prop("checked", false);
        $("input[name='forcat']").prop("checked", false);
        $("input[name='forvid']").prop("checked", false);
        $("input[name='fortip']").prop("checked", false);
    })
}

$(".input_raw").on("click", function(){
    if($("input[name='input_name']").is(":checked")){
        $(".create_button__inner, .center_text").addClass("reduced_opc")
        $(window).resize(function(){  
        if(nav_width > 716){
            $(".create_button__inner, .center_text").removeClass("reduced_opc")
             $("input[name='input_name']").prop("checked", false);
             $("input[name='forcat']").prop("checked", false);
             $("input[name='forvid']").prop("checked", false);
             $("input[name='fortip']").prop("checked", false);
        }
        })}
    else{
        $(".create_button__inner, .center_text").removeClass("reduced_opc")
        
    }
});

$(window).scroll(function(){
    if($(this).scrollTop() > 10){
        $( ".dummy" ).addClass("toTop").fadeIn( "slow" );
    }
    else{
        $( ".toTop" ).css( "display", "none" ).fadeOut( "slow" );
    }
})

$( document ).ready(function() {
 $( ".cat_content_2" ).addClass("hideItem");
 $( ".cat_content_3" ).addClass("hideItem");
 $( ".cat_content_4" ).addClass("hideItem");
 $( ".cat_content_5" ).addClass("hideItem");
});

$(".left_sider1").on("click", function(){
    $( ".left_sider1" ).addClass("active");
    $( ".left_sider2" ).removeClass("active");
    $( ".left_sider3" ).removeClass("active");
    $( ".left_sider4" ).removeClass("active");
    $( ".left_sider5" ).removeClass("active");
    $( ".cat_content_1" ).removeClass("hideItem");
    $( ".cat_content_2" ).addClass("hideItem");
    $( ".cat_content_3" ).addClass("hideItem");
    $( ".cat_content_4" ).addClass("hideItem");
    $( ".cat_content_5" ).addClass("hideItem");
    

})

$(".left_sider2").on("click", function(){
    $( ".left_sider2" ).addClass("active");
    $( ".left_sider1" ).removeClass("active");
    $( ".left_sider3" ).removeClass("active");
    $( ".left_sider4" ).removeClass("active");
    $( ".left_sider5" ).removeClass("active");

    $( ".cat_content_1" ).addClass("hideItem");
    $( ".cat_content_2" ).removeClass("hideItem");
    $( ".cat_content_3" ).addClass("hideItem");
    $( ".cat_content_4" ).addClass("hideItem");
    $( ".cat_content_5" ).addClass("hideItem");
    
})

$(".left_sider3").on("click", function(){
    $( ".left_sider3" ).addClass("active");
    $( ".left_sider2" ).removeClass("active");
    $( ".left_sider1" ).removeClass("active");
    $( ".left_sider4" ).removeClass("active");
    $( ".left_sider5" ).removeClass("active");
    $( ".cat_content_1" ).addClass("hideItem");
    $( ".cat_content_2" ).addClass("hideItem");
    $( ".cat_content_3" ).removeClass("hideItem");
    $( ".cat_content_4" ).addClass("hideItem");
    $( ".cat_content_5" ).addClass("hideItem");
})

$(".left_sider4").on("click", function(){
    $( ".left_sider4" ).addClass("active");
    $( ".left_sider5" ).removeClass("active");
    $( ".left_sider3" ).removeClass("active");
    $( ".left_sider2" ).removeClass("active");
    $( ".left_sider1" ).removeClass("active");
    $( ".cat_content_1" ).addClass("hideItem");
    $( ".cat_content_2" ).addClass("hideItem");
    $( ".cat_content_3" ).addClass("hideItem");
    $( ".cat_content_4" ).removeClass("hideItem");
    $( ".cat_content_5" ).addClass("hideItem");
})

$(".left_sider5").on("click", function(){
    $( ".left_sider5" ).addClass("active");
    $( ".left_sider4" ).removeClass("active");
    $( ".left_sider3" ).removeClass("active");
    $( ".left_sider2" ).removeClass("active");
    $( ".left_sider1" ).removeClass("active");
    $( ".cat_content_1" ).addClass("hideItem");
    $( ".cat_content_3" ).addClass("hideItem");
    $( ".cat_content_4" ).addClass("hideItem");
    $( ".cat_content_5" ).removeClass("hideItem");
    $( ".cat_content_2" ).addClass("hideItem");
})

$(document).on({
    mouseenter:function(){
        $( ".cat_wrapper" ).addClass("do_wrap")
    },
    mouseleave:function(){
        $( ".cat_wrapper" ).removeClass("do_wrap")
    }}, ".cat_controller"
  )


$(document).on({
    mouseenter:function(){
        $( ".vid_wrapper" ).addClass("do_wrap")
    },
    mouseleave:function(){
        $( ".vid_wrapper" ).removeClass("do_wrap")
    }}, ".vid_controller"
  )

$(document).on({
    mouseenter:function(){
        $( ".tip_wrapper" ).addClass("do_wrap")
    },
    mouseleave:function(){
        $( ".tip_wrapper" ).removeClass("do_wrap")
    }}, ".tip_controller"
  )


$(".label_ui_target").on("click", function(){
    if($("input[name='ui_target']").is(":checked")){
         $( ".ui_target .fa-chevron-down" ).removeClass("rotate-up")
         $( ".all_ui_content").removeClass("dynamic_margin")
         $( ".ui_target").removeClass("no_radius")
        }
    else{
        $( ".ui_target .fa-chevron-down" ).addClass("rotate-up")
        $( ".all_ui_content").addClass("dynamic_margin")
        $( ".ui_target").addClass("no_radius")
    }

});

$(".label_bke_target").on("click", function(){
    if($("input[name='bke_target']").is(":checked")){
         $( ".bke_target .fa-chevron-down" ).removeClass("rotate-up")
          $( ".bke_target").removeClass("no_radius")
        }
    else{
        $( ".bke_target .fa-chevron-down" ).addClass("rotate-up")
        $( ".bke_target").addClass("no_radius")
    }

});

$(".label_algo_target").on("click", function(){
    if($("input[name='algo_target']").is(":checked")){
         $( ".algo_target .fa-chevron-down" ).removeClass("rotate-up")
         $( ".algo_target").removeClass("no_radius")
        }
    else{
        $( ".algo_target .fa-chevron-down" ).addClass("rotate-up")
        $( ".algo_target").addClass("no_radius")

    }

});

$(".label_free_target").on("click", function(){
    if($("input[name='free_target']").is(":checked")){
         $( ".free_target .fa-chevron-down" ).removeClass("rotate-up")
         $( ".free_target").removeClass("no_radius")
        }
    else{
        $( ".free_target .fa-chevron-down" ).addClass("rotate-up")
        $( ".free_target").addClass("no_radius")
    }

});

$(".label_prm_target").on("click", function(){
    if($("input[name='prm_target']").is(":checked")){
         $( ".prm_target .fa-chevron-down" ).removeClass("rotate-up")
         $( ".prm_target").removeClass("no_radius")
        }
    else{
        $( ".prm_target .fa-chevron-down" ).addClass("rotate-up")
        $( ".prm_target").addClass("no_radius")
    }


});

$(".label_tips_target").on("click", function(){
    if($("input[name='tips_target']").is(":checked")){
         $( ".tips_target .fa-chevron-down" ).removeClass("rotate-up")
         $( ".tips_target").removeClass("no_radius")
        }
    else{
        $( ".tips_target .fa-chevron-down" ).addClass("rotate-up")
        $( ".tips_target").addClass("no_radius")
    }


});


function addPadding(){
    $( ".all_ui_content .toggle_ctg__others__descr" ).last().addClass("dynamic_padding")
    $( ".all_bke_content .toggle_ctg__others__descr" ).last().addClass("dynamic_padding")
    $( ".all_algo_content .toggle_ctg__others__descr" ).last().addClass("dynamic_padding")
    $( ".all_free_content .toggle_ctg__others__descr" ).last().addClass("dynamic_padding")
    $( ".all_prm_content .toggle_ctg__others__descr" ).last().addClass("dynamic_padding")
    $( ".all_tips_content .toggle_ctg__others__descr" ).last().addClass("dynamic_padding")
}
function addMargin(){
    $( ".all_ui_content").addClass("dynamic_margin")
    $( ".all_bke_content").addClass("dynamic_margin")
    $( ".all_algo_content").addClass("dynamic_margin")
    $( ".all_free_content").addClass("dynamic_margin")
    $( ".all_prm_content").addClass("dynamic_margin")
    $( ".all_tips_content").addClass("dynamic_margin")
}


addPadding();
addMargin();


$(".all_search").on("click", function(){
    $( ".navigation_search" ).toggle();
    $(window).scroll(function(){
        if($(this).scrollTop() > 0){
            console.log($(".navigation_search"))
            $(".navigation_search").fadeOut();
            $(".desktop_search .fa-search").addClass("icon_search_reset");
            $(".label_search").on("click", function(){
                if($( ".navigation_search" ).is(":visible")){
                    $(".desktop_search .fa-search").removeClass("icon_search_reset");
                    $(".desktop_search .fa-search").addClass("icon_search");
                }else{
                    $(".desktop_search .fa-search").addClass("icon_search_reset");
                    $(".desktop_search .fa-search").removeClass("icon_search")
                }   
            })
                    
        }
    })
    

});


$(".label_search").on("click", function(){
    if($("input[name='nav_searcher']").is(":checked")){
        $( ".desktop_search .fa-search").removeClass("icon_search")

    }else{
        $( ".desktop_search .fa-search").addClass("icon_search")
    }
})


$(window).on('load', function(){
    if(localStorage.getItem("enable-cookies")!="1"){
        $(".cookies").css( "display", "flex" )
        $("#store-cookie").on("click", function(){
        localStorage.setItem("enable-cookies", "1");
        $(".cookies").slideUp();
        });
    
    }
});


function nextSlide(){
    goToSlide(currentSlide + 1);
}

function previousSlide(){
    goToSlide(currentSlide - 1);
}


let slideInterval = setInterval(nextSlide, 10000);

function goToSlide(s){
    slides[currentSlide].className = 'slide';   
    currentSlide = (s + slides.length) % slides.length;
    slides[currentSlide].className = 'slide current';
}

let playing = true;

function pauseSlideshow(){
    playing = false;
    clearInterval(slideInterval);
}

function playSlideshow(){
    playing = true;
    slideInterval = setInterval(nextSlide, 10000);
}

let previous_btn = document.querySelector('.trending__icon1');
let next_btn = document.querySelector('.trending__icon2');

$(next_btn).on("click", function(){
    pauseSlideshow();
    nextSlide();
});

$(previous_btn).on("click", function(){
    pauseSlideshow();
    previousSlide();
});
