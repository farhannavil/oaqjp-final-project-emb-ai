import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }   
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        # Parse the response text into a dictionary
        response_dict = json.loads(response.text)
        
        # Extract the emotions and their scores
        emotions = response_dict["emotionPredictions"][0]["emotion"]
        
        # Find the dominant emotion (emotion with the highest score)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Prepare the final dictionary
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        return result
    elif response.status_code == 400:
        # Handle blank input by returning None for all keys
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    else:
        return f"Error: {response.status_code}, {response.text}"
