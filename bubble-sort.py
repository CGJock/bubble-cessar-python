"""
para hacer la implementacion de un bubble sort debemos tomar en cuenta que se desea hacer una comparacion uno a uno de los elementos
hasta encontrar el numero menor y llevarlo al final del elemnto
ejemplo [1,2,5,9,6,4]
tras el primer bucle [1,2,5,6,4,9]
y tras terminar todos los bucles [1,2,4,5,6,9]
significando que con cada vuelta, se lleva el elemento mayor al final "bubbling"

Para implementar el buble sort necesitaremos:
un array a ordenar
-un loop interno que recorre el loop e intercambien los numeros si el primer valor es mayor al siguiente, este loop debera recorrer un elemento menos por cada iteracion, ya que se encuentran filtrados ya
-un loop externo que controle cuantas veces se debera hacer esto -1 cantidad de veces que el largo del array original
"""

disordered_array = [1,3,5,7,8,2,9,10,4,15]

def sort(array):
    times_to_run = len(array)# timestorun sera igual al largo del array
    
    #loop externo que se recorre -1 una cantidad de veces respecto al largo del array ej= (ttr =10 = 10 ttr - 1 = 9)
    for i in range(times_to_run -1):
      for j in range(times_to_run - i - 1):#loop interno que se ira decreciendo a cada iteracion, ej en la primera vuelta (ttr=10, i= 0, = 1 ) (ttr - i -1)= 9
          if array[j] > array[j+1]:
            #si el elemento del array es mayor al siguiente, se swapea la posicion, asi hasta llevar ese numero al final
            array[j],array[j+1] = array[j+1], array[j]
    print(array)
            
#expected output [1,2,3,4,5,7,8,9,10,15]

sort(disordered_array)
