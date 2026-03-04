from aigyminsper.search.search_algorithms import BuscaLargura, BuscaProfundidade
from aigyminsper.search.graph import State

class AspiradorPo(State):

    def __init__(self, op, posicao_robo, condicao_d1="sujo", condicao_d2="sujo", condicao_d3="sujo", condicao_d4="sujo"):
        # voce sempre deve usar esta chamada para inicializar a superclasse
        super().__init__(op)
        # recebe (0,0), (1,0), (1,1), (0,1)
        self.posicao_robo = posicao_robo
        # recebe limpo ou sujo
        self.condicao_d1 = condicao_d1
        # recebe limpo ou sujo
        self.condicao_d2 = condicao_d2
        # recebe limpo ou sujo
        self.condicao_d3 = condicao_d3
        # recebe limpo ou sujo
        self.condicao_d4 = condicao_d4
    
    def successors(self):
        successors = []
        x,y = self.posicao_robo
        #consequência de ir para esq
        if x==1:
            successors.append(AspiradorPo('ir para esq', (x-1, y), self.condicao_d1, self.condicao_d2, self.condicao_d3, self.condicao_d4))
        #consequência de ir para dir
        if x==0:
            successors.append(AspiradorPo('ir para dir', (x+1, y), self.condicao_d1, self.condicao_d2, self.condicao_d3, self.condicao_d4))
        #consequência de ir para dir
        if y==0:
            successors.append(AspiradorPo('ir para cima', (x, y+1), self.condicao_d1, self.condicao_d2, self.condicao_d3, self.condicao_d4))
        if y==1:
        #consequência de ir para 
            successors.append(AspiradorPo('ir para baixo', (x, y-1), self.condicao_d1, self.condicao_d2, self.condicao_d3, self.condicao_d4))

        #consequência de limpar
        if self.posicao_robo == (0,0):
            successors.append(AspiradorPo('limpar', self.posicao_robo, "limpo", self.condicao_d2, self.condicao_d3, self.condicao_d4))
        elif self.posicao_robo == (1,0):
            successors.append(AspiradorPo('limpar', self.posicao_robo, self.condicao_d1, "limpo", self.condicao_d3, self.condicao_d4))
        elif self.posicao_robo == (0,1):
            successors.append(AspiradorPo('limpar', self.posicao_robo, self.condicao_d1, self.condicao_d2, "limpo", self.condicao_d4))
        elif self.posicao_robo == (1,1):
            successors.append(AspiradorPo('limpar', self.posicao_robo, self.condicao_d1, self.condicao_d2, self.condicao_d3, "limpo"))



        return successors
    
    def is_goal(self):
        return self.condicao_d1 == "limpo" and self.condicao_d2 == "limpo" and self.condicao_d3 == "limpo" and self.condicao_d4 == "limpo"
    
    def description(self):
        return "O aspirador deve limpar os cômodos que estão sujos"
    
    def cost(self):
        return 1
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None

def main():
    print('Busca em largura')
    state = AspiradorPo('', (0,0), 'sujo', 'sujo', 'sujo', 'sujo')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nâo achou solucao')

if __name__ == '__main__':
    main()