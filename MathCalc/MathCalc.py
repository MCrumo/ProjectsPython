import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy.plotting import plot
import numpy.linalg as lin
import cmath as cm
sp.init_printing()


p='pregunta'
def n(p):
    a='aaaaa'
    while a.isalpha()==True and a[0]!='-' or a[0]==' ' or a.isalpha()==False and a.isdigit()==False and a[0]!='-':
        a=input(p)    
    if a.isdigit():
        b=float(a)
        return b
    elif a[0]=='-' and a[1].isdigit()==True:
        b=float(a)
        return b



preg='Files/Columnes? '
def fc(preg):
    a='a'
    while a.isalpha()==True or a.isalpha()==False and a.isdigit()==False or a=='1' or a=='0':
        a=input(preg)
    if a.isdigit() and a!='1' and a!='0':
        b=int(float(a))
        return b

def vec():
    vec=[]
    for i in range(arg):
        vec.append(n(str(i+1)))
    return vec


def mat():
    llista=[]
    f=fc(preg)
    for i in range(f):
        llista.append([])
        for j in range(f):
            llista[i].append(n(str(i+1)+str(j+1)+' '))
    llista=np.array(llista)
    return llista

def p_mat():
    llista=[]
    fila=int(n('Files? '))
    columna=int(n('Columnes? '))
    if fila<=0:
        print('Row out of range ')
    if columna<=0:
        print('Column out of range ')
    
    for i in range(fila):
        llista.append([])
        for j in range(columna):
            llista[i].append(n(str(i+1)+str(j+1)))
    llista=np.array(llista)
    return llista

def t_vec():
    llista=[]
    fila=int(n('Files? '))
    if fila<=0:
        print('Row out of range ')
    else:
        for i in range(fila):
            llista.append([])
            for j in range(1):
                llista[i].append(n(str(i+1)+str(j+1)))
    llista=np.array(llista)
    return llista


def diag():
    m=mat()
    m=sp.Matrix(m)
    diag= m.diagonalize()
    return m.eigenvects(), m.eigenvals(), diag

def mat_prod(): 
    try:
        n=int(float(input('Quants elements multilicaras?\n 1<n<4 ')))
    except:
        return('Must be type(float) ')
    
    if n<=1 or n>=4:
        return('Product out of range ')
    if n==2:
        print('\nMat 1 ')
        m1=np.array(mat())
        print('\nMat 2 ')
        m2=np.array(mat())
        x=np.dot(m1,m2)
        print(x)
    if n==3:
        print('\nMat 1 ')
        m1=np.array(mat())
        print('\nMat 2 ')
        m2=np.array(mat())
        print('\nMat 3 ')
        m3=np.array(mat())
        m23=np.dot(m2,m3)
        x=np.dot(m1,m23)
        print(x)
         
def mv_prod():
    try:
        a=int(float(input('Mat·vec --> 1\nvec·Mat --> 2\n')))
    except:
        return('None type(float) ')
              
    if a==1:
        print('\nMat: ')
        m=np.array(mat())
        print('\nvec')
        v=vec()
        x=np.dot(m,v)
        return x
    elif a==2:
        print('\nvec')
        v=vec()
        print('\nMat: ')
        m=np.array(mat())
        x=np.dot(v,m)
        return x
    else:
        return('Out of range ')
    
def mat_op():
    try:
        a=int(float(input(
            'Transpose(mat) --> 1\n'
            '(mat)-1 ---------> 2\n'
            'det|mat| --------> 3\n')))
    except:
        return('None type(float) ')
    if a==1:
        m=np.array(mat())
        t= np.transpose(m)
        return t
    if a==2:
        m=np.array(mat())
        minv= lin.inv(m)
        return minv
    if a==3:
        m=np.array(mat())
        det=lin.det(m)
        return det
    else:
        return('Out of range ')

def poli():
    sp.init_printing()
    sp.var('k')
    m=mat()
    Nuc=sp.Matrix(m)
    ki= sp.eye(len(m[0]))*k
    Mp= Nuc-ki
    poli=Mp.det()
    spoli=sp.sympify(str(poli))
    #a=sp.factor(spoli)
    return('Polinomi simplificat: ', spoli)

def p_escalar():
    print('wt·G·v\n')
    print('wt\n')
    wt=t_vec()
    print('\nG\n')
    G=mat()
    print('\nv\n')
    v=np.array(vec())
    p=np.dot(wt,G)
    prod=np.dot(p,v)
    return prod
 
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

sp.var('x')
f=x**2
def integrar(f):
    sp.var('x')
    a=('Vols que sigui definida? ')
    print(a)
    while a!='si' and a!='no':
        a=input('si o no? ')
    b=a
    if b=='no':
        inti= sp.integrate(f,x)
        return inti
    if b=='si':
        x0=n('lim inferior: ')
        xf=n('lim superior: ')
        intd= sp.integrate(f,(x,x0,xf))
        return intd

def derivar(f):
    sp.var('x')
    der=sp.diff(f)
    return der

def limit(f):
    sp.var('x')
    x0=n('En quin punt vols evaluar el límit')
    a=('Vols evaluar els límits laterals? ')
    print(a)
    while a!='si' and a!='no':
        a=input('si o no? ')
    b=a
    if b=='si':
        lime=sp.limit(f,x,x0,'-')
        limd=sp.limit(f,x,x0,'+')
        return ('Límit esquerra: ', lime, 'Límit dreta: ',limd)
    if b=='no':
        limx=sp.limit(f,x,x0)
        return limx

def n(p):
    a='a'
    while a.isalpha():
        a=input(p)
    b=float(a)
    return b

def sistema():
    llista=[]
    vals=['x','y','z','t','s','m','n','r','a','b','c','d','e','f','g','h']
    valors=[]
    f=fc('Quantes incògnies/equacions hi ha? ')
    if f>len(vals):
        return('Out of range', len(vals))
    else:
        print('Matriu NO apliada: ')
        llista2=[]
        for i in range(f):
            llista2.append([])
            for j in range(f):
                llista2[i].append(n(vals[j]+': '))
        M=np.array(llista2)
        va=[]
        for i in range(f):
            va.append(n('Terme independent '+str(i+1)+': '))
        va=np.array(va)
        sol=lin.solve(M,va)
        for i in range(f):
            valors.append(vals[i])
        ig=[]
        for i,j in zip(valors,sol):
            igualtat= str(i)+'='+str(j)
            ig.append(igualtat)
        return ig

def complexe(x,y):
    sp.var('e')
    z=complex(x,y)
    #print('Real: ', z.real,'\tImag: ',z.imag)
    #print(dir(cm))
    w= cm.polar(z)   
    print('Binòmica:',z)
    print('Exponencial:', (w[0])*e**(1j*(w[1])))
    print('Mòdul: ',w[0],'u','\nAngle: ',w[1],'rad')

def mcd(a, b):
    if a == b:
        return a
    elif a > b:
        return mcd(a-b, b)
    else:
        return mcd(a, b-a)

def mcm(a, b):
    mcm = (a*b) / mcd(a, b)
    return int(mcm)

funcio=x**3
def grafica(funcio):
    sp.var('x')
    x0=n('x0? ')
    xf=n('xf? ')
    print(' ')
    plot(funcio, (x,x0,xf), xlavel= 'X', ylavel='Y',title=str(funcio))
    
def ajuda():
    a=('FUNCIONS:\n\n'
    'Algebra:\n'
    '\tdiag():        vaps i veps de M\n'
    '\tmat_prod():    producte de matrius\n'
    '\tmv_prod():     productes matriu, vector\n'
    '\tmat_op():      opreancions d una matriu\n'
    '\tpoli():        polinomi característic'
    '\nCàlcul:\n'
    '\tfactorial(n)   factorial de int n\n'
    '\tintegrar(f):   integra la funció\n'
    '\tderivar(f):    deriva la funció\n' 
    '\tlimit(f):      limit de la funció\n'
    '\tsistema():     resol el sistema\n'
    '\tcomplexe(x,y)  complex de re(x) i Im(y)\n'
    '\tmcd(a,b)       mcd de int a, int b\n'
    '\tmcm(a,b)       mcm de int a, int b'
    '\nFísica:\n'
    '\tgrafica(f):    gràfica de la funció\n'
    '\nDEFINICIONS:\n'
    '\tn(preg):   input per un nombre R\n' 
    '\tfc(preg):  input de files/columnes\n'
    '\tmat():     definir matriu quadrada\n'
    '\tp_mat:     definir matriu amb i(files) & j(columnes)\n'
    '\tvec():     definir vector\n'
    '\tt_vec():   definir vector transposat\n'
    '')
    print(a)
    
    
ajuda()
