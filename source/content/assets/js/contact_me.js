$(function() {
  $('.contactForm').submit(function(event) {
    event.preventDefault(); // Prevent the form from submitting via the browser
    var form = $(this);
    var post_url = '/contact/'; //get form action url
    var request_method = 'POST'; //get form GET/POST method
    var form_data = new FormData(this);

    $.ajax({
      url : post_url,
      type: request_method,
      data : form_data,
      contentType: false,
      cache: false,
      processData: false
    }).done(function(response){ //
        if(response["status"] == "NOT_OK")
        {
          $('.form').prepend(response["message"]);
        }
        else
        {
           $('.form').prepend(response["message"]);
           $('.contactForm').trigger('reset');
        }
    }).fail(function(response){
      $('.form').prepend(response["message"]);
  });
  });
});