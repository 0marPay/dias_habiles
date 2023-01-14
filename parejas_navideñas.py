import random 

concursantes = ["Lista", "de", "concursantes", "para", "intercambio", "Navideño"]

def get_random_list(min, max):
    items = [i for i in range(min, max)]
    random.shuffle(items)
    return items

def check_pairs(l1, l2):
    return all([l1[i] != l2[i] for i in range(len(l1))])

def check_equality(l1, l2):
    coincidencia = 0
    l = [[l1[i], l2[i]] for i in range(len(l1))]
    for e in l:
        e.sort()
    for e in l:
        for i in l:
            if i == e: coincidencia += 1
    return coincidencia == len(l)   

carry_on = True
while carry_on:
    dan = [concursantes[i] for i in get_random_list(min=0, max=len(concursantes))]
    reciben = [concursantes[i] for i in get_random_list(min=0, max=len(concursantes))]

    carry_on = check_pairs(dan, reciben) and check_equality(dan,reciben)

    if carry_on: 
        for i in range(len(dan)): 
            print(dan[i],'a',reciben[i])
        print()

    carry_on = not carry_on