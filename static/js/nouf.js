$(function() {
  //when button is clicked
  $('#button').click(function() {
    var userInput = $('#box').text();
    //sending socket
    let ws = new WebSocket("ws://localhost:8050/websocket");
    //open socket connection
    ws.onopen = function() {
      //send socket
      console.log(userInput);
      ws.send(userInput);
    };
    //receive socket
    ws.onmessage = function (evt) {
      console.log(evt.data);
      //$('#box2').removeAttr('data-placeholder');
       $('#box2').attr('data-placeholder','');
      $('#box2').text(evt.data);
    };
  });

  $(document).on('change keydown keypress input', 'div[data-placeholder]', function() {
    if (this.textContent) {
      this.dataset.divPlaceholderContent = 'true';
    } else {
      delete(this.dataset.divPlaceholderContent);
    }
  });
});
