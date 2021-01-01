//Function that hides and shows comments
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

//Simple function to hide banners after load
  function rollimg() {
    let banneruls = document.getElementsByClassName("bannerul")
    for(i=0; i<banneruls.length; i++)
    {
      banneruls[i].style.display="none";
    }
    banneruls[0].style.display="block";
  }

//Function to previous banner
  function previous_img()
  {
    let banners = document.getElementsByClassName("bannerul");
    var index = 0;
    for (i=0; i<banners.length; i++)
    {
      if (banners[i].style.display == "block")
        {
          index = i;
        }
    }
    if(index == 0)
      {
        banners[index].style.display = "none";
        index = banners.length-1;
        banners[index].style.display = "block";
      }
    else
      {
        banners[index].style.display = "none";
        banners[index-1].style.display = "block";
      }
  }

//Fuction to next banner
  function next_img()
  {
    let banners = document.getElementsByClassName("bannerul");
    var index = 0;
    for (i=0; i<banners.length; i++)
    {
      if (banners[i].style.display == "block")
        {
          index = i;
        }
    }

    if(index == banners.length-1)
      {
        banners[index].style.display = "none";
        index = 0;
        banners[index].style.display = "block";
      }
    else
    {
      banners[index].style.display = "none";
      banners[index+1].style.display = "block";
    }
  }
