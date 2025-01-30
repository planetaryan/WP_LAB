$(document).ready(function() {
    $('#bill').click(function() {

        var brand = $('#brand').val();
        var price = 0;


        switch(brand) {
            case "hp": price = 500; break;
            case "nokia": price = 200; break;
            case "samsung": price = 300; break;
            case "motorola": price = 250; break;
            case "apple": price = 1000; break;
        }


        if ($('.select_device input[type="checkbox"]:eq(0)').is(':checked')) price += 100; // Mobile
        if ($('.select_device input[type="checkbox"]:eq(1)').is(':checked')) price += 700; // Laptop


        var quantity = $('.quantity input[type="number"]').val();
        var totalAmount = price * quantity;

        alert("Total Amount: $" + totalAmount);
    });
});
