import datetime
import calendar

def create_calendar(final_date):
    """
    Cria lista de dias contendo cada dia, desde o atual até o final_date informado pela instância.\n
    """
    # Cria objeto da classe datetime para obter dados da data atual. 
    current_day = datetime.datetime

    # Cria lista que receberá dias
    calendario = calendar.Calendar()

    # Calcula o range de dias entre as datas em questão
    days = final_date - current_day.today().date() #pylint: disable= unused-variable
    
    # Atravessa o range adicionando á lista um elemento de dia
    

    return calendario

dia = datetime.datetime
ativo = {}
ticker = 'BOVAS89'
vencimento = datetime.date(2020, 7, 20)
ativo = {'Ticker': ticker, 'Vencimento':vencimento}
print(vencimento)
calendario = create_calendar(vencimento)


for c in ativo:
    if 'Ticker' in c:
        print(ativo[c])

print(dia.today().date())