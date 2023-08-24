# Dungeon and Dragon

import random

def Ataque(Personaje, Enemigo, D20_Punteria, D12_Suerte):
    Peso_Arma=Personaje['Peso_Arma']
    Fuerza_Arma=Personaje['Arma']
    Aguante_Personaje=Personaje['Aguante']
    Fuerza_Personaje=Personaje['Fuerza']
    Agilidad_Personaje=Personaje['Agilidad']

    Daño= Fuerza_Personaje + Agilidad_Personaje - (Peso_Arma % Aguante_Personaje )

    Aumento= 0
    if Peso_Arma % Fuerza_Arma == 0:
        Aumento = Daño * 0.03
    
    if D20_Punteria % 2 == 0:
        Ataque= Daño +  Aumento
    else:
        Ataque= Daño - Aumento
    
    if D12_Suerte >= 8:
        Enemigo['Escudo']= 0
    
    Aguante_Enemigo = Enemigo['Aguante']
    Agilidad_Enemigo = Enemigo['Agilidad']
    Escudo_Enemigo = Enemigo['Escudo']
    Vida_Enemigo = Enemigo['Vida']

    Defensa= (Aguante_Enemigo * Agilidad_Enemigo) + (Escudo_Enemigo + (Escudo_Enemigo * 0.5))

    Daño_Aplicado= Ataque - Defensa
    
    if Daño_Aplicado < 0:
        Daño_Aplicado= 0

    Enemigo['Vida'] -= Daño_Aplicado

    Enemigo_Muerto = False
    if Enemigo['Vida'] <= 0:
        Enemigo_Muerto = True

    return Daño, Defensa, Enemigo['Vida'], Enemigo_Muerto

Personaje_Elegido=input("Elige una clase de entre: 1) Gladiador, 2) Arquero, 3) Mago: ")
Personaje_Elegido=int(Personaje_Elegido)

#No es necesario definir un Dic en 0 valores de entrada.
""" Personaje = {'Fuerza': 0,
    'Agilidad': 0,
    'Aguante': 0,
    'Arma': 0,
    'Peso_Arma':0} """

Gladiador= {'Fuerza': 40,
    'Agilidad': 10,
    'Aguante': 15,
    'Arma': 90,
    'Peso_Arma': 11}

Arquero= {'Fuerza': 12,
        'Agilidad': 20,
        'Aguante': 10,
        'Arma': 25,
        'Peso_Arma': 14}

Mago= {'Fuerza': 5,
        'Agilidad': 16,
        'Aguante': 8,
        'Arma': 80,
        'Peso_Arma': 4}

if Personaje_Elegido == 1:
    Personaje = Gladiador
elif Personaje_Elegido == 2:
    Personaje = Arquero
elif Personaje_Elegido == 3:
    Personaje = Mago
else:
    raise Exception("INVALIDO")


Enemigo= {'Aguante': 10,
          'Agilidad':1,
          'Escudo': 10,
          'Vida': 15}

print(f"Los Stats de tu clase son: {Personaje}")


Instanc
D20_Punteria= random.randint(1,20)
D12_Suerte= random.randint(1,12)
 
Daño, Defensa, Vida_Enemigo, Enemigo_Muerto = Ataque(Personaje, Enemigo, D20_Punteria, D12_Suerte)

print(f"El Daño Realizado es: {Daño}")
print(f"La Defensa del enemigo es: {Defensa} ")
print(f"La vida del enemigo es de: {Vida_Enemigo}")

if Enemigo_Muerto:
    print("Felicidades, Ganaste!!")
else:
    print("Lo siento, Perdiste!")


