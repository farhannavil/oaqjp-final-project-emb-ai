"""
server.py

This module sets up a Flask web application to detect emotions
from user input and return the results as JSON responses.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

# Initialize Flask application
app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Handle POST requests to detect emotions from user input.

    Returns:
        JSON response with the detected emotions or an error message 
        for invalid input.
    """
    text_to_analyze = request.form.get('text')
    result = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None
    if result['dominant_emotion'] is None:
        response = "Invalid text! Please try again!"
    else:
        response = (f"For the given statement, the system response is "
                    f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                    f"'fear': {result['fear']}, 'joy': {result['joy']} and "
                    f"'sadness': {result['sadness']}. The dominant emotion is "
                    f"{result['dominant_emotion']}.")

    return jsonify({"response": response})

@app.route('/')
def index():
    """
    Render the index.html template for the main page.

    Returns:
        Rendered HTML template.
    """
    return render_template('index.html')

if __name__ == '__main__':
    """
    Run the Flask application on localhost:5000.
    """
    app.run(host='localhost', port=5000, debug=True)
