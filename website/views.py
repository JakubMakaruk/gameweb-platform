import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count, Avg
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from .models import Rate, Comment
import requests
from .classes import RankingGame, DetailGame


# Create your views here.


def home(request):
    if request.method == 'GET':
        login_form = LoginForm()
        register_form = RegisterForm()
        usernames = User.objects.values_list('username', flat=True)
        usernames_json = json.dumps(list(usernames), cls=DjangoJSONEncoder)
        emails = User.objects.values_list('email', flat=True)

        context = {
            'login_form': login_form,
            'register_form': register_form,
            'usernames': usernames_json
        }

        return render(request, 'index.html', context)


def loginPage(request):
    if request.method == 'POST':
        if 'loginLogin' in request.POST:
            username = request.POST['loginLogin']
            password = request.POST['passwordLogin']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request=request, user=user)
                messages.success(request, "Logged in succesfully.")
                return redirect('home')
            else:
                messages.error(request, "Incorrect username or password.")
                return redirect('home')
    return render(request, 'index.html', {})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('')

def registerPage(request):
    if 'loginRegister' in request.POST:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            login = register_form.cleaned_data['loginRegister']
            email = register_form.cleaned_data['emailRegister']
            password = register_form.cleaned_data['passwordRegister']
            repeatPassword = register_form.cleaned_data['repeatPasswordRegister']

            if password == repeatPassword:
                user = User.objects.create_user(username=login,
                                                email=email,
                                                password=password)
        return redirect('home')

        users = User.objects.all()
        context = {
            'users': users,
        }


        return render(request, 'index.html', context)


def forum(request):
    return render(request, 'forum.html', {})


def ranking(request):
    ranking_games = Rate.objects.values('game_id').annotate(rate=Avg('value'), count_rates=Count('value')).order_by(
        '-rate', '-count_rates')[:10]

    temp_games = get_games(ranking_games)
    covers = get_cover(temp_games)

    games = []

    for index, game in enumerate(temp_games):
        games.append(RankingGame(index+1,
                          temp_games[index].get('id'),
                          temp_games[index].get('name'),
                          "{:.1f}".format(ranking_games[index].get('rate')),
                          ranking_games[index].get('count_rates'),
                          covers[index].replace('t_thumb', 't_logo_med')))


    context = {
        'games': games
    }

    return render(request, 'ranking.html', context)



def search(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        headers = {'Client-ID': '5mxvhx4wsmpqqere91pcd3ula4vec6', 'Authorization': 'Bearer ' 'u8m7oulqxfj8g0yg4f0t3a9z43h1p8'}

        data = 'fields id; where name="' + title + '";'

        r = requests.post('https://api.igdb.com/v4/games', data=data, headers=headers)


        if len(r.json()) > 0:
            response_game_id = r.json()[0].get('id')

            return redirect('gameDetails', response_game_id)

    return render(request, 'searchGame.html', {})




def gameDetails(request, pk):
    headers = {'Client-ID': '5mxvhx4wsmpqqere91pcd3ula4vec6', 'Authorization': 'Bearer u8m7oulqxfj8g0yg4f0t3a9z43h1p8'}

    data = 'fields id, name, cover, genres, platforms, summary, release_dates; where id=' + str(pk) + ';'

    r = requests.post('https://api.igdb.com/v4/games', data=data, headers=headers)
    response_game = r.json()[0]

    if Rate.objects.filter(game_id=response_game.get('id')):
        game_rate = Rate.objects.values('game_id').annotate(rate=Avg('value'), count_rates=Count('value')).filter(game_id=response_game.get('id'))[0]
    else:
        game_rate = { 'rate': 0, 'count_rates': 0 }
    cover = get_cover([response_game])[0]
    genres = get_genres(response_game)
    platforms = get_platforms(response_game)
    release_date = get_releaseDate(response_game)
    summary = response_game.get('summary')


    game = DetailGame(response_game.get('id'),
                      response_game.get('name'),
                      "{:.1f}".format(game_rate.get('rate')),
                      game_rate.get('count_rates'),
                      cover.replace('t_thumb', 't_cover_big'),
                      genres,
                      platforms,
                      release_date,
                      summary)

    if Comment.objects.filter(game_id=pk):
        comments = Comment.objects.filter(game_id=pk).order_by('-date')
    else:
        comments = {}


    context = {
        'game': game,
        'comments': comments
    }


    return render(request, 'gameDetails.html', context)


def addRate(request, pk):
    new_rate = Rate.objects.create(author=request.user, game_id=pk, value=request.POST.get('rate-value'))
    new_rate.save()
    print(new_rate)
    print(request.POST)
    return redirect('gameDetails', pk)

def addComment(request, pk):
    new_comment = Comment.objects.create(author=request.user, game_id=pk, content=request.POST.get('comment-text'))
    new_comment.save()
    return redirect('gameDetails', pk)



def get_games(ranking_games):
    headers = {'Client-ID': '5mxvhx4wsmpqqere91pcd3ula4vec6', 'Authorization': 'Bearer u8m7oulqxfj8g0yg4f0t3a9z43h1p8'}

    ids = ""
    for index, game in enumerate(ranking_games):
        if index != len(ranking_games)-1:
            ids += str(game.get('game_id')) + ", "
        else:
            ids += str(game.get('game_id'))

    data = 'fields id, name, cover; where id=(' + ids + ');'

    r = requests.post('https://api.igdb.com/v4/games', data=data, headers=headers)
    temp_games = r.json()

    games = []
    for index in range(0, len(ranking_games)):
        games.append(next((temp_games[i] for i in range(0, len(temp_games))
                           if temp_games[i].get('id') == ranking_games[index].get('game_id')), None))

    return games

def get_cover(games):
    headers = {'Client-ID': '5mxvhx4wsmpqqere91pcd3ula4vec6', 'Authorization': 'Bearer u8m7oulqxfj8g0yg4f0t3a9z43h1p8'}

    ids = ""
    for index, game in enumerate(games):
        if index != len(games) - 1:
            ids += str(game.get('cover')) + ", "
        else:
            ids += str(game.get('cover'))

    data = 'fields id, url; where id=(' + ids + ');'

    r = requests.post('https://api.igdb.com/v4/covers', data=data, headers=headers)
    temp_covers = r.json()

    covers_url = []
    for index in range(0, len(games)):
        covers_url.append(next((temp_covers[i].get('url') for i in range(0, len(temp_covers))
                                if temp_covers[i].get('id') == games[index].get('cover')), None))

    return covers_url

def get_genres(game):
    headers = {'Client-ID': '5mxvhx4wsmpqqere91pcd3ula4vec6', 'Authorization': 'Bearer u8m7oulqxfj8g0yg4f0t3a9z43h1p8'}

    ids = ','.join(str(x) for x in game.get('genres'))

    data = 'fields name; where id=(' + ids + ');'

    r = requests.post('https://api.igdb.com/v4/genres', data=data, headers=headers)
    temp_genres = r.json()

    genres = ""
    for index, genre in enumerate(temp_genres):
        if index != len(temp_genres) - 1:
            genres += genre.get('name') + ", "
        else:
            genres += genre.get('name')

    return genres

def get_platforms(game):
    headers = {'Client-ID': '5mxvhx4wsmpqqere91pcd3ula4vec6', 'Authorization': 'Bearer u8m7oulqxfj8g0yg4f0t3a9z43h1p8'}

    ids = ','.join(str(x) for x in game.get('platforms'))

    data = 'fields abbreviation; where id=(' + ids + ');'

    r = requests.post('https://api.igdb.com/v4/platforms', data=data, headers=headers)
    temp_platforms = r.json()

    platforms = ""
    for index, genre in enumerate(temp_platforms):
        if index != len(temp_platforms) - 1:
            platforms += genre.get('abbreviation') + ", "
        else:
            platforms += genre.get('abbreviation')

    return platforms

def get_releaseDate(game):
    headers = {'Client-ID': '5mxvhx4wsmpqqere91pcd3ula4vec6', 'Authorization': 'Bearer u8m7oulqxfj8g0yg4f0t3a9z43h1p8'}

    ids = str(game.get('release_dates')[0])

    data = 'fields human; where id=(' + ids + ');'

    r = requests.post('https://api.igdb.com/v4/release_dates', data=data, headers=headers)
    temp_releaseDate = r.json()[0].get('human')

    return temp_releaseDate

