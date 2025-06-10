# Chatbot Deployment with Flask and JavaScript

In this tutorial we deploy the chatbot I created in [this](https://github.com/miracl3-dreams/python-chatbot-be) tutorial with Flask and JavaScript.

This gives 2 deployment options:
- Deploy within Flask app 
- Serve only the Flask chatbot API. 

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone https://github.com/miracl3-dreams/python-chatbot-be.git
$ cd chatbot-deployment
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

Now for deployment follow my tutorial to implement `app.py` and `app.js`.

## Watch the Tutorial
[![Alt text](https://img.youtube.com/vi/a37BL0stIuM/hqdefault.jpg)](https://youtu.be/a37BL0stIuM)  
[https://youtu.be/a37BL0stIuM](https://youtu.be/a37BL0stIuM)

## Note
In the video we implement the first approach is to build a Chatbot using Flask app. Only slight modifications are needed to run the frontend separately. 

## Credits:
# python-chatbot-be
