from transformers import BertForSequenceClassification, BertTokenizer
import torch

# Load pre-trained model tokenizer and model
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

def predict_stability(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    predicted_class = torch.argmax(outputs.logits).item()
    if predicted_class == 0:
        return "You seem to be stable."
    else:
        return "You might need to consult a professional for better assistance."

# Example text for assessment
text = "I feel very down and hopeless. I don't see any point in living anymore."

# Predict mental stability using the BERT model
prediction = predict_stability(text)

# Print the prediction
print(prediction)
