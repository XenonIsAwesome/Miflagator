


document.addEventListener('DOMContentLoaded', () => {

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    var question = document.getElementById("question_container")

    socket.on('redirect', function(data)
    {
        window.location = data.url;
    });

    socket.on('new_question', data => {
        question.innerHTML = 'שאלה ' + (data['counter']) + '/10 </br></br>' + data['content']
    })

    if(document.querySelector("#yes_button") != null){
            document.querySelector("#yes_button").addEventListener("click", function(e){
            e.preventDefault();    //stop form from submitting
            console.log('banana')
            socket.emit("answer", {"button": "y"} )
            console.log('banono')
            })
    }

    if(document.querySelector("#no_button") != null){
            document.querySelector("#no_button").addEventListener("click", function(e){
            e.preventDefault();    //stop form from submitting
            socket.emit("answer", {"button": "n"} )
            })
    }

    if(document.querySelector("#passive_button") != null){
            document.querySelector("#passive_button").addEventListener("click", function(e){
            e.preventDefault();    //stop form from submitting
            socket.emit("answer", {"button": "p"} )
            })
    }
})