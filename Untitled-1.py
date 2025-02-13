ans=int(input("ingrese numero a convertir a romano: "))

if ans<= 9:
    if ans<=3:
        resultado=ans*"I"
        print(resultado)
    if ans==4:
        resta=5-ans
        resultado1=resta*"I"
        print(resultado1,"V")
    if ans>=5:
        resta=ans-5
        resultado1=resta*"I"
        print("V",resultado1)
elif ans>9:
    print("Ingrese un numero valido")