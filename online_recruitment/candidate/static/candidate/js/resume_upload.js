constform = document.querySelector("form"),
fileInput = form.querySelector(".file-input"),
progressArea = document.querySelector(".pregress-area"),
uploadArea = document.querySelector(".uploaded-area"),

Form.addEventlistener("click",()=>{
     fileInput.click();
});

fileInput.onchange = ({target}) =>{
   let file = target.files[0];//getting file and [0] this mean if user has selected multiples files then get 
   if(file){//if file is selected
      let filename = file.name;//getting selected file name
      uploadfile(fileName);//calling uploadfile with passing file name as an argument
   }
}

function uploadfile(name){
   let xhr = new XMLHttpRequest();//creating new xml obj (AJAX)
   xhr.open("POST","php/uploadfile.php" );//sending post request to the specified URL/Files
   xhr.upload.addEventlistener("progress", ({loaded, total})  =>{
      let fileLoaded = Math.floor((loaded/total)* 100);//getting percentage of loaded file size 
      let fileTotal = Math.floor(total/1000);//getting file size in KBfrom bytes 
      let progressHTML =``;
      let uploadedHTML =``;
   });
   let formdata = new FormData(form);//formData is an object to easily send form data
   xhr.send(formData);//sending form data to php 
}