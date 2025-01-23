function calc_avg(){
    let sum=0;
    const inputs=document.querySelectorAll('.marks');

    inputs.forEach(input => {
        sum+=parseFloat(input.value);
    });
    let avg=sum/inputs.length;
    document.getElementById('avg').innerText= "Your average is : " + avg;

    if(avg>90){
        document.getElementById('grade').innerText= "Your grade is : " + "A"; 
    }
    else if(avg>80){
        document.getElementById('grade').innerText= "Your grade is : " + "B";
    }
    else if(avg>70){
        document.getElementById('grade').innerText= "Your grade is : " + "C";
    }
    else if(avg>60){
        document.getElementById('grade').innerText= "Your grade is : " + "D";
    }
}