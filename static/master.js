var divs = ["Oct19", "Oct20", "Oct21", "Oct22", "Oct23", "Oct24", "Oct25"];

var visibleDivId = "Oct19";

var m = [{
  div: "Oct19",
  buId: '1'
}, {
  div: "Oct20",
  buId: '2'
}, {
  div: "Oct21",
  buId: '3'
}, {
  div: "Oct22",
  buId: '4'
}, {
  div: "Oct23",
  buId: '5'
}, {
  div: "Oct24",
  buId: '6'
}, {
  div: "Oct25",
  buId: '7'
}]

function toggleVisibility(divId) {
  if (visibleDivId !== divId) {
    visibleDivId = divId;
  }
  hideNonVisibleDivs();
}

function hideNonVisibleDivs() {
  var i, divId, div;
  for (i = 0; i < divs.length; i++) {
    divId = divs[i];
    div = document.getElementById(divId);
    if (visibleDivId === divId) {
      div.style.display = "block";
      const found = m.find(e => e.div === visibleDivId)
      document.getElementById(found.buId).classList.add("active")
    } else {
      div.style.display = "none";
      const l = m.find(e => e.div === divId)
        document.getElementById(l.buId).classList.remove("active")
    }
  }
}

var Ids = ['1', '2', '3'];

function next() {
  if (Ids[2] !== '7') {
    Ids.shift()
    Ids.push((parseInt(Ids[1]) + 1).toString())
  } else {
    Ids.splice(0, Ids.length)
    Ids = ['1', '2', '3']
  }
  const found=m.find(e=>e.buId===Ids[0])
  toggleVisibility(found.div)
  hideNonVisibleButtons()
}

function prev() {
  if (Ids[0] !== '1') {
    Ids.unshift((parseInt(Ids[0]) - 1).toString())
    Ids.pop()
  } else {
    Ids.splice(0, Ids.length)
    Ids = ['5', '6', '7']
  }
  const found=m.find(e=>e.buId===Ids[0])
  toggleVisibility(found.div)
  hideNonVisibleButtons()
}

function hideNonVisibleButtons() {
  var j, button;
  for (j = 1; j < 8; j++) {
    button = document.getElementById(j.toString());
    if (Ids.includes(j.toString())) {
      button.style.display = "inline";
    } else {
      button.style.display = "none";
    }
  }
}

divSpeaker=["spk1","spk2","spk3","spk4","spk5","spk6","spk7","spk8","spk9","spk10","spk11","spk12","spk13","spk14","spk15"]
activeSpk=["spk1","spk2"]

function next1(){
  if (activeSpk[1]!==divSpeaker[divSpeaker.length-1]) {
    activeSpk.push(divSpeaker[divSpeaker.indexOf(activeSpk[1])+1])
    activeSpk.shift()
  } else {
    activeSpk.splice(0, activeSpk.length)
    activeSpk=["spk15","spk1"]
  }
  SpeakerShow()
}

function prev1(){
if (activeSpk[0]!==divSpeaker[0]) {
    activeSpk.unshift(divSpeaker[divSpeaker.indexOf(activeSpk[0])-1])
    activeSpk.pop()
  } else {
    activeSpk.splice(0, activeSpk.length)
    activeSpk=["spk15","spk1"]
  }
  SpeakerShow()
}

function SpeakerShow(){
  for(let i=0;i<divSpeaker.length;i++){
    let d=document.getElementById(divSpeaker[i])
    if(activeSpk.includes(divSpeaker[i]))
      d.style.display="inline"
    else
      d.style.display="none"
  }
}