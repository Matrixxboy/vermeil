from transformers import pipeline

intent_classifier = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiment")

result = intent_classifier("Can you tell me a joke?")
print(result)  # Example Output: [{'label': 'joke', 'score': 0.95}]
