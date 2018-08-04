var wget=function(url,callback){var xhr=new XMLHttpRequest();xhr.onreadystatechange=function(){if(xhr.readyState==XMLHttpRequest.DONE)
callback(xhr.responseText);}
xhr.open('GET',url,true);xhr.send(null);};document.addEventListener('DOMContentLoaded',function(e){var server_id_meta=document.querySelector('meta[name="server_id"]');if(!server_id_meta)
return;if(!server_id_meta.getAttribute('content'))
return;wget('/api/server/'+server_id_meta.getAttribute('content')+'/logs',function(data){var logs=document.getElementById('logs');logs.innerHTML=JSON.parse(data);});});