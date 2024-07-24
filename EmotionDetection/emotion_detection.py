import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, headers=headers, json=json)

        data = json.loads(response.text)

        if response.status_code == 400:
            result = {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }

        anger_score = data["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = data["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = data["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = data["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = data["emotionPredictions"][0]["emotion"]["sadness"]

        emotion_scores = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        dominant_emotion_idx = emotion_scores.index(max(emotion_scores))
        dominant_emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
        dominant_emotion = dominant_emotion_keys[dominant_emotion_idx]

        result = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion
        }

        return result
    except Exception as e:
        print(f"Failed: {e}")
        return None
