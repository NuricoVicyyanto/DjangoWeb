import playsound
def alert():
    i=1
    while i < 6:
        alert = playsound.playsound('alert.mp3')
        print(alert)
        if i == 3:
            break
        i +=1

alert()