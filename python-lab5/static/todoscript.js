function clickTitle() {
    alert("Ouch!");
}

function warnOnDelete(deletetext) {
    var theDiv = document.getElementById("warning");
    var link = deletetext.href ;
    theDiv.innerText = "Be Careful! " + link;
}

function clearWarning() {
    var theDiv = document.getElementById("warning");
    theDiv.innerText = "";
}