# Manipular data e hora, conversão de texto para data e vice versa, soma e subtração em datas

from datetime import date, time, datetime, timedelta #consigo trazer a data atual

def trabalhando_com_date():
    data_atual = date.today() # tipo datetime.date
    print(data_atual.strftime('%d/%m/%y')) # Com o strftime consigo trazer a data para o nosso padrão utilizando as diretvas do python
    # tipo string
    print(data_atual.strftime('%d/%m/%Y')) # Com 'Y' traz o ano completo
    print(data_atual.strftime('%A %B %Y')) # 'A' tras o dia 'B' o mês

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(type(horario)) #datetime.time
    print(horario)
    horariostr = horario.strftime('%H:%M:%S') # tipo string
    print(type(horariostr))
    print(horario)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y')) # Pego somente o dia
    print(data_atual.strftime('%H:%M:%S')) # Pego somente a hora
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S')) # Pego data e hora convertida
    print(data_atual.strftime('%c')) # Tras a data completa somente com uma letra
    print(data_atual.day) # Somente o dia
    print(data_atual.year)  # Somente o ano
    print(data_atual.hour)  # Somente a hora
    print(data_atual.minute)  # Somente o minuto
    print(data_atual.date())  # Somente a data
    print(data_atual.weekday())  # Dia da semana
    print(data_atual.month)  # Somente o mes

    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta',
             'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])

    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(type(data_convertida))

    #com time e delta posso efetuar contas com datas
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)
    nova_data = data_convertida - timedelta(hours=2)
    print(nova_data)
    nova_data = data_convertida - timedelta(minutes=15)
    print(nova_data)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)
    nova_data = data_convertida + timedelta(days=365, hours=2, minutes=15)
    print(nova_data)


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()