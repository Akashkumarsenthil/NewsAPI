from django.shortcuts import render
import requests, json

# Create your views here.

def index(request):
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