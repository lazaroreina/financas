import random

def rdado():

    return random.randrange(1,400000)

class Acao:
    def __init__(self, ticker):
        self.ticker = ticker

    def privateimput(self, key):
        return float(input('Digite a variável {}: '.format(key)))
       
    ################################
    # Sessão para declaração de variáveis globais
    ################################

    values_ativo = {'ativo_circulante':0.0, 'caixa_equivalentes':0.0, 'contas_receber': 0.0, 'estoques':0.0, 'despesas_antecipadas':0.0,
    'realizavel_lp':0.0, 'ativos_operacionais':0.0, 'ativos_financeiros':0.0, 'ativo_nao_circulante':0.0, 'estoque_medio':0.0}
    values_passivo = {'passivo_circulante':0.0, 'fornecedores':0.0, 'tributos':0.0, 'obrigacoes_trabalhistas':0.0,'emprestimos_cp':0.0,'exigivel_lp':0.0,
    'passivos_operacionais': 0.0, 'passivos_financeiros':0.0, 'passivo_nao_circulante_e_pl':0.0}
    values_dre = {'receita_liquida':0.0, 'cmv':0.0}
    values_gerenciais = {'estoque_mat_prima':0.0, 'consumo_estoque':0.0, 'estoque_elaboracao':0.0, 'custo_producao':0.0, 'estoque_acabado':0.0,'cpv':0.0, 
    'duplicatas_receber_media': 0.0, 'vendas_prazo': 0.0, 'fornecedores_pagar': 0.0, 'compras_prazo':0.0}
    values_indicadores = {'liquidez_corrente':0.0,'liquidez_seca':0.0,'liquidez_imediata':0.0,'ncg':0.0, 'ccl':0.0, 'pme': 0.0,
    'pmf':0.0, 'pmv': 0.0, 'pmc':0.0, 'pmpf':0.0}
    
    ################################
    # Sessão relacionada a obtenção das contas contábeis e valores gerenciais que serão usadas no cálculos dos indicadores
    ################################

    def get_values(self):
        """
        Carrega valores envolvidos na análise.\n
        """

        ################################ Ativo #############################

        print('Carregando dados do ativo: ')
        for c in self.values_ativo:
            self.values_ativo[c] = self.privateimput(c)

        ################################ Passivo #############################

        print('Carregando dados do passivo:')    
        for c in self.values_passivo:
            self.values_passivo[c] = self.privateimput(c)

        ################################ DRE #############################
        
        print('Carregando dados da DRE: ')
        for c in self.values_dre:
            self.values_dre[c] = self.privateimput(c)

        ################################ Valores Gerenciais ##############################    

        print('Carregando dados gerenciais: ')
        for c in self.values_gerenciais:
            self.values_gerenciais[c] = self.privateimput(c)

    ################################
    # Sessão relacionada ao cálculo dos indicadores
    ################################

                #### Indicadores de liquidez ####

    def get_liquidez_corrente(self):
        """
        Obtem a liquidez corrente da empresa - Aprimorar para detalhar o período de análise.\n
        """
        self.values_indicadores['liquidez_corrente'] = self.values_ativo['ativo_circulante'] / self.values_passivo['passivo_circulante']
        return True

    def get_liquidez_imediata(self): 
        """
        Obtém a liquidez imediata da empresa - Aprimorar para detalhar o perído de análise.\n
        """
        self.values_indicadores['liquidez_imediata'] = self.values_ativo['caixa_equivalentes'] / self.values_passivo['passivo_circulante']
        return True

    def get_liquidez_seca(self):
        """
        Obtém a liquidez seca.\n
        """
        self.values_indicadores['liquidez_seca'] = (self.values_ativo['ativo_circulante'] - self.values_ativo['estoques']) / self.values_passivo['passivo_circulante']
        return True

                ######## Indicadores de capital de giro ########
    

    def get_ncg(self):
        """
        Obtém a Necessidade de Capital de Giro.\n
        """
        self.values_indicadores['ncg'] = self.values_ativo['ativos_operacionais'] - self.values_passivo['passivos_operacionais']
        return True

    def get_ccl(self): 
        """
        Obtém o Capital Circulante Líquido.\n
        """
        self.values_indicadores['ccl'] = self.values_ativo['ativo_circulante'] - self.values_passivo['passivo_circulante']
        return True

                ######## Indicadores de prazos médios operacionais ########

    def get_pme(self): 
        """
        Obtém o prazo médio de estocagem de matéria-prima.\n
        """
        self.values_indicadores['pme'] = self.values_gerenciais['estoque_mat_prima'] / self.values_gerenciais['consumo_estoque']
        return True

    def get_pmf(self):
        """
        Obtém o prazo médio de fabricação do produto final.\n
        """
        self.values_indicadores['pmf'] = self.values_gerenciais['estoque_elaboracao'] / self.values_gerenciais['custo_producao']
        return True
    
    def get_pmv(self):
        """
        Obtém o prazo médio de estocagem de produtos acabados.\n
        """
        self.values_indicadores['pmv'] = self.values_gerenciais['estoque_acabado'] / self.values_gerenciais['cpv']
        return True
    
    def get_pmc(self):
        """
        Obtém o prazo médio de recebimento dos produtos vendidos.\n
        """
        self.values_indicadores['pmc'] = self.values_gerenciais['duplicatas_receber_media'] / self.values_gerenciais['vendas_prazo']
        return True
    
    def get_pmpf(self):
        """
        Obtém o prazo médio de pagamento a fornecedores.\n
        """
        self.values_indicadores['pmpf'] = self.values_gerenciais['fornecedores_pagar'] / self.values_gerenciais['compras_prazo']
        return True


    ################################
    # Sessão relacionada ao carregamento dos indicadores
    ################################
    def get_indicadores(self):
    

        ################################ Indicadores Liquidez #############################

        self.get_liquidez_corrente()
        self.get_liquidez_imediata()
        self.get_liquidez_seca()

        ################################ Indicadores de Capital de Giro #############################

        self.get_ncg()
        self.get_ccl()

        ############################ Indicadores de Prazos Médios ################################

        self.get_pme()
        self.get_pmf()
        self.get_pmv()
        self.get_pmc()
        self.get_pmpf()

        return True



   