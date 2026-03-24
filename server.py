"""
Flask server for the Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    """
    Recieve text from the web interface, analyze emotion,
    and return the formatted response string.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is:<br><br>"
    f"&nbsp;&nbsp;Anger: {response['anger']}<br>"
    f"&nbsp;&nbsp;Disgust: {response['disgust']}<br>"
    f"&nbsp;&nbsp;Fear: {response['fear']}<br>"
    f"&nbsp;&nbsp;Joy: {response['joy']}<br>"
    f"&nbsp;&nbsp;Sadness: {response['sadness']}<br><br>"
    f"<b>Dominant emotion: {response['dominant_emotion']}</b>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
