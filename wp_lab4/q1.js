$(document).ready(function(){
    $("#moveButton").click(function(){
        $(".table-container").animate({
            left: "-=300px"
        }, 2000);
    });
});
