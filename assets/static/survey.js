console.log(userId);

let mainCol = document.getElementById("main-col");

function ajaxPost(url, content, handler) {
    let req = new XMLHttpRequest();
    req.addEventListener('load', handler);
    req.open("post", url);
    req.setRequestHeader("Content-Type", "application/json");
    req.responseType = 'json';
    req.send(JSON.stringify(content));
}

function addElement(parent, etype, className="") {
    let e = document.createElement(etype);
    parent.appendChild(e);
    e.className = className;
    return e;
}

function loadImages() {
    console.log(this.response);
    if (!this.response["success"]) {
        alert(`User ID: ${userId} does not exist!`);
        location.href = "/";
    }
    let header = addElement(mainCol, "h2");
    header.textContent = `User ID: ${userId}`;
    let imageData = this.response["images"];
    for (const [pairId, data] of Object.entries(imageData)) {
        let qval = data["score"];
        loadImage(data["ref"], pairId, qval);
    }
    addSubmitButton();
}

function loadImage(src, pairId, qval) {
    let imgdiv = addElement(mainCol, "div", "row");
    imgdiv.style.margin = "20px";
    let srcdiv = addElement(imgdiv, "div", "col-md-6");
    let imgsrc = addElement(srcdiv, "img");
    imgsrc.setAttribute("src", "/static/images/" + src);
    let scorediv = addElement(imgdiv, "div", "col-md-6");
    let imgscore = addElement(scorediv, "input", "form-input score-box");
    let caption = addElement(scorediv, "small", "form-text text-muted");
    imgscore.setAttribute("id", pairId);
    imgscore.style.marginTop = "20%";
    if (qval != null) {
        imgscore.value = qval;
        caption.textContent = "You already scored this image, modify the value if you want";
    } else {
        caption.textContent = "Score the image";
    }
}

function addSubmitButton() {
    let submit = addElement(mainCol, "button", "btn btn-primary");
    submit.textContent = "SUBMIT";
    submit.style.marginLeft = "60%";
    submit.setAttribute("id", "submitButton")
    submit.addEventListener("click", () => {
        let request = {"userId": userId};
        let results = {}
        let scores = document.getElementsByClassName("score-box");
        for (const score of scores) {
            results[score.getAttribute("id")] = score.value;
        }
        request["results"] = results;
        ajaxPost("/set-user-result", request, clickSubmit);
    });
}

function clickSubmit() {
    if (this.response["success"]) {
        alert("Update Success");
    } else {
        alert("Update Failed");
    }
}

let request = {"userId": userId};
ajaxPost("/get-user-info", request, loadImages);
