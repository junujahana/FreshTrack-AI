# 🍎 FreshTrack AI

FreshTrack AI is a demo-ready AI application that predicts the freshness of fruits in real-time. Built as part of the Building AI Application Challenge by Decoding Data Science, this app was created in just 8 days.

It combines pre-trained AI-based fruit recognition with simple storage-based freshness rules to give an easy-to-understand Freshness Score (%).

🚀 Features

Upload an image of a fruit (apple, banana, or orange)

AI detects the fruit type using MobileNetV2 from the Transformers library

Input Days Stored and Storage Type (Room Temperature, Refrigerated, Frozen)

Get an instant Freshness Score (%) with the model’s confidence

Interactive Gradio web interface for instant results

🖥️ Demo

The app is deployed on Hugging Face Spaces. Try it out here:

https://huggingface.co/spaces/junujahana/FreshTrack_AI

🔧 Tech Stack

Python – programming language

Gradio – interactive UI framework

Transformers + MobileNetV2 – pre-trained image classification for fruit detection

Pillow – image processing

📝 How It Works

Upload a fruit image to the app.

The app detects the fruit type and returns a confidence score.

Enter the Days Stored and select the Storage Type:

Room Temperature → freshness decreases faster

Refrigerated → freshness decreases moderately

Frozen → freshness decreases slowly

The app calculates a Freshness Score (%) combining the AI prediction with simple storage-based rules.


💡 Why This Project

FreshTrack AI provides a fast and user-friendly solution for checking fruit freshness.
It’s helpful for consumers, retailers, and supply chain managers to save time, reduce waste, and ensure better fruit quality.

📂 Files Included

app.py – Gradio demo interface

requirements.txt – Python dependencies

README.md – project description


👨‍💻 Author

Junu Jahana
