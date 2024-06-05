var button = document.getElementById("frameContainer1")
if(button){
    button.addEventListener('click', function(e){
        window.location.href = "./customers.html";
    })
}


var frameContainer2 = document.getElementById("frameContainer2");
if (frameContainer2) {
  frameContainer2.addEventListener("click", function (e) {
    window.location.href = "./movies.html";
  });
}