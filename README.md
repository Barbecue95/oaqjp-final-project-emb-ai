# Repository for final project

# Emotion Detection System using Watson NLP

A robust, enterprise-grade Python web application deployed using Flask that leverages the IBM Watson Natural Language Processing (NLP) API to analyze text and predict emotional states.

## Features
- **Watson NLP Integration:** Communicates with cloud-based AI infrastructure to extract key metrics.
- **Multi-Emotion Scoring:** Evaluates text payloads across five distinct categories: `anger`, `disgust`, `fear`, `joy`, and `sadness`.
- **Dominant Emotion Identification:** Implements backend algorithmic optimization to instantly extract the primary emotional winner.
- **Robust Error Handling:** Intercepts blank submission states via API `status_code` checks to maintain application runtime stability.
- **Clean Architecture & Compliant Code:** Structured into dedicated distribution packages (`EmotionDetection`) and fully compliant with enterprise standards (scored 10/10 via PyLint).

## Project Architecture
```text
final_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
├── test_emotion_detection.py
└── README.md
