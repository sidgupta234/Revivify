from django.shortcuts import render
import requests
from django.http import HttpResponse
import unicodedata
# Create your views here.
def home(request):

	return render(request,"sample.html");

def index(request):
	 print "i was called"
	 if(request.GET.get('q', '')):
	 	theUrl="http://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&titles="+request.GET.get('q', '')
	 	r = requests.get(theUrl, auth=('user', 'pass'));
	 	print r.text
	 	return HttpResponse(r.text, content_type='hacko/json')
	 elif(request.GET.get('p', '')):
	 	theUrl="https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles="+request.GET.get('p', '')
	 	r = requests.get(theUrl, auth=('user', 'pass'));
	 	print r.text
	 	return HttpResponse(r.text, content_type='hacko/json')
	 else:
	 	key="f7ee811c-3f3d-47b4-ad77-b31fe1831b2f"
	 	r="http://www.dictionaryapi.com/api/v1/references/thesaurus/xml/"+request.GET.get('r', '')+"?key="+key
	 	r=requests.get(r);
	 	r=r.text
	 	r=unicodedata.normalize('NFKD', r).encode('ascii','ignore')
	 	return HttpResponse(r,content_type="text/plain")

	 