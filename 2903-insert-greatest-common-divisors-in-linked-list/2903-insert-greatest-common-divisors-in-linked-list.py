# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Algoritmo Euclidiano
        def gcd(x, y):
            # Mientras el segundo número (y) no sea cero
            while y:
                # Se asigna a x el valor de y, y a y el residuo de x entre y
                x, y = y, x % y  
            # Se devuelve el valor absoluto de x, que es el MCD
            return abs(x)

        # Si solo tenemos un elemento, regresar head
        if head.next == None:
            return head

        # Crear nodos para GCD
        prev, post = head, head.next

        # Mientras post no sea NULO
        while post:

            # Creamos un nuevo nodo cuyo valor sera el GCD de prev y post
            new = ListNode(gcd(prev.val, post.val))

            # Asignamos prev.next al nuevo nodo y new.next al nodo posterior
            prev.next = new
            new.next = post

            # Actualizamos los nodos prev y post para seguir con el calculo
            prev = post
            post = post.next
        
        # Regresamos la LL
        return head