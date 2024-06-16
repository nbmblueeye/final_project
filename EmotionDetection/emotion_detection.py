import json
import requests

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    try:
        # Fetching data from Server
        response = requests.post(url, headers=headers, json=input_json)

        # Return None if empty input
        if response.status_code == 400:
            response_none = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None,
                'message': 'Empty text provided'
            }
            return (response_none), response.status_code

        result = response.json()
        emotion_predictions = result.get('emotionPredictions',[])

        # Add text to text_to_analyze
        ## Check if emotion_predictions, the list is not empty
        if emotion_predictions and 'emotionMentions' in emotion_predictions[0]:
            emotion_mentions = emotion_predictions[0]['emotionMentions']
            text = emotion_mentions[0]['span']['text']  # Access the 'text' field

            ## Convert the response text into a dictionary using the json library functions.
            text_dictionary = json.dumps({'text': text})
        
            ## Extract the required set of emotions, including anger, disgust, fear, joy and sadness
            emotions = emotion_mentions[0]['emotion']

            ## Find the dominant emotion based on the highest score
            dominant_emotion = max(emotions, key=emotions.get)
        
            ## Add dominant_emotion to the emotion dictionary
            emotions['dominant_emotion'] = dominant_emotion
            print(emotions)
            return emotions, response.status_code
    
    except requests.exceptions.RequestException as e:
        response_none = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'message': f'Request error: {str(e)}'
        }
        return response_none, response.status_code  
  