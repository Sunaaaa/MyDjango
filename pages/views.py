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
    dt = datetime.now()
    today = str(dt.year) + str(dt.month) + str(dt.day-1)
    print(today)
#    t = '20191212'



    movie_url = f'{url}?key={key}&targetDt={today}'

    data = requests.get(movie_url).json()
    movies = data.get('boxOfficeResult').get('dailyBoxOfficeList')[:5]
    rank = [ movies[i].get('rank') for i in range(0,5)]
    movieCd = [ movies[i].get('movieCd') for i in range(0,5)]
    mname = [ (movies[i].get('movieNm'), movies[i].get('rank')) for i in range(0,5)]
    openDt = [ movies[i].get('openDt') for i in range(0,5)]
        

    context = {
        'movies' : movies,
        'movieCd' : movieCd,
        'rank' : rank,
        'mname' : mname,
        'openDt' : openDt,

    }
    return render(request, 'pages/index.html', context)

def detail(request):
    print('DETAIL')
    context = {

    }
    return render(request, 'pages/detail.html', context)