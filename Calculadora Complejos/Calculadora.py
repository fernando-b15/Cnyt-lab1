from sys import stdin
import math
import unittest

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
        z=multiplicar(float(num1[0]),float(num1[1]),float(num2[0]),float(num1[1]))
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
        z=fase_polar(float(num1[0]),float(num1[1]))
        if z[1]>=0:
                print(str(z[0])+' + '+str(z[1])+'i')
        else:
                print(str(z[0])+' - '+str(z[1]*-1)+'i')
      
                
    elif ope=='cartesiano a polar':
        num1=list(stdin.readline().split()) 
        z=cartesiano_polar(float(num1[0]),float(num1[1]))
        print('mudulo :'+str(z[0]))
        print('fase polar :'+str(z[1])) 
        
             
    elif ope=='polar a cartesiano':
            num1=list(stdin.readline().split()) 
            z=polar_cartesiano(float(num1[0]),float(num1[1]))
            if z[1]>=0:
                print(str(z[0])+' + '+str(z[1])+'i')
            else:
                print(str(z[0])+' - '+str(z[1]*-1)+'i') 
      
    elif ope=='modulo':
        print("escriba 1 o 2 dependiendo del numero del operador que desea convertir: ")
        tem=int(stdin.readline())
        if tem==1:
            z=modulo(float(num1[0]),float(num1[1]))
            print(z)
        else:
            z=modulo(float(num2[0]),float(num2[1]))
            print(z)
            
    elif ope=='conjugado':
            num1=list(stdin.readline().split())        
            z=conjugado(float(num1[0]),float(num1[1]))
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
            num2=float(stdin.readline())
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
        num4=float(stdin.readline())
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
    elif ope=='norma':
            num1=stdin.readline().split()
            num3=[]
            for i in num1:
                i=i.replace('(','')
                i=i.replace(')','')
                i=i.replace(',',' ')
                i=i.split()
                num3.append(i)        
            print(num3)
            norma(num3)
    elif ope=='distancia entre vectores':
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
            distanciaentrevectores(num3,num4)
    elif ope=='matriz hermitiana':
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
        matrizhermitiana(num5)
    elif ope=='matriz unitaria':
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
        matrizunitaria(num5)
    elif ope=='producto tensor':
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
        producto_tensor(num5,num6)
def producto_tensor(num5,num6):
    mat=[]
    for i3 in range(0,(len(num5)*len(num6))):
        tempo=[]
        for j5 in range(0,len(num5[0])*len(num6[0])):
            tempo.append([i3,j5])
        mat.append(tempo)
    for z1 in range(0,len(mat)):
        for z2 in range(0,len(mat[0])):
            if z1==1 and z2==0:
                print(z1//len(num6),z2//len(num5))
            num10=num5[z1//len(num6)][z2//len(num5)]
            num11=num6[z1%len(num6)][z2%len(num5)]
            print(num10,num11)
            mat[z1][z2]=multiplicar(float(num10[0]),float(num10[1]),float(num11[0]),float(num11[1]))
    print(mat)
def matrizunitaria(num5):
    num8=adjunto_matriz(num5)
    res=multiplicar_matrices(num5,num8)
    print(res)
    l1=[0,0]
    l2=[0,0]
    l3=[0,0]
    for i2 in range(0,len(res)):
        for j3 in range(0,len(res[0])):
            if i2==j3:
                l3[0]+=res[i2][j3][0]
                l3[1]+=res[i2][j3][1]
            elif j3>i2:
                l1[0]+=res[i2][j3][0]
                l1[1]+=res[i2][j3][1]
            elif i2>j3:
                l2[0]+=res[i2][j3][0]
                l2[1]+=res[i2][j3][1]
    print(sum(l1)+sum(l2),math.ceil(sum(l3)))            
    if sum(l1)+sum(l2)==0 and (math.ceil(sum(l3)))==len(res):
        print('TRUE')
    else:
        print('FALSE')
def matrizhermitiana(num5):
    num8=adjunto_matriz(num5)
    for i1 in range(len(num5)):
        for j1 in range(len(num5[0])):
            num5[i1][j1]=[float(num5[i1][j1][0]),float(num5[i1][j1][1])]
    if num5==num8:
        print('TRUE')
    else:
        print('FALSE')
def distanciaentrevectores(num3,num4):
    num5=[]
    for i in range(0,len(num3)):
        num5.append([float(num3[i][0])-float(num4[i][0]),float(num3[i][1])-float(num4[i][1]),])
    print(num5)
    norma(num5)
def norma(num3):
    res=[]
    for i in num3:
        res.append(float(i[0])**2)
        res.append(float(i[1])**2)
    res1=sum(res)**(1/2)    
    print(res1)
    return res1

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
        res.append(multiplicar(float(f[i][0]),float(f[i][1]),float(c[i][0]),float(c[i][1])))
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
            tempo.append(conjugado(float(j[0]),float(j[1])))
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
        res.append([num2*float(i[0]),num2*float(i[1])])
    print(res)
    return res    
    
def inverso_vector(num3):
    res=[]
    for i in num3:
        res.append([-1*float(i[0]),-1*float(i[1])])
    print(res)
    return res
def sumar_vectores(num3,num4):
    res=[]
    for i in range(0,len(num3)):
        res.append(sumar(num3[i],num4[i]))
                    
    print(res)
    return res  
def sumar(num1,num2):
    n1=float(num1[0])
    n2=float(num1[1])
    n3=float(num2[0])
    n4=float(num2[1])
    res=[]
    res.append(n1+n3)
    res.append(n2+n4)
    print(res)
    return res

def restar(num1,num2):
    n1=float(num1[0])
    n2=float(num1[1])
    n3=float(num2[0])
    n4=float(num2[1])
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
    if num2[0]==0 and num2[1]==0:
        print("no se puede dividir entre cero")
    else:    
        n1=float(num1[0])
        n2=float(num1[1])
        n3=float(num2[0])
        n4=float(num2[1])
        cont=conjugado(n3,n4)
        r1=multiplicar(n1,n2,cont[0],cont[1])
        r2=multiplicar(n3,n4,cont[0],cont[1])
        res=[(r1[0]/r2[0]),(r1[1]/r2[0])]
        print(res)
        return res
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
        res=math.degrees(math.atan(n2/n1))
        print(res)
        return res
    elif n1<0 and 0<=n2:
        res=180+math.degrees(math.atan(n2/n1))
        print(res)
        return res
    elif n1<0 and n2<0:
        res=180+math.degrees(math.atan(n2/n1))
        print(res)
        return res
    else:
        res=360+math.degrees(math.atan(n2/n1))
        print(res)
        return res
def cartesiano_polar(n1,n2):
    res=[modulo(n1,n2),fase_polar(n1,n2)]
    print(res)
    return res
def polar_cartesiano(n1,n2):
    res=[n1*math.degrees(math.cos(n2)),n2*math.degrees(math.sin(n2))]
    return res
class TestStringMethods(unittest.TestCase):

    def test_sumarcomplejos(self):
        self.assertEqual([5,2],sumar([3,2],[2,0]))
    def test_restacomplejos(self):
        self.assertEqual([1,1],restar([5,2],[4,1]))
    def test_multiplicarcomplejos(self):
        self.assertEqual([14,23],multiplicar(4,3,5,2))
    def test_conjugadocomplejos(self):
        self.assertEqual([5,3],conjugado(5,-3))
    def test_modulocomplejos(self):
        self.assertEqual(5,modulo(4,3))
    def test_sumavectorescomplejos(self):
        self.assertEqual([[16.0,0.0],[1.0,1.0],[3.0,-9.0]],sumar_vectores([[8,3],[-1,-4],[0,-9]],[[8,-3],[2,5],[3,0]]))     
    def test_inversovectorescomplejos(self):
        self.assertEqual([[5.0,-2.0],[-3.0,0.0],[0.0,1.0]],inverso_vector([[-5,2],[3,0],[0,-1]])) 
    def test_sumamatricescomplejos(self):    
         self.assertEqual([[[-15.0,-5.0],[-10.0,-6.0],[7.0,3.0]],[[4.0,17.0],[6.0,-7.0],[14.0,-10.0]],[[5.0,5.0],[2.0,-1.0],[-2.0,-1.0]]],suma_matrices([[[-8,-3],[-6,-4],[0,-4]],[[-1,8],[6,-10],[8,-5]],[[4,0],[8,5],[-7,-9]]],[[[-7,-2],[-4,-2],[7,7]],[[5,9],[0,3],[6,-5]],[[1,5],[-6,-6],[5,8]]]))
    def test_inversamatrizcomplejos(self):
         self.assertEqual([[[-7.0,-3.0],[1.0,-7.0]],[[9.0,4.0],[7.0,9.0]]],inversa_matriz([[[7,3],[-1,7]],[[-9,-4],[-7,-9]]]))
    def test_transponermatriz(self):
         self.assertEqual([[[5.0,9.0],[-7.0,-5.0],[-1.0,-4.0]],[[8.0,2.0],[-3.0,-7.0],[7.0,-8.0]]],transponer_matriz([[[5,9],[8,2]],[[-7,-5],[-3,-7]],[[-1,-4],[7,-8]]]))
    def test_adjuntramatrices(self):
         self.assertEqual([[[7.0,-7.0],[5.0,0]],[[3.0,-8.0],[8.0,6.0]],[[8.0,-4.0],[-10.0,1.0]]],adjunto_matriz([[[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]]))
if __name__ == '__main__':
    unittest.main()
main()

    
