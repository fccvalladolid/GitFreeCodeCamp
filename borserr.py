#BORJA SERRANO PEREZ

import random



#----------------------------------------------------------------------------------------------

def puntuacion(nivel, toques):   

   ficheroA="Puntuaciones.txt"

   ficheroB="Auxiliar.txt"

   existe=False #Varuable que nos va a marcar si existe o no el nivel al que estamos jugando

   

   try:

      ficheroPuntos=open(ficheroA, "r")

      

      for l in ficheroPuntos:

         if int(l[0])==nivel: #Se ejecuta cuando el nivel actual que vamos a guardar coincide con uno ya guardado

            existe=True #Quiere decir que existe ese nivel y no tiene que crearlo

            puntos=int(l[2])

            break

               

      if existe: #Como existe ese nivel, compara sus toques

         ficheroPuntos.seek(0)   

         if toques<puntos: #Si consique un numero de puntos(toques) que los que ya estaban guardados en el fichero

            print "Enhorabuena! Ha batido el record del nivel", nivel, ".\n"

            aux=open(ficheroB, "w")

            

            for linea in ficheroPuntos: #Bucle que actualiza el ficheroB (aux) para despuues volcarle en el ficheroA (ficheroPuntos)

               if int(linea[0])!=nivel: #Copia los niveles diferentes al que estamos jugando tal cual                        

                  aux.write(linea)

               else: #Reescribre el nivel actual con la nueva puntuacion

                  aux.writelines([str(nivel), " ", str(toques),"\n"])   

            ficheroPuntos.close()

            aux.close()

            copiaFichero(ficheroA, ficheroB)       

                  

      else: #Se ejecuta si existe=false, que quiere decir que no existe ese nivel(es la primera vez que se juega)

         ficheroPuntos.close()

         ficheroPuntos=open(ficheroA, "a")

         ficheroPuntos.writelines([str(nivel), " ", str(toques), "\n"])



   except:#Crea el fichero la primera vez que se ejecuta el programa

      ficheroPuntos=open(ficheroA, "w")

      ficheroPuntos.writelines([str(nivel), " ", str(toques),"\n"])

      ficheroPuntos.close()   

            



   

#----------------------------------------------------------------------------------------------

#Sustituye el contenido del ficheroA por el del ficheroB

def copiaFichero(ficheroA, ficheroB):

   f1=open(ficheroA, "w")

   f2=open(ficheroB, "r")



   for linea in f2:

      f1.write(linea)



   f1.close()

   f2.close()

#----------------------------------------------------------------------------------------------

def muestraTab(tablero):

   numeros=[" ",0,1,2,3,4,5,6,7,8,9]

   letras=['A','B','C','D','E','F','G','H','I','J']

   k=0

   

   print ""

   for i in numeros: #Imprime en horizontal en la primera linea la lista numeros

      print i, " ",

   print ""



   for i in range(2,12): #Bucle for que imprime la lista letras y la lis tatablero

      print letras[k]," ", #Imprime en vertical en la primera columna la lista letras   

      for j in range(2,12): 

         print tablero[i][j], " ", #Va recorriendo en cada fila todas sus columnas e imprimiendo lo que se encuentra

      k=k+1

      print "\n"

   print "\n"

#------------------------------------------------------------------------------------------------

#Busca mediante el bucle for las x y si no hay ninguna x quiere decir que el tablero esta vacio por lo que devuelve false para que se acabe el juego



def comprobar(tablero):

   encontrado=False



   for i in range(2,12):

      for j in range(2,12):

         if tablero[i][j]=='x': 

            encontrado=True

            break

      

   return encontrado

#------------------------------------------------------------------------------------------------

def juego(tablero):

   toques=0

   i=1

   l=[]

   

   print "\nLa orden para jugar tiene que ser del tipo: A0, en este caso dara un toque en esa posicion.\n"

   print "\nSi en algun momento desea acabar el juego introduzca SALIR.\n"

   print "\nSi quiere rectificar puede hacerlo tantas veces como quiera hasta al tablero inicial introduciendo DESHACER.\n"



   while True:

      fallo=False #Variable que en caso de que sea true no se ejecuta el juego y empieza el bucle otra vez

      orden=raw_input("Introduzca la orden: ")



      if orden=="SALIR": break

      elif orden=="DESHACER":

         if toques==0: print "\nNo has dado ningun toque, no puedes deshacer.\n"

         else:

            if i<=toques:

               tablero=toque(tablero, l[len(l)-i][0], l[len(l)-i][1]) #Se pasa a la subrutina toque el tablero y la ultima coordenada guardada en el array

               muestraTab(tablero)

               i=i+1

            else: print "\nSe encuentra en el tablero inicial, imposible deshacer mas.\n"

               

      else: 

         if len(orden)!=2: print "La orden introducida no es valida."

         else:

            if orden[0]=="A": x=0+2

            elif orden[0]=="B": x=1+2

            elif orden[0]=="C": x=2+2

            elif orden[0]=="D": x=3+2

            elif orden[0]=="E": x=4+2

            elif orden[0]=="F": x=5+2

            elif orden[0]=="G": x=6+2

            elif orden[0]=="H": x=7+2

            elif orden[0]=="I": x=8+2

            elif orden[0]=="J": x=9+2

            else: 

               print "La orden introducida no es valida."

               fallo=True

         

            if fallo==False:        

               try:

                  y=int(orden[1])+2

   

                  l.append([x,y]) #Lista donde se almacenan los toques que se realizan



                  toques=toques+1



                  tablero=toque(tablero,x,y)

                  muestraTab(tablero)

                  continuar=comprobar(tablero)

                  

                  if continuar==False:

                     if toques==1: print "Has resuelto el tablero en", toques, "toque.\n"

                     else: print "Has resuelto el tablero en", toques, "toques.\n"

                     puntuacion(nivel, toques) 

                     break

         

               except ValueError: print "La orden introducida no es valida."

#----------------------------------------------------------------------------------------------

#Partiendo de la coordenada introducida que es la central, se da un toque cambiando las x por puntos y viceversa



def toque(tablero, x, y):

   i=0

   k=-2

   while i<5: #Este bucle los cambia por columnas, que como son 5 la i va hasta 5. No cambia la fila superior ni enferior

      if tablero[x-1][y+k]=='.': tablero[x-1][y+k]='x'

      elif tablero[x-1][y+k]=='x': tablero[x-1][y+k]='.'

      

      if tablero[x][y+k]=='.': tablero[x][y+k]='x'

      elif tablero[x][y+k]=='x': tablero[x][y+k]='.'

      

      if tablero[x+1][y+k]=='.': tablero[x+1][y+k]='x'

      elif tablero[x+1][y+k]=='x': tablero[x+1][y+k]='.'

      

      k=k+1 

      i=i+1       

   i=0

   j=-1

   while i<3: #Como en el bucle anterior no cambia la fila superior e inferior, se cambian en este bucle que como tienen 3 columnas la i va hasta 3

      if tablero[x-2][y+j]=='x': tablero[x-2][y+j]= '.'

      elif tablero[x-2][y+j]=='.': tablero[x-2][y+j]= 'x'

         

      if tablero[x+2][y+j]=='x': tablero[x+2][y+j]='.'

      elif tablero[x+2][y+j]=='.':tablero[x+2][y+j]='x'

      j=j+1

      i=i+1



   return tablero

#-----------------------------------------------------------------------------------------------

#Crea un tablero aleatoriamente en funcion del nivel introducido



def mancharTab(tablero, nivel):

   i=0



   while i<nivel:

      x=random.randint(2,11)

      y=random.randint(2,11)

      tablero=toque(tablero, x, y)

      i=i+1



   return tablero

#------------------------------------------------------------------------------------------------   

#Inicializa el tablero, por lo que solo esta compuesto de puntos



def tabVacio(Filas, Columnas):



   tablero=range(Filas)

   for i in tablero:       

      tablero[i]=range(Columnas)

   

   for i in tablero:       

      for j in i:

         i[j]="."



   return tablero

#----------------------------------------------------------------------------------------------

#  "MAIN"



Filas=14 #Filas

Columnas=14 #Columnas

   



tablero=tabVacio(Filas, Columnas)



while True:

      nivel=raw_input("\n\nIntroduzca el nivel deseado para comenzar la partida: ")

      try:

         nivel=int(nivel)

         if nivel>=1: break 

         else:

            print "\nERROR! El nivel debe de ser mayor o igual que 1."

            print "\n\nIntroduzca el nivel deseado para comenzar la partida: "

      except ValueError:

         print "\nERROR! Entrada no valida."

         print "\n\nIntroduzca el nivel deseado para comenzar la partida: "



tablero=mancharTab(tablero, int (nivel))

muestraTab(tablero)

juego(tablero)


