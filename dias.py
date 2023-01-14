import datetime
from datetime import date
import time

def input_date():
    d = input()
    if d != '':
        try:
            d = d.split(',')
            d = [int(i) for i in d]
        except:
            print('Ingrese fechas en un formato correcto.')    
            print('Pulse ENTER para terminar.')
            input()
        try: 
            date(d[0], d[1], d[2])
        except:
            print('Las fechas no pueden procesarse.')
            print('Pulse ENTER para terminar.')
            input()
        return date(d[0], d[1], d[2])
    else:
        d = date.today()
        return date(d.year, d.month, d.day)
        


def dias_habiles():
    '''
    Función para contar la cantidad de días hábiles entre dos fechas establecidas.
    PRUEBA DE CONCEPTO
    
    d0 - fecha inicial
    d1 - fecha final
    
    '''
    
    # Ingresamos las fechas con la función
    print('Ingrese la primera fecha:')
    d0 = input_date()
    print()
    print('Ingrese la segunda fecha:')
    print('Para la fecha actual, presione ENTER')
    d1 = input_date()

    
    # Primero nos aseguramos de que la primera fecha sea menor a la segunda
    if d0>d1:
        print("La fecha ingresada debe anterior a la fecha actual")
        print('Pulse ENTER para terminar.')
        input()

    
    # Declaramos los días de vacaciones que son oficialemnte inhábiles en México. Esto se debe actualizar para años posteriores. 
    # https://mexico.justia.com/federales/leyes/ley-federal-del-trabajo/titulo-tercero/capitulo-iii/
    #                AÑO  MES DÍA         AÑO  MES DÍA
    Holidays = [date(2021, 1 , 1 ),  date(2022, 1 , 1 ), # I. El 1o. de enero;
                date(2021, 2 , 1 ),  date(2022, 2 , 7 ), # II. El primer lunes de febrero en conmemoración del 5 de febrero;
                date(2021, 3 , 15),  date(2022, 3 , 21), # III. El tercer lunes de marzo en conmemoración del 21 de marzo;
                date(2021, 5 , 1 ),  date(2022, 5 , 1 ), # IV. El 1o. de mayo;
                date(2021, 9 , 16),  date(2022, 9 , 16), # V. El 16 de septiembre;
                date(2021, 11, 15),  date(2022, 11, 21), # VI. El tercer lunes de noviembre en conmemoración del 20 de noviembre;
                date(2021, 12, 25),  date(2022, 12, 25), # VIII. El 25 de diciembre
               ] # VII. El 1o. de diciembre de cada seis años, cuando corresponda a la transmisión del Poder Ejecutivo Federal;

    
    # Creamos una función complementaria para calcular la cantidad de días netos entre ambas fechas
    def total_dias(d0, d1):
        return (d1 - d0).days

    # La variable _habiles_ comienza en 0 y va aumentando (+1) cada día que sea hábil (<6 / 6=sábado & NO Holiday) 
    habiles = 0
    for i in range(total_dias(d0, d1)):
        fecha_actual = d0 + datetime.timedelta(days=i+1)
        if (fecha_actual.weekday()+1 < 6) and (fecha_actual not in Holidays):
            habiles = habiles + 1
    
    # Y damos como resultado el valor final de la variable hábiles
    print()
    print('Los días hábiles entre el', d0, 'y el', d1,'son', habiles, 'días.')
    return habiles

if __name__ == "__main__":
    while True:
        print('CALCULAR DÍAS HÁBILES')
        print('Formato de fechas AAAA, MM, DD')
        print()
        dias_habiles()
        print()
        print('------------------------------------------------------------------')
        print()
        time.sleep(3)