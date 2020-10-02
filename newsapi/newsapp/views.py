from django.shortcuts import render
import requests, json

# Create your views here.

def headlines(request):
    headlines = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=e60ee0c37594499aa36b7027cdb262f1')
    headlines_api = json.loads(headlines.content)
    return render(request, 'headlines.html', {'api': headlines_api})

def blockchain(request):
    blockchain = requests.get('http://newsapi.org/v2/everything?q=bitcoin&from=2020-09-02&sortBy=publishedAt&apiKey=e60ee0c37594499aa36b7027cdb262f1')
    blockchain_api = json.loads(blockchain.content)
    return render(request, 'blockchain.html', {'api': blockchain_api})

def business(request):
    business = requests.get('http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e60ee0c37594499aa36b7027cdb262f1')
    business_api = json.loads(business.content)
    return render(request, 'business.html', {'api': business_api})

def apple(request):
    apple = requests.get('https://newsapi.org/v2/everything?q=apple&from=2020-10-01&to=2020-10-01&sortBy=popularity&apiKey=e60ee0c37594499aa36b7027cdb262f1')
    apple_api = json.loads(apple.content)
    return render(request, 'apple.html', {'api': apple_api})

def techcrunch(request):
    techcrunch = requests.get('https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey=e60ee0c37594499aa36b7027cdb262f1')
    techcrunch_api = json.loads(techcrunch.content)
    return render(request, 'blockchain.html', {'api': techcrunch_api})