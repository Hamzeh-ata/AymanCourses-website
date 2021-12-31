

fetch("http://127.0.0.1:8000/completed_courses/")
.then(function (response) {
    return response.json();
})
.then(function (data) {
    appendData(data);
})
.catch(function (err) {
    console.log('error: ' + err);
});


   function appendData(data){
       for(var i =0;i<data.length;i++){
        var newElement=document.createElement("div");
        newElement.className="col btn-col pt-2 pb-2";
        newElement.id='btn-col';
newElement.innerHTML=`
{% load static %}

  <button
   class="btn1"onclick="window.open('videos/${data[i].slug}','_self',)">

    <div  class="row btn-row">
    <div class="col-md-5 justify-content-center align-content-center d-flex">
        <img class="pt-1 pb-1 align-self-center img-thumb" src="./imgs/thumb.png" style="width: 100%; height: 85%;">
    </div>
    <div class="col-md-7 d-flex">
        <div class="course-info align-self-center">                        
      <div class="title-text pt-1">
          ${data[i].slug}
    </div>
    <div class="desc-text">
       اخل فقاعات من الوهم نعيش، نرى العالم من حولنا بمفاهيمه التى أراد أن يصدرها لنا، نكتفي بالتحسر على الماضي العتيق، تهب علينا الريح من كل مكان سحيق، فيتبدل وعي أجيال كاملة، وتتحول ثقافات
    </div>
    <div class="course_info pt-1 pb-1">
        <div class="row">
            <div class="col">
                  <div class="course_videos_count">
                   عدد الدروس
                  </div>        
                </div>
            <div class="col">
               <div class="course_time">
               عدد ساعات الدورة 
           </div>
           </div>        
        </div>
        <div class="row">
           <div class="col">
                 <div class="course_videos_number">
                  ${data[i].course_count}
                 </div>
             </div>
           <div class="col">
              <div class="course_videos_number">
               ${data[i].course_time}
          </div>
          </div>
          </div>
    </div>
   </div>
 </button>
 </div>`
 document.getElementById('row-2').appendChild(newElement);
 if(i==1 || i==3){
    var space=document.createElement("div");
    space.className="w-100";
    space.id='w100';
    document.getElementById('row-2').appendChild(space);

 }

       }
   }


