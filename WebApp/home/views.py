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