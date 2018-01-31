// $(document).ready(function(){
//     $(".update").click(function(){
//         $('.modal').popup('show');
//     });

//     $(".close").click(function(){
//         $('.modal').popup('hide');
//     });
// });



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
