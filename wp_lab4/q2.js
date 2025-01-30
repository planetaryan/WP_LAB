$(document).ready(function() {
    $("button").click(function() {

        var num1 = parseFloat($("input:eq(0)").val());
        var num2 = parseFloat($("input:eq(1)").val());


        if (isNaN(num1) || isNaN(num2)) {
            $(".output").text("Please enter valid numbers.");
            return;
        }

        var result;

        switch (this.id) {
            case "add":
                result = num1 + num2;
                break;
            case "subtract":
                result = num1 - num2;
                break;
            case "multiply":
                result = num1 * num2;
                break;
            case "divide":
                if (num2 === 0) {
                    result = "Cannot divide by zero!";
                } else {
                    result = num1 / num2;
                }
                break;
        }


        $(".output").text("Result: " + result);
    });
});
