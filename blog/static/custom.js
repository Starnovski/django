
  function show_comments(){

  let comments = document.getElementsByClassName("mb-0");
  for (i=0; i<comments.length; i++)
  {
    if (comments[i].style.display === "none"){
      comments[i].style.display = "block";
      }
    else {
      comments[i].style.display = "none";
    }
  }
  let button = document.getElementById("show_comments");
  if (button.innerHTML === "Show comments"){
    button.innerHTML = "Hide comments";}
    else{button.innerHTML = "Show comments";}
    
  }
