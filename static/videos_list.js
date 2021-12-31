
  fetch("http://127.0.0.1:8000/course2/")
  .then(function (response) {
    return response.json();
})
.then(function (data) {
    appendData(data);
})
.catch(function (err) {
    console.log('error: ' + err);
});

  


function appendData(data) {
  var mainContainer = document.getElementsByClassName("span");
  for (var i = 0; i < data.length; i++) {
    var newElement=document.createElement("div");
   
      newElement.innerHTML=`
      {% load static %}

      <div class="col-sm align-self-center courses_col pt-2 pb-2 justify-content-center d-flex">
    <div class="button-secition">
        <div class="row w-100 ml-0 ">
            <div class="col-md-3 justify-content-center d-flex">
               <img class="img-thumb " src="/imgs/ta2ses.png">
               
            </div>
            <div class="col-md-7 d-flex justify-content-center">
                <div class="button-content align-self-center justify-content-center ">
                   <div class="video-title text-center align-self-center j">${data[i].video_title}</div>
                   <div class="video-time text-center align-self-center">${data[i].video_time}</div>
                 </div>
            </div>
            <div class="col-md-2 d-flex justify-content-center align-content-center">
                <div class="d-s"> 
                   <button class="download-button"></button>
                   <button class="share-button"></button>
                </div>
           </div>
        </div>
       </div>    
  </div>`
  document.getElementById('row2').appendChild(newElement);
  }
}


  

