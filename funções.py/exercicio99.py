import time

def maior(* num):
    cont = maior = 0
    for v in num:
        print(f'{v} ', end='', flush=True)
        time.sleep(0.5)
        if cont == 0:
            maior = cont
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f"\nForam informados {cont} valores")
    print(f"O maior valor foi o valor {maior}")

def maior2(* max_value):
    maior = max(max_value)
    print(maior)

#programa princial:
maior(1, 2, 3, 4, 5)
maior2(1, 2, 3, 4, 10, 45)