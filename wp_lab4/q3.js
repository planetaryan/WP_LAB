$(document).ready(function() {
    $('#updateCard').click(function() {
        // Get user input values
        var bgColor = $('#bgColor').val();
        var font = $('#fontSelect').val();
        var fontSize = $('#fontSize').val();
        var border = $("input[name='border']:checked").val();
        var picture = $('#picture').is(':checked');
        var greetingText = $('#greeting').val();

        // Apply changes to the card container
        $('#cardContainer').css('background-color', bgColor);
        $('#cardText').css({
            'font-family': font,
            'font-size': fontSize + 'px'
        });

        // Apply border style
        if (border === "none") {
            $('.card').css('border', 'none');
        } else if (border === "solid") {
            $('.card').css('border', '5px solid black');
        } else {
            $('.card').css('border', '5px double black');
        }

        // Display picture if checkbox is checked
        if (picture) {
            $('.card').append('<img src="cake.jpeg" alt="Birthday Picture">');
        } else {
            $('.card img').remove();
        }

        // Set the greeting text
        $('#cardText').text(greetingText);
    });
});
