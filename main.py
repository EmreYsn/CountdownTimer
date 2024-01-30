import time

def countdown(t):
    while t:
        dakika,saniye = divmod(t,60)
        zamanlayıcı = '{:02d}:{:02d}'.format(dakika,saniye)
        print(zamanlayıcı,end="\r")
        time.sleep(1)
        t -= 1
    print('Zaman doldu')

t = input("Saati saniye cinsinden girin:")

countdown(int(t))
