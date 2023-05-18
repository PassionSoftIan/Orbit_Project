from django.shortcuts import render

# Create your views here.
def tetris(request):
    return render(request, 'games/tetris.html')

def snake(request):
    return render(request, 'games/snake.html')

def game_2048(request):
    return render(request, 'games/2048.html')
