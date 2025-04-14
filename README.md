---
title: LanggraphAgenticAI
emoji: 🐨
colorFrom: blue
colorTo: red
sdk: streamlit
sdk_version: 1.42.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: Refined langgraphAgenticAI
---

### End To End Agentic AI Projects

The project is in development

Basic chat bot and chatbot with tools 

# Basic Chatbot

A simple chatbot implementation demonstrating fundamental conversational AI principles.

![Basic Chatbot Demo](assets\basicChatbot.png)
![Chatbot with tool](assets\chatbotwithTool.png)

## Overview

This project provides a basic chatbot and chatbot with tools that can respond to user input based on predefined rules or a simple pattern-matching algorithm. It's designed as a starting point for understanding chatbot development and can be easily extended.

## Features

* **Simple Input Processing:** Takes text input from the user.
* **Rule-Based Responses:** Generates responses based on predefined rules or patterns.
* **Basic Conversation Flow:** Maintains a simple conversational context (e.g., remembering the user's name).
* **Easy to Understand Code:** The codebase is designed to be clear and well-commented for learning purposes.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Installation

1.  Clone the repository:
    ```bash
    git clone [git@github.com:Abhipise81/Chatbot.git](https://github.com/Abhipise81/Chatbot)
    cd Chatbot
    ```
2.  Create a virtual environment:
    ```bash
    conda create -p venv python==3.12
    conda activate venv/
    ```
3.  Install any required dependencies (if any are listed in a `requirements.txt` file):
    ```bash
    pip install -r requirements.txt
    ```

### Running the Chatbot

Execute the main script:

```bash
streamlit run app.py
```

### Additional Notes.

For using chatbot we require GROQ_API_KEY an to get some data that is not inside the LLM we need to do 
google search for that we are using travily_api_key. You will get this option in streamlit userinterface.

