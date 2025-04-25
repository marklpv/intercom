from flask import Flask, request
import os

app = Flask(__name__)

VMSG_FOLDER = "vmsg"

@app.route("/vmsg", methods=["POST"])
def play_vmsg():
    vmsg = request.form["vmsg"]
    filename = f"{vmsg}"
    filepath = os.path.join(VMSG_FOLDER,filename)
    if os.path.isfile(f"{filepath}.mp3"):
        filepath = f"{filepath}.mp3"
    elif os.path.isfile(f"{filepath}.wav"):
        filepath = f"{filepath}.wav"
    else:
        return "No audio file found.", 400
    os.system(f"mpg123 {filepath}")
    return "Played", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10333)