from django.http import HttpResponse
from django.shortcuts import render
import operator
import string


def home(request):
    return render(request, 'home.html', )
def count(request):
    fulltext = request.GET['fulltext']

    #Deletes empty spaces in fulltext and save it as wordlist
    wordlist = fulltext.split()
    
    #Declare an empty list
    worddictionary = {}

    #For each word in wordlist, if exist in list add 1, if not, add it to list
    for word in wordlist:
        word = word.lower()
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    #Sort list from highest occurence to least
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,
    'count':len(wordlist), 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html',)
    