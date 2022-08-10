from flask import Flask
from flask import request, jsonify, render_template
from src.dao import *


app = Flask(
    __name__,
    static_url_path='/static',
    static_folder="../../assets/static",
    template_folder="../../assets/template"
)
FAILED_RESPONSE = {"success": False}


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/survey", methods=["GET"])
def survey_page():
    user_id = request.args.get('userId', '')
    data = {"userId": user_id}
    return render_template("survey.html", data=data)


@app.route("/get-user-info", methods=["POST"])
def get_user_info():
    user_id = request.get_json()["userId"]
    dao = get_dao()
    user = dao.find_item(User(user_id=user_id))
    if user is None:
        return jsonify(FAILED_RESPONSE)
    user_images = dao.get_items(UserImage, {"user_id": user_id})
    response = {"success": True}
    images = {ui.pair_id: {"ref": ui.ref, "score": ui.score} for ui in user_images}
    response.update(user.row_tuple)
    response["images"] = images
    return jsonify(response)


@app.route("/set-user-result", methods=["POST"])
def set_user_result():
    request_obj = request.get_json()
    print(request_obj)
    # Validate
    user_id = request_obj["userId"]
    results = request_obj["results"]
    dao = get_dao()
    for pair_id, score in results.items():
        if not score:
            continue
        try:
            score = int(score)
            if score < 0 or score > 100:
                raise
        except:
            return jsonify(response)
        ui = dao.find_item(UserImage(pair_id=pair_id))
        ui.score_result(score)
        dao.update_item(ui)
    user = dao.find_item(User(user_id=user_id))
    user.complete()
    dao.update_item(user)
    return jsonify({"success": True})


def run_server():
    app.run(debug=True, host="0.0.0.0", port=5001)
