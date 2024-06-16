"""
Server for Emotion Detection using Flask
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

# Define the template directory
app = Flask(__name__)

@app.route("/emotionDetector", methods=['GET'])
def detect_emotion():
    """
        Flask route to detect emotion from the provided text.

        Returns: responseText with emotion analysis and dominant emotion.
    """
    # Get text to analyze from User
    text_to_analyze = request.args.get('textToAnalyze')
    # Get response Data from Server
    emotions = emotion_detector(text_to_analyze)

    # Check for response with None value
    if emotions['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again!."
        return response_text

    response = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": emotions["dominant_emotion"]
    }
    # Create result response text
    response_text = (
            f"For the given statement, the system response is:\n"
            f"'anger': {response['anger']},\n"
            f"'disgust': {response['disgust']},\n"
            f"'fear': {response['fear']},\n"
            f"'joy': {response['joy']} and\n"
            f"'sadness': {response['sadness']}.\n"
            f"The dominant emotion is {response['dominant_emotion']}."
        )
    return response_text

@app.route("/")
def index():
    """
        Flask route for the home page.

        Returns: Rendered HTML template for the home page.
    """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
