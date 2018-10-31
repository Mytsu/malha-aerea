# Instituto Federal de Minas Gerais - Campus Formiga
# Estrutura de Dados 2
# Jonathan Arantes

from grafo.Vertice import Vertice
from grafo.Aresta import Aresta

class Grafo(object):

    def __init__(self, dir = False):
        self.vertices = []
        self.arestas = []
        self.direcionado = dir
        self.tempo = 0

    def addVertice(self, id):
        self.vertices.append(Vertice(id))

    def addAresta(self, orig, dest, peso):
        self.arestas.append(Aresta(orig, dest, peso))
        if not self.direcionado:
            self.arestas.append(Aresta(dest, orig, peso))

    def buscaAresta(self, u, v):
        for i in self.arestas:
            orig = i.getOrigem()
            dest = i.getDestino()
            if orig.getId() == u.getId() and dest.getId() == v.getId():
                return i

    def buscaVertice(self, id):
        for i in self.vertices:
            if id == i.getId():
                return i
    
    def grafoVazio(self):
        if len(self.vertices) == 0:
            return True
        else:
            return False

    def eh_euleriano(self):
        for u in self.vertices:
            if self.grau(u) % 2 is not 0:
                return False
        return True

    def grau(self, u):
        grau = 0
        for w in self.arestas:
            if u == w.getOrigem():
                grau += 1
        return grau

    def buscaLargura(self, v1, v2):
        return []

    def Dijkstra(self, v1):
        return []

    def eh_Ciclico(self):
        if (len(self.arestas) > len(self.vertices) - 1):
            return True
        else:
            return False

    def conexoes(self, id):
        lista = []
        for v in self.vertices:
            if v.getId() == id:
                for a in self.arestas:
                    if a.getOrigem() == v:
                        lista.append((a.getPeso(), a.getDestino()))
        # Retorna uma lista de tuplas com todas as ligações do 
        # vertice indicado, na ordem `Peso, Destino` 
        return lista
