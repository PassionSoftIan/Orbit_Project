from django.shortcuts import render

# Create your views here.
def tetris(request, user_pk):
    return render(request, 'games/tetris.html', context={"user_pk": user_pk})

def snake(request, user_pk):
    return render(request, 'games/snake.html', context={"user_pk": user_pk})

def game_2048(request, user_pk):
    return render(request, 'games/2048.html', context={"user_pk": user_pk})
