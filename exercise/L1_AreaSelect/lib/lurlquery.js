var lSendUrl = function(PostType, Url, formData, successPaperState, self){
	var xmlhttp;

	if(PostType == 'GET'){
		if (window.XMLHttpRequest){
		// code for IE7+, Firefox, Chrome, Opera, Safari
	        xmlhttp=new XMLHttpRequest();
	    }else{
	    // code for IE6, IE5
	        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	    }
	    xmlhttp.onreadystatechange = function(){
	        // self.successPaperState(self);
	        successPaperState();
	    }
	    xmlhttp.open(PostType, Url, true);
	    xmlhttp.send(null);

	}else{
		$.ajax({
			url: Url,
			type: "POST",
			dataType: 'JSON',
			data: formData,		
	        crossDomain: true, 
			processData: false,
			contentType: false,
			success: function(response) {
			  //set the thumbnail
			// successPaperState();
				successPaperState(response, self);
				// console.log(" connect to DB ", response);
			},
			error: function(jqXHR, textStatus, errorMessage) {
			  	console.log(errorMessage); // Optional
			}
		});
	}   
}
