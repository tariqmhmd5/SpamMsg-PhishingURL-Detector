# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse
from . import FeatureExtractor
import pickle

def home(request):
    return(render(request,'home.html'))

def classify(request):
    if request.method=='POST':
        url = request.POST['url']

        data = FeatureExtractor.getAttributess(url)
        data = data.values

        model = pickle.load(open('static/SVC_Model.sav', 'rb'))
        predicted_value = model.predict(data)

        if predicted_value==0:
            value="Url is Trusted"
        else:
            value="This is phishing url be aware of it!"
        
        context = {'value':value}
    else:
        return(HttpResponse("404 Not Found"))

    return(render(request,'home.html',context))

def spam(request):
    if request.method=='POST':
        message = request.POST['spam']
        message = message.lower()

        tf = pickle.load(open('static/tfidf.pickle', 'rb'))
        model = pickle.load(open('static/Spam_Classifier.sav', 'rb'))

        data = tf.transform([message])
        #data = data.todense()
        predicted_value = model.predict(data)

        if predicted_value==0:
            value="Not Spam!!"
        else:
            value="Spam Message!!"
        
        context = {'value':value}
    else:
        return(render(request,'spam.html'))

    return(render(request,'home.html',context))