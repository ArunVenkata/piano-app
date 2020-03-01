const keys = document.querySelectorAll(".key"),
    note = document.querySelector(".nowplaying"),
    hints = document.querySelectorAll(".hints");
var map = {}; // You could also use an array
onkeydown = onkeyup = function (e) {
    e = e || event; // to deal with IE
    map[e.keyCode] = e.type === 'keydown';
    /* insert conditional here */
};

var record = {}, startRecordingTime, isRecording = false; //Recording Variables
var mediaRecorder;

function startRecording() {
    var startRecordingAudio = document.querySelector("#start-record");
    startRecordingAudio.addEventListener("ended", function () {
        startRecordingAudio.currentTime = 0;
        mediaRecorder.start();
        startRecordingTime = Date.now();
    });
    startRecordingAudio.play();
    record = {'Keys': {}}, isRecording = true;
}

function stopRecording() {
    console.log(record);
    if (!$.isEmptyObject(record)) {
        mediaRecorder.stop();
        record.TotalTime = Date.now() - startRecordingTime;
        document.querySelector("#stop-record").play();
        isRecording = false;
        $("#save").removeClass("hidden");
        console.log(record);
    }
}

function save() {
    record['FileName'] = $("#filename").val();
    record['Audio'] = mediaAudioBase64;
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
    if (isSaving) return;
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

navigator.mediaDevices.getUserMedia({audio: true})
    .then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        var reader = new window.FileReader();
        var audioChunks = [];
        mediaRecorder.addEventListener("dataavailable", event => {
            audioChunks.push(event.data);
            console.log(mediaRecorder.audioBitsPerSecond)
        });

        mediaRecorder.addEventListener("stop", () => {
            const audioBlob = new Blob(audioChunks, {'type': 'audio/wav'});
            audioChunks = [];
            reader.readAsDataURL(audioBlob);
            reader.onloadend = function () {
                mediaAudioBase64 = reader.result;
                mediaAudioBase64 = mediaAudioBase64.split(',')[1];
                console.log(mediaAudioBase64);
            }
        });

    });