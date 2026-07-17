from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route("/emotionDetector")
def sentiment_analyzer():
    ''' get a text from an HTML interface and run the emotion analysis.'''
    text_to_analyze = request.args.get('textToAnalyze')
    
    # pass the text to the previously created function
    response = emotion_detector(text_to_analyze)
    
    # Extract dict variables
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Formatea la respuesta en el texto exacto requerido
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' render the index.html.'''
    return render_template('index.html')

if __name__ == "__main__":
    # Execute the server on port 5000
    app.run(host="0.0.0.0", port=5000)