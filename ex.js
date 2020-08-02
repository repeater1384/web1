function PrintTime() {
    var today = new Date();
    var hh = today.getHours();
    var mi = today.getMinutes();
    var ss = today.getSeconds();
    document.getElementById("result").innerHTML = hh + ":" + mi + ":" + ss;
}

// 중지를 위해 ID 보관
var timerId = null;

// 시계 시작
function StartClock() {
    PrintTime();
    timerId = setInterval(PrintTime, 1000);
}
// 시계 중지
function StopClock() {
    if(timerId != null) {
        clearInterval(timerId);
    }
}

var flag = 0
function bling(){
  if (flag === 0) {
    document.querySelector('h1').style.color = '#d6806e';
    flag ++;
  } else if(flag === 1) {
    document.querySelector('h1').style.color = '#fbb666';
    flag ++;
  }else if(flag === 2){
    document.querySelector('h1').style.color = '#f9f871';
    flag ++;
  }else{
    document.querySelector('h1').style.color = '#f2ecff';
    flag = 0;
  }
}
function startTitleConv(){
  setInterval(bling, 1000);
}
