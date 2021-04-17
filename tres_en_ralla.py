import tkinter

def ini_finestra():
    
    root= tkinter.Tk()
    finestra= tkinter.Canvas(root, height= 600, width=600, background= 'grey') 
    finestra.pack()
    return finestra         


def ini_graella(finestra):
    for i in [0, 150, 300, 450]:         #creem el 1r bucle, que generarà les 3 barres horitzontals
        finestra.create_line(75,75+i,      # separades entre si, 150 unitats.
                             525,75+i,
                             width= 7,
                             fill= 'magenta')
        
    for i in [0, 150, 300, 450]:
        finestra.create_line(75+i,75,      #ara fem el mateix per les verticals
                             75+i,525,
                             widt= 7,
                             fill= 'magenta')  
    return finestra




def marca_casella(fila, columna, jugador, finestra): 
    f = 0   # definim f, que serà la cordenada 'y' cartesiana de referència per marcar el punt del jugador
    c = 0   # definim c, que serà la cordenada 'x' cartesiana de referència per marcar el punt del jugador
    
    #segons quina sigui la fila, la 'y' tindrà 3 valors diferent, per tant, el associem segons la fila 
    if fila==1:     
        f=75
       
    if fila==2:
        f=75+150
     
    if fila==3:
        f=75+150+150
        
   #segons quina sigui la columna, la 'x' tindrà 3 valors diferent, per tant, el associem segons la columna 
    if columna==1:
        c=75
        
    if columna==2:
        c=75+150
        
    if columna==3:
        c=75+150+150
        
    if jugador == 'blau':
        finestra.create_oval(c, f,
                            c+150,f+150,
                            fill= 'blue')
    if jugador == 'vermell':
        finestra.create_oval(c, f,
                            c+150,f+150,
                            fill= 'red')
        
def taulell_ple(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if (mat[i][j] == 0): 
                return False
    return True

def is_win(m): 
    #Les dues diagonals
    if m[0][0]==1 and m[1][1]==1 and m[2][2]==1: return 1;
    if m[0][0]==2 and m[1][1]==2 and m[2][2]==2: return 2;
    if m[0][2]==1 and m[1][1]==1 and m[2][0]==1: return 1;
    if m[0][2]==2 and m[1][1]==2 and m[2][0]==2: return 2;
    #Totes les columnes
    if m[0][0]==1 and m[1][0]==1 and m[2][0]==1: return 1;
    if m[0][0]==2 and m[1][0]==2 and m[2][0]==2: return 2;
    if m[0][1]==1 and m[1][1]==1 and m[2][1]==1: return 1;
    if m[0][1]==2 and m[1][1]==2 and m[2][1]==2: return 2;
    if m[0][2]==1 and m[1][2]==1 and m[2][2]==1: return 1;
    if m[0][2]==2 and m[1][2]==2 and m[2][2]==2: return 2;
    #Totes les files
    if m[0][0]==1 and m[0][1]==1 and m[0][2]==1: return 1;
    if m[0][0]==2 and m[0][1]==2 and m[0][2]==2: return 2;
    if m[1][0]==1 and m[1][1]==1 and m[1][2]==1: return 1;
    if m[1][0]==2 and m[1][1]==2 and m[1][2]==2: return 2;
    if m[2][0]==1 and m[2][1]==1 and m[2][2]==1: return 1;
    if m[2][0]==2 and m[2][1]==2 and m[2][2]==2: return 2;
    else: return 0; # returns 0 si no juanga cap dels dos
        

comptador= 0
finestra= ini_finestra()
ini_graella(finestra) # "guardem" la graella dins de canvas per ajuntar les dues funcions
taulell = [[0,0,0],[0,0,0],[0,0,0]]
a=150

def control_de_joc(event):
    global a
    global finestra
    global jugador
    global comptador
    global taulell
    
    x= event.x
    y= event.y
    if comptador%2 == 0:
        jugador='blau'
    else:
        jugador= 'vermell'
    comptador=comptador+1
    fila=1
    columna=1
                
    for i in range(3):
        for j in range(3):
            xi= 75+(i*a)
            xf= xi + a
            yi= 75 + (j*a)
            yf= yi + a
            if xi<x and x<xf and yi<y and y<yf:
                fila=i+1
                columna=j+1
    
    if taulell[fila-1][columna-1] == 0 and is_win(taulell) == 0:
        if (jugador == 'blau'):
                taulell[fila-1][columna-1] = 1 # 1 if casella balva
                marca_casella(columna, fila, jugador, finestra)
        else:
            taulell[fila-1][columna-1] = 2 # 2 if casella vermella
            marca_casella(columna, fila, jugador, finestra)
    else:
        comptador = comptador - 1
        

    if taulell_ple(taulell) or  is_win(taulell) != 0: #reiniciar?
        comptador= 0 
        finestra= ini_finestra()
        ini_graella(finestra)
        taulell = [[0,0,0],[0,0,0],[0,0,0]]
        a=150
        
        finestra.bind('<ButtonRelease-1>',control_de_joc)
        finestra.mainloop()
        control_de_joc(event)
    
finestra.bind('<ButtonRelease-1>',control_de_joc)

finestra.mainloop()
