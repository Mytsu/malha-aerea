from grafo import Grafo

class Malha:
    def __init__(self):
        self.voos = Grafo.Grafo(True)
        self.rotas = Grafo.Grafo()

    # questao 1
    def load(self, fileName = 'map.txt'):
        try:
            with open(fileName, 'r') as arq:
                for linha in arq:
                    v1, v2, peso = linha.split(' ')
                    if self.voos.buscaVertice(v1) is None:
                        self.voos.addVertice(v1)
                        self.rotas.addVertice(v1)
                    if self.voos.buscaVertice(v2) is None:
                        self.voos.addVertice(v2)
                        self.rotas.addVertice(v2)
                    if self.voos.buscaAresta(v1, v2) is None:
                        self.voos.addAresta(v1, v2, peso)
                        self.rotas.addAresta(v1, v2, peso)
        except Exception as e:
            raise e

    # questao 2
    def voosDiretos(self, v):
        conexoes = self.voos.conexoes(v)
        print('Voos diretos que partem do aeroporto %s:' % v)
        for i in conexoes:
            print('Aeroporto: %s \t Tempo de Voo: %s' % i[1] % i[0])

    # questao 3
    def menorCaminho(self, v1, v2):
        print('Menor caminho em termos de tempo de voo:')
        lista = self.voos.buscaLargura(v1, v2)
        s = ''
        for v in lista:
           s += str(v.getId()) + ' -> '
        print(s)
        print('Menor caminho em termos de distancia percorrida:')
        lista = self.rotas.buscaLargura(v1, v2)
        s = ''
        for v in lista:
           s += str(v.getId()) + ' -> '
        print(s)
        return lista

    # questao 5
    def problemaCaixeiro(self, inicio):
        print('Menor caminho que passa por todos os Aeroportos:')
        lista = self.voos.Dijkstra(inicio)
        s = ''
        for v in lista:
            s += str(v.getId()) + ' -> '
        print(s)