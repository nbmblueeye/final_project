from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

# Define the template directory
app = Flask(__name__)

@app.route("/emotionDetector", methods=['GET'])
def detect_emotion():
    # Get text to analyze from User
    text_to_analyze = request.args.get('textToAnalyze')

    # Get response Data from Server
    emotions = emotion_detector(text_to_analyze)
    
    # Check for response with None value
    if emotions["dominant_emotion"] == None:
        responseText = "Invalid text! Please try again!."
        return responseText
    else:
        response = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": emotions["dominant_emotion"]
        }

        # Create result response text
        responseText = f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}." 
        return responseText

@app.route("/")
def index():
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)