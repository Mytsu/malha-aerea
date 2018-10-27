# Instituto Federal de Minas Gerais - Campus Formiga
# Estrutura de Dados 2
# Jonathan Arantes

from Vertice import Vertice
from Aresta import Aresta

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

    def inicializaFonte(self, fonte):
        for v in self.vertices:
            v.setEstimativa(99999)
            v.setVisitado(False)
        fonte.setVisitado(True)
        fonte.setEstimativa(0)

    def relaxaVertice(self, u, v, w):
        if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
            v.setEstimativa(u.getEstimativa() + w.getPeso())
            v.predecessor.append(u.getId())

    def visita(self, u):
        u.setVisitado(True)
        self.tempo += 1
        u.setInput(self.tempo)
        v = self.buscaAdjacente(u)
        while v is not None:
            v.predecessor.append(u.getId())
            self.visita(v)
            v = self.buscaAdjacente(u)
        self.tempo += 1
        u.setOutput(self.tempo)
        return u.predecessor

    def buscaAdjacente(self, u):
        for i in range(len(self.arestas)):
            origem = self.arestas[i].getOrigem()
            destino = self.arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True)
                return destino
        else:
            return None

    def buscaLargura(self, id):
        fonte = self.buscaVertice(id)
        if fonte is None:
            return None
        self.inicializaFonte(fonte)
        lista = [fonte]
        while 0 != len(lista):
            u = lista[0]
            v = self.buscaAdjacente(u)
            if v is None:
                lista.pop(0)
            else:
                self.tempo += 1
                v.setInput(self.tempo)
                v.predecessor.append(u.getId())
                v.setVisitado(True)
                lista.append(v)
            u.setVisitado(True)

    def buscaProfundidade(self):
        self.tempo = 0
        for v in self.vertices:
            v.setVisitado(False)
            v.input = 0
            v.output = 0
        for v in self.vertices:
            if not v.getVisitado():
                self.visita(v)

    def Dijkstra(self, origem):
        fonte = self.buscaVertice(origem)
        if fonte is None:
            return None
        self.inicializaFonte(fonte)
        lista = []
        resposta = []
        for i in self.vertices:
            lista.append(i)
        while len(lista) != 0:
            lista.sort(key=lambda u: u.estim)
            u = lista[0]
            v = self.buscaAdjacente(u)
            if v is None:
                for i in self.vertices:
                    i.setVisitado(False)
                self.tempo += 1
                u.setInput(self.tempo)
                resposta.append(lista[0])
                lista.pop(0)
            else:
                w = self.buscaAresta(u, v)
                if w is not None:
                    self.relaxaVertice(u, v, w)

        return resposta

    def eh_Ponto(self, u):
        for v in self.vertices:
            v.setVisitado(False)
        u.setVisitado(True)
        self.visita(self.buscaAdjacente(u))
        for v in self.vertices:
            if v.getVisitado() == False:
                return True
    
    def pontosArticulacao(self):
        art = []
        for u in self.vertices:
            if self.eh_Ponto(u):
                art.append(u.getId())
        return art

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
