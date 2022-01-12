def game():
    return 770

score=game()
with open("game.txt") as f:
    hiScoreStr=f.read()
if hiScoreStr=='':
    with open("game.txt","w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score:
    with open("game.txt","w") as f:
        f.write(str(score))