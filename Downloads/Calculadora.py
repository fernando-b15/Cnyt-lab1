from sys import stdin
import math
def main():
    inicio()

def inicio():
    global num1
    global num2
    num1=list(stdin.readline().split())
    num2=list(stdin.readline().split())
    ope=stdin.readline().strip()
    print(ope)
    if ope=='suma':
        sumar()
    elif ope=='resta':
        restar()
    elif ope=='multiplicacion':
        multiplicar(int(num1[0]),int(num1[1]),int(num2[0]),int(num1[1]))
    elif ope=='division':
        dividir()
    elif ope=='fase polar':
        print("escriba 1 o 2 dependiendo del numero del operador que desea convertir: ")
        tem=int(stdin.readline())
        if tem==1:
            fase_polar(int(num1[0]),int(num1[1]))
        else:
            fase_polar(int(num2[0]),int(num1[1]))
    elif ope=='cartesiano a polar':
        print("escriba 1 o 2 dependiendo del numero del operador que desea convertir: ")
        tem=int(stdin.readline())
        if tem==1:
            cartesiano_polar(int(num1[0]),int(num1[1]))
        else:
            cartesiano_polar(int(num2[0]),int(num1[1]))       
def sumar():
    n1=int(num1[0])
    n2=int(num1[1])
    n3=int(num2[0])
    n4=int(num2[1])
    res=[]
    res.append(n1+n3)
    res.append(n2+n4)
    print(res)

def restar():
    n1=int(num1[0])
    n2=int(num1[1])
    n3=int(num2[0])
    n4=int(num2[1])
    res=[]
    res.append(n1-n3)
    res.append(n2-n4)
    print(res)
def multiplicar(n1,n2,n3,n4):
    pe=[]
    pc=[]
    pe.append(n1*n3)
    pe.append(-1*n2*n4)
    pc.append(n2*n3)
    pc.append(n1*n4)
    res=[]
    res.append(sum(pe))
    res.append(sum(pc))
    print(res)
    return res
def dividir():
    n1=int(num1[0])
    n2=int(num1[1])
    n3=int(num2[0])
    n4=int(num2[1])
    cont=conjugado(n3,n4)
    r1=multiplicar(n1,n2,cont[0],cont[1])
    r2=multiplicar(n3,n4,cont[0],cont[1])
    res=[round((r1[0]/r2[0]),3),round((r1[1]/r2[0]),3)]
    print(res)
def conjugado(n1,n2):
    res=[]
    res.append(n1)
    res.append(n2*-1)    
    return res
def modulo(n1,n2):
    res=((n1**2)+(n2**2))**(1/2)
    return res
def fase_polar(n1,n2):
    if 0<=n1 and 0<=n2:
        res=round(math.degrees(math.atan(n2/n1)),0)
        print(res)
        return res
    elif n1<0 and 0<=n2:
        res=180+round(math.degrees(math.atan(n2/n1)),0)
        print(res)
        return res
    elif n1<0 and n2<0:
        res=180+round(math.degrees(math.atan(n2/n1)),0)
        print(res)
        return res
    else:
        res=360+round(math.degrees(math.atan(n2/n1)),0)
        print(res)
        return res
def cartesiano_polar(n1,n2):
    res=[modulo(n1,n2),fase_polar(n1,n2)]
    print(res)
    return res
main()

    
