import random

def rdado():

    return random.randrange(1,400000)

class Acao:
    def __init__(self, ticker):
        self.ticker = ticker

    ################################
    # Sessão para declaração de variáveis globais
    ################################

    values_ativo = {'ativo_circulante':0.0, 'caixa_equivalentes':0.0, 'contas_receber': 0.0, 'estoques':0.0, 'despesas_antecipadas':0.0,
    'realizavel_lp':0.0, 'ativos_operacionais':0.0, 'ativos_financeiros':0.0, 'ativo_nao_circulante':0.0, 'estoque_medio':0.0}
    values_passivo = {'passivo_circulante':0.0, 'fornecedores':0.0, 'tributos':0.0, 'obrigacoes_trabalhistas':0.0,'emprestimos_cp':0.0,'exigivel_lp':0.0,
    'passivos_operacionais': 0.0, 'passivos_financeiros':0.0, 'passivo_nao_circulante_e_pl':0.0}
    values_dre = {'receita_liquida':0.0, 'cmv':0.0}
    values_gerenciais = {'estoque_mat_prima':0.0, 'consumo_estoque':0.0, 'estoque_elaboracao':0.0, 'custo_producao':0.0, 'estoque_acabado':0.0,'cpv':0.0, 
    'duplicatas_receber': 0.0, 'vendas_prazo': 0.0, 'fornecedores_pagar': 0.0, 'compras_prazo':0.0}
    values_indicadores = {'liquidez_corrente':0.0,'liquidez_seca':0.0,'liquidez_imediata':0.0,'ncg':0.0, 'ccl':0.0, 'pme': 0.0,
    'pmf':0.0, 'pmv': 0.0, 'pmc':0.0, 'pmpf':0.0}
    
    ################################
    # Sessão relacionada a obtenção das contas contábeis que serão usadas no cálculos dos indicadores
    ################################


                #### Ativo ##### 

    def get_ativo_circulante(self): 
        """
        Obtém dados do ativo circulante - Aprimorar para detalhar o período de análise e coletar dados automaticamente.\n
        """
        self.values_ativo['ativo_circulante'] = rdado()

        return True

    def get_caixa_equivalentes(self): 
        """
        Obtém dados de caixa e equivalentes de caixa.\n
        """
        self.values_ativo['caixa_equivalentes'] = rdado()
        
        return True

    def get_contas_receber(self):
        """
        Obtém dados sobre contas a receber.\n
        """
        self.values_ativo['contas_receber'] = rdado()

        return True

    def get_estoques(self): 
        """
        Obtém dados sobre estoques.\n
        """
        self.values_ativo['estoques'] = rdado()
        return True

    def get_despesas_antecipadas(self): 
        """
        Obtém dados das despesas antecipadas.\n
        """
        self.values_ativo['despesas_antecipadas'] = rdado()
        return True

    def get_realizavel_lp(self): 
        """
        Obtém dados dos ativos realizáveis a longo prazo.\n
        """
        self.values_ativo['realizavel_lp'] = rdado()
        return True
    
    def get_ativos_operacionais(self):
        """
        Obtém dados dos ativos operacionais.\n
        """
        self.values_ativo['ativos_operacionais'] = (self.values_ativo['caixa_equivalentes'] / 1)+ self.values_ativo['contas_receber'] + self.values_ativo['estoques']
        return True


    def get_ativos_financeiros(self):
        """
        Obtém dados dos ativos financeiros.\n
        """
        self.values_ativo['ativos_financeiros'] = self.values_ativo['caixa_equivalentes'] + 0.0 # incluir demais contas (investimentos, etc)
        return True
    
    def get_ativo_nao_circulante(self):
        """
        Obtém dados dos ativos não circulantes.\n
        """
        self.values_ativo['ativo_nao_circulante'] = rdado()
        return True

                        ##### Passivo #####

    def get_passivo_circulante(self): 
        """
        Obtem dados do passivo circulante - Aprimorar para detalhar o período de análise e coletar dados automaticamente.\n
        """
        self.values_passivo['passivo_circulante'] = rdado()
        return True

    def get_fornecedores(self): 
        """
        Obtem dados da conta fornecedores - Aprimorar para detalhar o período de análise e coletar dados automaticamente.\n
        """
        self.values_passivo['fornecedores'] = rdado()
        return True

    def get_tributos(self): 
        """
        Obtem dados da conta tributos - Aprimorar para detalhar o período de análise e coletar dados automaticamente.\n
        """
        self.values_passivo['tributos'] = rdado()
        return True

    def get_obrigacoes_trabalhistas(self): 
        """
        Obtem dados da conta obrigações trabalhistas - Aprimorar para detalhar o período de análise e coletar dados automaticamente.\n
        """
        self.values_passivo['obrigacoes_trabalhistas'] = rdado()
        return True

    def get_emprestimos_cp(self):
        """
        Obtem dados da conta emprestimos e financiamentos de curto prazo - Aprimorar para detalhar o período de análise e coletar dados automaticamente.\n
        """
        self.values_passivo['emprestimos_cp'] = rdado()
        return True

    def get_exigivel_lp(self): 
        """
        Obtém dados do passivo exigível a longo prazo.\n
        """
        self.values_passivo['exigivel_lp'] = rdado()
        return True

    def get_passivos_operacionais(self):
        """
        Obtém dados dos passivos operacionais.\n
        """
        self.values_passivo['passivos_operacionais'] = self.values_passivo['fornecedores'] + self.values_passivo['obrigacoes_trabalhistas'] + self.values_passivo['tributos']
        return True

    def get_passivos_financeiros(self):
        """
        Obtém dados dos passivos financeiros.\n
        """
        self.values_passivo['passivos_financeiros'] = self.values_passivo['emprestimos_cp'] + 0.0 # incluir demais contas
        return True

    def get_passivo_nao_circulante_e_pl(self):
        """
        Obtém dados dos passivo não circulantes.\n
        """
        self.values_passivo['passivo_nao_circulante_e_pl'] = rdado()
        return True

                        ##### DRE #####
    
    def get_receita_liquida(self):
        """
        Obtém os dados da receita líquida.\n 
        """
        self.values_dre['receita_liquida'] = rdado()
        return True
    
    def get_cmv(self):
        """
        Obtém dados do CMV (Custo da Mercadoria Vendida).\n
        """
        self.values_dre['cmv'] = rdado()
        return True


                        ######## Valores Gerenciais #######

    
    def get_estoque_mat_prima(self):
        """
        Obtém dados gerenciais do estoque médio de matéria prima.\n
        """
        self.values_gerenciais['estoque_mat_prima'] = rdado()
        return True

    def get_consumo_estoque(self):
        """
        Obtém dados gerenciais do consumo médio de estoques de materia prima.\n
        """
        self.values_gerenciais['consumo_estoque'] = rdado()
        return True

    def get_estoque_elaboracao(self):
        """
        Obtém dados gerenciais do estoque médio de produtos em elaboração.\n
        """
        self.values_gerenciais['estoque_elaboracao'] = rdado()
        return True
    
    def get_custo_producao(self):
        """
        Obtém dados gerenciais do custo médio de produção.\n
        """
        self.values_gerenciais['custo_producao'] = rdado()
        return True

    def get_estoque_acabado(self):
        """
        Obtém dados gerenciais do estoque médio de produtos acabados.\n
        """
        self.values_gerenciais['estoque_acabado'] = rdado()
        return True

    def get_duplicatas_receber(self):
        """
        Obtém dados gerenciais do saldo médio das duplicatas a receber.\n
        """
        self.values_gerenciais['duplicatas_receber'] = rdado()
        return True

    def get_vendas_prazo(self):
        """
        Obtém dados gerenciais ...
        """


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
        self.values_indicadores = self.values_gerenciais['estoque_acabado'] / self.values_gerenciais['cpv']
        return True
    
    def get_pmc(self):
        """
        Obtém o prazo médio de recebimento dos produtos vendidos.\n
        """
        self.values_indicadores['pmc'] = self.values_gerenciais['duplicatas_receber'] / self.values_gerenciais['vendas_prazo']
        return True
    
    def get_pmpf(self):
        """
        Obtém o prazo médio de pagamento a fornecedores.\n
        """
        self.values_indicadores['pmpf'] = self.values_gerenciais['fornecedores_pagar'] / self.values_gerenciais['compras_prazo']
        return True


    ################################
    # Sessão relacionada à carregamento de valores
    ################################

    def get_values(self):
        """
        Carrega valores envolvidos na análise.\n
        """

        ################################ Ativo #############################

        self.get_ativo_circulante()
        self.get_caixa_equivalentes()
        self.get_estoques()
        self.get_contas_receber()
        self.get_despesas_antecipadas()
        self.get_ativo_nao_circulante()
        self.get_ativos_financeiros()
        self.get_ativos_operacionais()
        

        ################################ Passivo #############################

        self.get_passivo_circulante()
        self.get_fornecedores()
        self.get_tributos()
        self.get_obrigacoes_trabalhistas()
        self.get_exigivel_lp()
        self.get_passivo_nao_circulante_e_pl()
        self.get_passivos_operacionais()
        self.get_passivos_financeiros()

        ################################ DRE #############################
        
        self.get_receita_liquida()
        self.get_cmv()

        ################################ Indicadores Liquidez #############################

        self.get_liquidez_corrente()
        self.get_liquidez_imediata()
        self.get_liquidez_seca()

        ################################ Indicadores de Capital de Giro #############################

        self.get_ncg()
        self.get_ccl()

        return True



   