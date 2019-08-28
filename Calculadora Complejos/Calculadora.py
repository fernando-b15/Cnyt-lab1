from sys import stdin
import math
def main():
    inicio()

def inicio():
    global num1
    global num2
    ope=stdin.readline().strip()
    print(ope)
    if ope=='suma':
        num1=list(stdin.readline().split())
        num2=list(stdin.readline().split())
        z=sumar(num1,num2)
        if z[1]>=0:
                print(str(z[0])+' + '+str(z[1])+'i')
        else:
                print(str(z[0])+' - '+str(z[1]*-1)+'i')
    elif ope=='resta':
        num1=list(stdin.readline().split())
        num2=list(stdin.readline().split())
        z=restar(num1,num2)
        if z[1]>=0:
                print(str(z[0])+' + '+str(z[1])+'i')
        else:
                print(str(z[0])+' - '+str(z[1]*-1)+'i')
    elif ope=='multiplicacion':
        num1=list(stdin.readline().split())
        num2=list(stdin.readline().split())
        z=multiplicar(int(num1[0]),int(num1[1]),int(num2[0]),int(num1[1]))
        if z[1]>0:
                print(str(z[0])+' + '+str(z[1])+'i')
        else:
                print(str(z[0])+' - '+str(z[1]*-1)+'i')
    elif ope=='division':
        num1=list(stdin.readline().split())
        num2=list(stdin.readline().split())
        z=dividir()
        if z[1]>0:
                print(str(z[0])+' + '+str(z[1])+'i')
        else:
                print(str(z[0])+' - '+str(z[1]*-1)+'i')
    elif ope=='fase polar':
        num1=list(stdin.readline().split())        
        z=fase_polar(int(num1[0]),int(num1[1]))
        if z[1]>=0:
                print(str(z[0])+' + '+str(z[1])+'i')
        else:
                print(str(z[0])+' - '+str(z[1]*-1)+'i')
      
                
    elif ope=='cartesiano a polar':
        num1=list(stdin.readline().split()) 
        z=cartesiano_polar(int(num1[0]),int(num1[1]))
        print('mudulo :'+str(z[0]))
        print('fase polar :'+str(z[1])) 
        
             
    elif ope=='polar a cartesiano':
            num1=list(stdin.readline().split()) 
            z=polar_cartesiano(int(num1[0]),int(num1[1]))
            if z[1]>=0:
                print(str(z[0])+' + '+str(z[1])+'i')
            else:
                print(str(z[0])+' - '+str(z[1]*-1)+'i') 
      
    elif ope=='modulo':
        print("escriba 1 o 2 dependiendo del numero del operador que desea convertir: ")
        tem=int(stdin.readline())
        if tem==1:
            z=modulo(int(num1[0]),int(num1[1]))
            print(z)
        else:
            z=modulo(int(num2[0]),int(num2[1]))
            print(z)
            
    elif ope=='conjugado':
            num1=list(stdin.readline().split())        
            z=conjugado(int(num1[0]),int(num1[1]))
            if z[1]>=0:
                print(str(z[0])+' + '+str(z[1])+'i')
            else:
                print(str(z[0])+' - '+str(z[1]*-1)+'i')
    elif ope=='adicion vectores':
            num1=stdin.readline().split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)
            print(num3)    
            num2=num1=stdin.readline().split()
            num4=[]
            for i in num2:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num4.append(i)    
            print(num4)
            if len(num4)==len(num3):
                res=sumar_vectores(num3,num4)   
            else:
                print('vectores distinta longitud')
    elif ope=='inverso vector':
            num1=stdin.readline().split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)
            res=inverso_vector(num3)
    elif ope=='producto escalar vectores':
            num1=stdin.readline().split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)
            num2=int(stdin.readline())
            res=escalar_por_vector(num2,num3)
        
    elif ope=='adicion matrices':
        num1=stdin.readline().strip()
        num5=[]
        while len(num1)!=0:
            num1=num1.split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)
            num5.append(num3)
            num1=stdin.readline().strip()
        print(num5)    
        num2=stdin.readline().strip()
        num6=[]
        while len(num2)!=0:
            num2=num2.split()
            num4=[]
            for i in num2:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num4.append(i)
            num6.append(num4)
            num2=stdin.readline().strip()    
        print(num6)
        if len(num6)==len(num5) and len(num6[0])==len(num5[0]):
            res=suma_matrices(num5,num6)
        else:    
            print('matrices no equivalentes')
    elif ope=='inversa matriz':
        num1=stdin.readline().strip()
        num5=[]
        while len(num1)!=0:
            num1=num1.split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)
            num5.append(num3)
            num1=stdin.readline().strip()
        res=inversa_matriz(num5)
    elif ope=='escalar por matriz':
        num1=stdin.readline().strip()
        num5=[]
        while len(num1)!=0:
            num1=num1.split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)
            num5.append(num3)
            num1=stdin.readline().strip()
        num4=int(stdin.readline())
        res=matriz_por_escalar(num5,num4)
    elif ope=='transpuesta matriz':
        num1=stdin.readline().strip()
        num5=[]
        while len(num1)!=0:
            num1=num1.split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)
            num5.append(num3)
            num1=stdin.readline().strip()
        res=transponer_matriz(num5)
    elif ope=='conjugado matriz':
        num1=stdin.readline().strip()
        num5=[]
        while len(num1)!=0:
            num1=num1.split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)
            num5.append(num3)
            num1=stdin.readline().strip()
        res=conjugado_matriz(num5)
    elif ope=='adjunta matriz':
        num1=stdin.readline().strip()
        num5=[]
        while len(num1)!=0:
            num1=num1.split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)
            num5.append(num3)
            num1=stdin.readline().strip()
        res=adjunto_matriz(num5)
    elif ope=='multiplicar matrices':
        num1=stdin.readline().strip()
        num5=[]
        while len(num1)!=0:
            num1=num1.split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)
            num5.append(num3)
            num1=stdin.readline().strip()
        print(num5)    
        num2=stdin.readline().strip()
        num6=[]
        while len(num2)!=0:
            num2=num2.split()
            num4=[]
            for i in num2:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num4.append(i)
            num6.append(num4)
            num2=stdin.readline().strip()    
        print(num6)
        if len(num5[0])==len(num6):
            res=multiplicar_matrices(num5,num6)
        else:    
            print('el numero de columnas de la matriz 1 es diferente del numero de filas de la matriz 2')
            
def multiplicar_matrices(num5,num6):
    res=[]
    for i in num5:
        z=[]
        fila=0
        while fila<len(num6[0]):
            print(fila)
            tempo=[]
            for i1 in range(0,len(num6)):
                for j in range(0,len(num6[0])):
                    if j==fila:
                        tempo.append(num6[i1][j])
            fila+=1
            z.append(fila_por_columna(i,tempo))
        res.append(z)
    print(res)
    return res
def fila_por_columna(f,c):
    res=[]
    print(f)
    print(c)
    for i in range(0,len(f)):
        res.append(multiplicar(int(f[i][0]),int(f[i][1]),int(c[i][0]),int(c[i][1])))
    print(res)
    res2=res[0]
    for k in range(1,len(res)):
        res2=sumar(res2,res[k])
    print(res2)
    return res2
def adjunto_matriz(num5):
    tempo=transponer_matriz(num5)
    res=conjugado_matriz(tempo)
    print(res)
    return res
def conjugado_matriz(num5):
    res=[]
    for i in num5:
        tempo=[]
        for j in i:
            tempo.append(conjugado(int(j[0]),int(j[1])))
        res.append(tempo)
    print(res)
    return res
def transponer_matriz(num5):
    res=[]
    fila=0
    while(len(res)!=len(num5[0])):
        tempo=[]
        for i in range(0,len(num5)):
            for j in range(0,len(num5[0])):
                if j==fila:
                    tempo.append(num5[i][j])
                    
        fila+=1
        res.append(tempo)
    print(res)
    return res
def matriz_por_escalar(num5,num4):
    res=[]
    for i in num5:
        res.append(escalar_por_vector(num4,i))
    print(res)
    return res
def inversa_matriz(num5):
    res=[]
    for i in num5:
        res.append(inverso_vector(i))
    print(res)
    return res
                
def suma_matrices(num5,num6):
    res=[]
    for i in range(0,len(num5)):
        res.append(sumar_vectores(num5[i],num6[i]))
    print(res)
    return res

def escalar_por_vector(num2,num3):
    res=[]
    for i in num3:
        res.append([num2*int(i[0]),num2*int(i[1])])
    print(res)
    return res    
    
def inverso_vector(num3):
    res=[]
    for i in num3:
        res.append([-1*int(i[0]),-1*int(i[1])])
    print(res)
    return res
def sumar_vectores(num3,num4):
    res=[]
    for i in range(0,len(num3)):
        res.append(sumar(num3[i],num4[i]))
                    
    print(res)
    return res  
def sumar(num1,num2):
    n1=int(num1[0])
    n2=int(num1[1])
    n3=int(num2[0])
    n4=int(num2[1])
    res=[]
    res.append(n1+n3)
    res.append(n2+n4)
    print(res)
    return res

def restar(num1,num2):
    n1=int(num1[0])
    n2=int(num1[1])
    n3=int(num2[0])
    n4=int(num2[1])
    res=[]
    res.append(n1-n3)
    res.append(n2-n4)
    print(res)
    return res
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
    return res
def conjugado(n1,n2):
    res=[]
    res.append(n1)
    res.append(n2*-1)    
    return res
def modulo(n1,n2):
    res=round(((n1**2)+(n2**2))**(1/2),2)
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
def polar_cartesiano(n1,n2):
    res=[n1*math.degrees(math.cos(n2)),n2*math.degrees(math.sin(n2))]
    return res
main()

    
