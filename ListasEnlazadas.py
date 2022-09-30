class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)

class SimpleLinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def addNode(self,data):
        P = Nodo(data)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P 

    def Eliminar(self, x):
        P = self.PTR
        if(self.PTR != None):
            while(P != None):
                if(P.next != None and P.next.data == x):
                    if(P.next == self.ULT):
                        P.next = None
                    else:
                        P.next = P.next.next
                P=P.next
        else:
            print("Lista vacia")

    def Recorrido(self):
        P = self.PTR
        while(P != None):
            print(P.data, end="->")
            P = P.next
        print("None")
    
    def __repr__(self):
        respuesta = ""
        P = self.PTR
        while(P != None):
            respuesta = respuesta + str(P.data) + "->"
            P = P.next
        respuesta = respuesta + "None"
        return respuesta

class CircularLinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def addNode(self, data: str):
        P = Nodo(data)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
            self.PTR.next = self.ULT
        else:
            self.ULT.next = P
            self.ULT = P
            self.ULT.next = self.PTR
            
    def Recorrido(self):
        P = self.PTR
        while(P != None):
            print(P.data, end="->")
            P = P.next
        print("None")
    
    def __repr__(self):
        respuesta = ""
        P = self.PTR
        respuesta = respuesta + str(P.data) + "->"
        P = P.next
        while(P != self.PTR):
            respuesta = respuesta + str(P.data) + "->"
            P = P.next
        respuesta = respuesta + "None"
        return respuesta