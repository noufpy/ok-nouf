$(document).on('change keydown keypress input', 'div[data-placeholder]', function() {
  if (this.textContent) {
    this.dataset.divPlaceholderContent = 'true';
  } else {
    delete(this.dataset.divPlaceholderContent);
  }
});
$("#box").bind("input", function (event) {
  let name = $('#box').text().length;

  if (name > 5) {
    $('#button').prop('disabled', false);
  }else {
    $('#button').prop('disabled', true);
  }
});

$('#button').click(function() {

  window.location.href='/index.html';
});

function readTextFile(file)
{
     var rawFile = new XMLHttpRequest();
     rawFile.open("GET", file, false);
     rawFile.onreadystatechange = function ()
     {
         if(rawFile.readyState === 4)
         {
             if(rawFile.status === 200 || rawFile.status == 0)
             {
                 var allText = rawFile.responseText;
                 doSomethingWithTheText(allText);
             }
         }
     }
     rawFile.send(null);
}

readTextFile("./Users/noufaljowaysir/github/ok-nouf/static/json/Friends.txt");
