
$(document).ready(function(){
    var page = $(location).attr('href');
    var fn = page.split('/').reverse()[0];
    if(/^\d+$/.test(fn)) {
        $(".edit_form").show();
    }
    $(".close").click(function(){
        $('.modal').popup('hide');
    });
});

$(document).ready(function(){
    $('#date_field').css("background", "#c8cdd0");      
    var selected_option = $('#new_form option:selected');
    $('select').change(function(){
        var selected_option = $('#new_form option:selected');
        if(selected_option.val() == 'YES') {
        $('#date_field').css("background", "white");      
        }
        if(selected_option.val() == 'NO') {
            $('#date_field').css("background", "#c8cdd0");      
        }
    });
});

$(document).ready(function(){
    $(".add_header").click(function(){
        $(".add_container").slideToggle();
    });
    $("#add_button").click(function(){
        $(".add_container").slideUp();
    });
});