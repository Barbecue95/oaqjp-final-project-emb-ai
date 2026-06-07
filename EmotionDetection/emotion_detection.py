import json
import requests

def emotion_detector(text_to_analyze):
    # The dedicated IBM Cloud URL endpoint for Emotion Prediction
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the payload object matching the target schema
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Setting the specific English stock model ID requested in Task 2 criteria
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Executing the request POST
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse the response text string into a Python dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the nested emotion dictionary from the Watson payload
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Isolate individual emotion keys
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Dynamically find the emotion key with the absolute highest score
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the clean structured output required by Task 3
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }