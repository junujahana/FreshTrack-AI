import gradio as gr
from transformers import pipeline

# Load a pre-trained image classification model
classifier = pipeline("image-classification", model="google/mobilenet_v2_1.0_224")

def predict_freshness(image, days_stored, storage_type):
    # Step 1: Classify the fruit
    result = classifier(image)[0]
    fruit = result['label']
    confidence = round(result['score'] * 100, 2)

    # Step 2: Freshness logic (simple simulation)
    base_score = 100
    if storage_type == "Room Temperature":
        freshness = base_score - (days_stored * 15)
    elif storage_type == "Refrigerated":
        freshness = base_score - (days_stored * 5)
    else:  # Frozen
        freshness = base_score - (days_stored * 2)

    freshness = max(0, freshness)  # don’t go below 0

    # Step 3: Return result
    return {
        "Predicted Fruit": fruit,
        "Model Confidence (%)": confidence,
        "Freshness Score (%)": freshness
    }

# Gradio interface
demo = gr.Interface(
    fn=predict_freshness,
    inputs=[
        gr.Image(type="pil", label="Upload Fruit Image"),
        gr.Slider(0, 20, step=1, value=2, label="Days Stored"),
        gr.Radio(["Room Temperature", "Refrigerated", "Frozen"], label="Storage Type", value="Room Temperature")
    ],
    outputs="json",
    title="🍎 FreshTrack AI",
    description="Upload an image of a fruit and get an estimated freshness score."
)

if __name__ == "__main__":
    demo.launch()
