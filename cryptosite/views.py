import json

import requests
from django.shortcuts import render


def home(request):
    # Grab Crypto Price
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?"
                                 "fsyms=BTC,XRP,ETH,XBT,NMC,STC,BCN,PPC,DOGE,XDG,FTC,GRC,XPM,NXT,"
                                 "AUR,DASH,NEO,MZC,XMR,XEM,POT,AMP,TIT,XVG,XLM,VTC,ETC,USDT,DCR,"
                                 "WAVES,ZEC,BCC,BCH,EOS,ADA,BTCP&tsyms=USD,EUR")
    price = json.loads(price_request.content)
    # Grab Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        quote = request.POST.get('quote')
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="
                                      + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
    else:
        notfound = "Enter the crypto currency symbol in the form above ...."
        return render(request, 'prices.html', {'notfound': notfound})
