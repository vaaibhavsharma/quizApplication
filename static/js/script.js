const answerField = document.getElementById("temp-ans")
const hint = document.getElementById("hint").textContent
const timer = document.querySelector(".timer");

//
var URLL = "{%url 'interval' %}"
var interval =10;
var xx=12

try {
    document.getElementById('buttonHint').addEventListener('click', ()=>{
    iziToast.info({
        title: 'Hint',
        message: hint,
        position: 'bottomCenter',
        timeout: false,
        closeOnClick: true,
        buttons: [
        ['<button>Click to Copy</button>', function (instance, toast) {
             navigator.clipboard.writeText(hint);
        }, true],
    ],
    });
    })
}catch (err){

}



document.querySelector('.check').addEventListener("click", (e) =>{
    if(answerField.value){
        check(e)
    }
});

answerField.addEventListener("keyup", nice)

function nice(e){
    const val = answerField.value

    if (e.keyCode === 13 && val) {
   e.preventDefault();

   check(e);
  }
}
function check(e){
    document.getElementById("button-addon2").style.display === "none";
    let form=$('#answer-form');
    $('#answer-form #id_answer').val($('#temp-ans').val());
    $.ajax({
        type:'POST',
        url: form.attr("action"),
        data:form.serialize(),
        success:function(response){
            const response_div = document.getElementById("response");
            if(response.winner === true){
                location.reload();
            }
            else{
                if(response.correct === true){
                    document.getElementById("button-addon2").disabled = false;
                     iziToast.success({
                        title: 'Correct',
                        message: 'Great, Fetching Your Next Question !',
                     });
                    setTimeout(()=>location.reload(),2000);
                }
                else if(response.correct === false){
                    document.getElementById("button-addon2").disabled = false;
                    if(response.customCode == 20){
                        iziToast.warning({
                            position: 'topRight',
                            title: 'Gift For You!',
                            buttons: [

        ['<button>Click Here</button>', function (instance, toast) {
window.location.replace(response.errorM);
        }, true]
                            ]
                        });

                    }else if(response.customCode == 10){
                        createBalloons(10)
                    }else{
                         iziToast.warning({
                            position: 'topRight',
                            title: 'Incorrect',
                            message: response.errorM,
                     });
                    }



                    $('#answer-form').trigger('reset');
                    $('#temp-ans').val('');
                    setTimeout(()=>response_div.innerHTML="",3000);
                }
                else{
                    iziToast.error({
                        position: 'topRight',
                        message: "Error!",
                     });
                }
            }
        },
        error: function(response){
            console.log(response)
            iziToast.error({
                        pos0ition: 'topRight',
                        message: "Error!",
            });
        }
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function random(num) {
  return Math.floor(Math.random()*num)
}

function getRandomStyles() {
  var r = random(255);
  var g = random(255);
  var b = random(255);
  var mt = random(200);
  var ml = random(50);
  var dur = random(5)+5;
  return `
  background-color: rgba(${r},${g},${b},0.7);
  color: rgba(${r},${g},${b},0.7); 
  box-shadow: inset -7px -3px 10px rgba(${r-10},${g-10},${b-10},0.7);
  margin: ${mt}px 0 0 ${ml}px;
  animation: float ${dur}s ease-in infinite
  `
}

function createBalloons(num) {
  var balloonContainer = document.getElementById("balloon-container")
  for (var i = num; i > 0; i--) {
  var balloon = document.createElement("div");
  balloon.className = "balloon";
  balloon.id = `balloon${i}`
  balloon.style.cssText = getRandomStyles();           balloonContainer.append(balloon);
  }

  setTimeout(deleteballons, 6000);

}

function deleteballons(){
    for (var i = 10; i > 0; i--) {
      var balloon = document.getElementById(`balloon${i}`)
      balloon.remove()
  }
}

function countDownTimer(time){
  
    //var data = {'interval':interval,"X-CSRFToken":csrftoken}
  var URL = "{% url 'timeOut_check' %}"
    let interval =10;
    var countdown = setInterval(()=>{
        time--;
        let timerwidth = time/10*100;
        if(time>0){
            $('.timer').animate({
                width:timerwidth+"vh"
            })
            //timer.style.width = timerwidth+"vh"

        }else{
            clearInterval(countdown);
            timer.style.width = "0vh"
            $.post('timeOut_check/',{
                'interval':0, 
                'csrfmiddlewaretoken':csrftoken
              },)
              setTimeout(()=>location.reload(),0)
        }
  
    },time*100 )
    /*
    $.ajax({
       
        type:"POST",
        url: 'timeOut_check/',
    
        data:{
          'interval': interval, 
          'csrfmiddlewaretoken':csrftoken
        } ,
        
        success: function (response) {
            if (response.result=='ok'){
                alert("response.message")
            }else{
                alert("Failed")
            }
         }
         
    })*/
  
 }
countDownTimer(interval)
