import time

inicio = time.time()


while True:
    fim = time.time()
    if (fim-inicio>=20):
        print(fim-inicio)
        break