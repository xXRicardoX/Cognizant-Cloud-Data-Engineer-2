#utilizar informações de data, horário e relacionar datas diferentes
from datetime import date, time, datetime,timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c')) #similar ao print anterior
    print(data_atual.weekday()) #pode colocar tambem algum mes, hora especificamente
    tupla = ('Segunda', 'Tedça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo') #Traduzir do dia da semana em portugues
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20,  15,30,20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/1985 12:45:45' #converter tipo string para datetime
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S') #o ano sempre maiusculo
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2)#timedelta usando para fazer a subtraçao de dias
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%Y')#strftime e comando para que eu possa converter o jeito que é exibido
    print(data_atual)
    print(data_atual_str)
    print(type(data_atual))
    print(type(data_atual_str))

def trablhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario.strftime('%H:%M:%S')))
if __name__ == '__main__':
    trabalhando_com_date()
    trablhando_com_time()
    trabalhando_com_datetime()