from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the tokenizer and model
model_name = "drhyrum/bert-tiny-torch-vuln"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example input: a code snippet or natural language describing code
text = "This function uses eval() on user input."

# Tokenize input
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

# Run inference
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()

# Display result
print(f"Predicted class: {predicted_class}")
