import datetime

class Aluno:
  def __init__(self, nome, ra):
    self.nome = nome
    self.ra = ra
    
class Monitor:
  def __init__(self, nome, ra):
    self.nome = nome
    self.ra = ra
    

class MonitoriaMateria:
  def __init__(self, disciplina, monitor, horarios):
    self.disciplina = disciplina
    self.monitor = monitor
    self.horarios = horarios

class Reserva:
  def __init__(self, aluno, disciplina, horario, topico):
    self.aluno = aluno
    self.disciplina = disciplina
    self.horario = horario
    self.topico = topico

class Horario:
  def __init__(self, monitor, inicio, duracao_min = 30, reservado=False):
    self.monitor = monitor
    self.inicio = inicio
    self.duracao_min = duracao_min
    self.reservado = reservado