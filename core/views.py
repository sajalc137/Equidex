from django.shortcuts import render
from .util import get_data

def home(request):
	return render(request, 'core/home.html')

def results(request):
    ticker = request.POST.get('ticker')
    
    # Perform necessary calculations and gather data for the stock ticker
    # Prepare the data to pass to the template
    context = {
        'ticker': ticker,
        'ratios': get_data(ticker)
    }    
    return render(request, 'core/results.html', context)