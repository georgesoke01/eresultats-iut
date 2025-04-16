document.addEventListener("DOMContentLoaded",function(){
    const colors = ["#ff9900", "#00cc99", "#9933cc", "#3399ff", "#ff6699", "#66cc33", "#ffcc00", "#0099cc", "#cc3399", "#33cc66"];
    const exam_number = document.querySelectorAll(".exam-number");

    function getRandomColor(excludeColor){
        let availableColors = colors.filter(color => color !==excludeColor);
        return availableColors[Math.floor(Math.random()* availableColors.length)];
    }

    let previousColor = null;
    exam_number.forEach(exam_number =>{
        let newColor = getRandomColor(previousColor);
        exam_number.style.backgroundColor = newColor;
        previousColor = newColor; 
    });
} );