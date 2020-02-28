const keys = document.querySelectorAll(".key"),
    note = document.querySelector(".nowplaying"),
    hints = document.querySelectorAll(".hints");
var map = {}; // You could also use an array
onkeydown = onkeyup = function (e) {
    e = e || event; // to deal with IE
    map[e.keyCode] = e.type == 'keydown';
    /* insert conditional here */
}

var record = {}, startRecordingTime, isRecording = false; //Recording Variables

function startRecording() {
    document.querySelector("#start-record").play();
    record = {'Keys': {}}, isRecording = true;
    startRecordingTime = Date.now();
}

function stopRecording() {
    console.log(record);
    if (!$.isEmptyObject(record)) {
        document.querySelector("#stop-record").play();

        record.TotalTime = Date.now() - startRecordingTime;
        isRecording = false;
        $("#save").removeClass("hidden");
        console.log(record);
    }
}

function save() {

    record['FileName'] = $("#filename").val();
    $.ajax({
        headers: {"X-CSRFToken": $("#csrf").val()},
        url: '/api/record',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
            console.log(data);
            $("#download-modal").modal("hide");
            $("#save").addClass("hidden");
        },
        data: JSON.stringify(record),
    });
}

function playNote(e) {
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`),
        key = document.querySelector(`.key[data-key="${e.keyCode}"]`);
    //Record sound File with time
    if (isRecording) record['Keys'][Date.now() - startRecordingTime] = audio.dataset.audio;

    if (!key) return;
    if(isSaving) return;
    const keyNote = key.getAttribute("data-note");

    key.classList.add("playing");
    note.innerHTML = keyNote;
    audio.currentTime = 0;
    audio.play();
}

function removeTransition(e) {
    if (e.propertyName !== "transform") return;
    this.classList.remove("playing");
}

function hintsOn(e, index) {
    e.setAttribute("style", "transition-delay:" + index * 50 + "ms");
}

hints.forEach(hintsOn);

keys.forEach(key => key.addEventListener("transitionend", removeTransition));

window.addEventListener("keydown", playNote);