from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def get_emotion_detection():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response is not None:
        anger = response["anger"]
        disgust = response["disgust"]
        fear = response["fear"]
        joy = response["joy"]
        sadness = response["sadness"]
        dominant_emotion = response["dominant_emotion"]

        if dominant_emotion is None:
            return "Invalid text! Please try again!"

        return_txt = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

        return return_txt
    return "Sorry, please try later again!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
