import time

def timer(tempo):
    while tempo > 0:
        min = int(tempo/60)
        seg = int(tempo%60)
        tempos = f'{min}:{seg}'
        print(tempos, end='\r')
        time.sleep(1)
        tempo -= 1
    print("Tempo esgotado")    

tempo = input("Digite o tempo em segundos ")

timer(int(tempo))