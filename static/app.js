$('#guess-form').on('submit', async function(e){
    e.preventDefault();
    // console.log($('#guess').val())
    let guess = $('#guess').val()
    if(guess === ''){
        return
    }
    let res = await chackWord(guess)
    checkResponse(res, guess)
    $('#guess').val('')
    console.log(res)
})

function checkResponse(data, val){
    let response = data.response
    if(response == "not-word"){
        $('#flash-msg').text("This is not a word in ower dictionary")
    }else if (response == "not-on-board"){
        $('#flash-msg').text("This is not a word on the board")
    }else if (response == "ok"){
        $('#flash-msg').text("Good Job")
        updateScore(val)
    }
}

function updateScore(str){
    let curScore = parseInt($('#score').text())
    let scoreToAdd = str.length
    let newScore = curScore + scoreToAdd
    $('#score').text(newScore)
}

async function chackWord(data){
    res = await axios.get('http://127.0.0.1:5000/check-awncer', {params: {guess: data}})
    return res.data
}

async function sendScore(data){
    const res = await axios.post('http://127.0.0.1:5000/get-scores', { score: data })
    return res.data
}

let timer = 60

let t = setInterval(async function(){
    $('#timer').text(timer)
    let sesionScore = parseInt($('#score').text())
    
    if(timer === 0){
        clearInterval(t)
        let scoreSend = await sendScore(sesionScore)
        console.log(scoreSend)
    }
    timer -= 1
},1000)