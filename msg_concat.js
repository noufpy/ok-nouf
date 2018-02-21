let jsonfile = require('jsonfile');
let fs = require('fs');
let stream;

function readFiles(dirname, onFileContent, onError) {
  fs.readdir(dirname, function(err, filenames) {
    if (err) {
      onError(err);
      return;
    }
    filenames.forEach(function(filename) {
      stream = fs.createWriteStream('data/chat.txt');

      jsonfile.readFile(dirname + filename, function(err, obj) {
        let conversation = obj.threads[0].messages;
        for (let i = conversation.length-1; i > -1; i--){
          // first message
          let msg = "";
          let who = conversation[i].sender;
          msg += conversation[i].message.replace('\n', ' ');
          // if the next one(s) is(are) form the same sender, CONCATENATE!
          if(i>0) {
            while (conversation[i-1].sender == who && i > 0) {
              msg += ". " + conversation[i-1].message.replace('\n', ' ');
              i--;
              if(i == 0) break;
            }
          }
          msg += "\n"
          stream.write(msg)
        }
        // end jsonfile.readFile
      });
    });
  });
}

readFiles('messages/');

// jsonfile.readFile(file, function(err, obj) {
//   let conversation = obj.threads[0].messages;
//
//   for (i=0;i<conversation.length;i++){
//
//     // stream.write(conversation[i].message + ".\n");
//     // fs.writeFile("wassup.yml", conversation[i].message + ".\n", function(err) {
//     //   if(err) {
//     //       return console.log(err);
//     //   }
//     //   console.log("The file was saved!");
//     // });
//
//     if (conversation[i].sender == "Nouf Aljowaysir") {
//       stream.write("- - " + conversation[i-1].message + "\n");
//       stream.write("- " + conversation[i].message + "\n");
//       //console.log("-- " + conversation[i-1].message);
//       //console.log("- " + conversation[i].message);
//       //console.log(conversation[i].date + ": " + conversation[i].message);
//     }
//   }
// })
