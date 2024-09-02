from Modelo.Nodo import Nodo

class ListaEnlazada:
    """
        Definicion de la estructura de datos lista simplemente enlazada, basada en nodos que contiene solo el elemento
        y una referencia al nodo siguiente
    """

    def __init__(self):
        """
            Constructor de la clase que inicializa las referencias a la cabeza y cola de la lista vacias y la cantidad
            de elementos de la lista en 0
        """
        self.__cabeza = None
        self.__cola = None
        self.__tamano = 0

    def __len__(self):
        """
            Devuelve la cantidad de elementos en la lista
        """
        return self.__tamano

    def indice_de(self, elemento):
        """
            Devuelve el indice del elemento que se le pasa por parametros
        """
        actual = self.__cabeza
        encontrado = False
        contador = 0
        while actual is not None and not encontrado:
            if actual.obtener_siguiente() == elemento:
                encontrado = True
                return contador
            else:
                actual = actual.obtener_siguiente()
            contador += 1

    def nodo_en(self, indice):
        """
            Devuelve el nodo que esta en la posicion que se le pasa por parametros
        """
        if 0 >= indice >= self.__tamano:
            raise IndexError('Indice fuera de rango!')
        if indice == 0:
            return self.__cabeza
        else:
            nodo = self.__cabeza
            for i in range(indice):
                nodo = nodo.obtener_siguiente()
            return nodo

    def agregar(self, elemento):
        """
            Inserta un elemento al final de la lista
        """
        nuevo_nodo = Nodo(elemento)
        if self.__cabeza is None:
            self.__cabeza = nuevo_nodo
            self.__cola = self.__cabeza
        else:
            self.__cola.cambiar_siguiente(nuevo_nodo)
            self.__cola = nuevo_nodo
        self.__tamano += 1

    def agregar_en(self, indice, elemento):
        """
            Inserta un elemento en el indice que se le pasa por parametros
        """
        nodo = Nodo(elemento)
        if 0 >= indice >= self.__tamano:
            raise IndexError('Indice fuera de rango!')
        if indice == 0:
            nodo.cambiar_siguiente(self.__cabeza)
            self.__cabeza = nodo
        elif indice == self.__tamano - 1:
            self.__cola.cambiar_siguiente(nodo)
            self.__cola = nodo
        else:
            anterior = self.node_at(indice - 1)
            next = self.node_at(indice)
            anterior.cambiar_siguiente(nodo)
            nodo.cambiar_siguiente(next)
        self.__tamano += 1

    def agregar_coleccion(self, nueva_lista):
        """
            Inserta todos los elementos de la lista que se le pasa por parametros
        """
        for valor in nueva_lista:
            self.agregar(valor)

    def eliminar(self, elemento):
        """
            Elimina el elemento que se le pasa por parametros
        """
        actual = self.__cabeza
        anterior = None
        found = False
        while not found and actual is not None:
            if actual.obtener_siguiente() is elemento:
                found = True
            else:
                anterior = actual
                actual = actual.obtener_siguiente()
        if anterior is None:
            self.__cabeza = actual.obtener_siguiente()
        else:
            anterior.cambiar_siguiente(actual.obtener_siguiente())
        self.__tamano -= 1
        self.__cola = self.node_at(self.__tamano - 1)
        if not found:
            print('Elemento no encontrado')

    def __iter__(self):
        """
            Convierte la lista en un objeto iterable
        """
        actual = self.__cabeza
        while actual is not None:
            yield actual
            actual = actual.obtener_siguiente()

