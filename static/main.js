$(function(){
    var TIMER = $('#timer')

    let decreaseTime = (setInterval(function() {
        let curTime = Number(TIMER.text())
        curTime--
        if (curTime <= 0){
            clearInterval(decreaseTime)
            $('#game').remove()
            $('.container').append('<button id="newGame" class="btn btn-primary btn-block">New Game</button>')
            $('#newGame').on('click', newGame)
            // $('#submit-guess-btn').click(false)
        }
        TIMER.text(curTime)
    }, 1000))

    $('#submit-guess-btn').on('click', function (evt) {
        evt.preventDefault();
        let guess = $('#user-guess').val()
        $('form').trigger('reset')
        let answerObj = {answer: guess}
        let answerSubmission =  $.ajax({
            type: 'POST',
            url:'/answer',
            data: answerObj,
            success: updateScore
        })
        
    })
    function updateScore (response){
        let currentScore = $('#score').text()
        if (response.result === 'ok') {
            $('#score').text((Number(currentScore)+response.word.length))
        }
    }
    function newGame(){
       let score = Number($('#score').text())
       let final = {high: score}
       let finalObj =  $.ajax({
            type: 'POST',
            url:'/new_game',
            data: final,
        })
    }

})