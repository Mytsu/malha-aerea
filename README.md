# Trabalho de Estrutura de Dados II

##### Instituto Federal de Minas Gerais

##### Jonathan Arantes - 0021625

__

## Sobre o projeto

Esta é uma implementação de uma malha aérea que deve tratar o controle de voos de uma companhia aérea; 

Este projeto deve atender os requisitos básicos:

1. Construir uma estrutura de dados que suporte dois grafos, o das rotas e o dos voos, os quais partilham os vértices, os aeroportos. O grafo dos voos terá apenas uma aresta para cada par (origem, destino), funcionando os respectivos voos como alternativas. Podem existir vários pesos associáveis a arestas: distância, número de paradas e duração. A interface deve incluir:

    - associar dados a partir de um arquivo sobre voos do território Brasileiro, com aeroportos, rotas e voos (considere as coordenadas indicadas em dezenas de Km);

    - representar (demonstrar) graficamente as rotas (ligações entre aeroportos), os voos, ou ambos;

    - para dois aeroportos dados mostrar o caminho como uma sequência de aeroportos, quer no grafo das rotas, quer no dos voos.

2. Mostrar, a partir de um aeroporto definido, quais os voos diretos (sem escalas e/ou conexões) que partem dele e a lista desses destinos.

3. Dados uma origem e um destino, desenvolver um algoritmo para determinar a viagem com menor custo em termos de: distância total a percorrer e tempo de voo.

4. Desenvolver um algoritmo para determinar se é possível, a partir de um aeroporto qualquer atingir qualquer outro (ou se será necessário em alguns casos fazer troca de aeroporto) e quais os aeroportos que, se ficassem fora de serviço (apenas um de cada vez), impediriam essa situação.

5. Partindo de um aeroporto selecionado definir uma rota que consiga passar por todos os aeroportos com um tempo de voo mínimo.