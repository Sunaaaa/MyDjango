from django.shortcuts import render, redirect
import requests
from datetime import datetime
from .models import Movie

# Create your views here.
# http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101
def index(request):
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key="fab6fd6434401fd4302d3ebdab8fef88"
    # today = DateFormat(datetime.now()).format('Ymd')
    t = '20191102'



    movie_url = f'{url}?key={key}&targetDt={t}'

    data = requests.get(movie_url).json()
    movies = data.get('boxOfficeResult').get('dailyBoxOfficeList')[:5]
    rank = [ movies[i].get('rank') for i in range(0,5)]
    mname = [ movies[i].get('movieNm') for i in range(0,5)]
    openDt = [ movies[i].get('openDt') for i in range(0,5)]
        

    context = {
        'rank' : rank,
        'mname' : mname,
        'openDt' : openDt,

    }
    return render(request, 'pages/index.html', context)
