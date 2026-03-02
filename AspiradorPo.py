from aigyminsper.search.search_algorithms import BuscaLargura, BuscaProfundidade
from aigyminsper.search.graph import State

class AspiradorPo(State):

    def __init__(self, op, posicao_robo, condicao_esq="sujo", condicao_dir="sujo"):
        # voce sempre deve usar esta chamada para inicializar a superclasse
        super().__init__(op)
        # recebe esquerda ou direita
        self.posicao_robo = posicao_robo
        # recebe limpo ou sujo
        self.condicao_esq = condicao_esq
        # recebe limpo ou sujo
        self.condicao_dir = condicao_dir
    
    def successors(self):
        successors = []

        #consequência de ir para esq
        successors.append(AspiradorPo('ir para esq', 'esq', self.condicao_esq, self.condicao_dir))
        #consequência de ir para dir
        successors.append(AspiradorPo('ir para dir', 'dir', self.condicao_esq, self.condicao_dir))

        #consequência de limpar
        if self.posicao_robo == "esq":
            successors.append(AspiradorPo('limpar', self.posicao_robo, "limpo", self.condicao_dir))
        elif self.posicao_robo == "dir":
            successors.append(AspiradorPo('limpar', self.posicao_robo, self.condicao_esq, "limpo"))



        return successors
    
    def is_goal(self):
        return self.condicao_dir == "limpo" and self.condicao_esq == "limpo"
    
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
    state = AspiradorPo('', 'esq', 'sujo', 'sujo')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nâo achou solucao')

if __name__ == '__main__':
    main()