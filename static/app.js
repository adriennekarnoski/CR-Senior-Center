$(document).ready(function(){
    $("#button").click(function(){
        $('.modal').popup('show');
    });

    $(".close").click(function(){
        $('.modal').popup('hide');
    });
});



$(document).ready(function(){
    $("#cleared_checkbox").click(function(){
        if($("#cleared_checkbox").is(':checked')) {
            $("#hole").val('date');
        } else {
            $("#hole").val('pending');
        };
        
    });
});