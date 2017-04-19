
// TODO use AJAX or remove it

// $(document).ready(function(){

//   $('#importJsonBtn').click(function(evt) {
//       $("#file-input").click();
//   });
//   $("#file-input").change(function(e){
//     importJson(e)
//   })

//   // first get the CSRF token
//   function getCookie(name) {
//       var cookieValue = null;
//       if (document.cookie && document.cookie !== '') {
//           var cookies = document.cookie.split(';');
//           for (var i = 0; i < cookies.length; i++) {
//               var cookie = jQuery.trim(cookies[i]);
//               // Does this cookie string begin with the name we want?
//               if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                   break;
//               }
//           }
//       }
//       return cookieValue;
//   }
//   var csrftoken = getCookie('csrftoken');
//   function csrfSafeMethod(method) {
//       // these HTTP methods do not require CSRF protection
//       return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//   }


//   function importJson(e) {
//       var file = e.target.files[0];
//       if (!file) {
//           return;
//       }
//       var reader = new FileReader();
//       reader.onload = function(e) {
//           var contents = e.target.result;

//           $.ajaxSetup({
//               beforeSend: function(xhr, settings) {
//                   if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//                       xhr.setRequestHeader("X-CSRFToken", csrftoken);
//                   }
//               }
//           });

//           $.ajax({
//               url : '/catalog/uploadcsv/upload/',
//               type : 'POST',
//               data : contents,
//               dataType:'text/csv',
//               success : function(data) {              
//                   console.log('Data: '+data);
//               },
//               error : function(request,error)
//               {
//                   console.log("Request: "+JSON.stringify(request));
//               }
//           });
//       };
//       reader.readAsText(file);
//   }

// });

