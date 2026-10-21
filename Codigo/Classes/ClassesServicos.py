from Codigo.Classes.ClassesEntidades import MonitoriaMateria, Reserva

class SistemaMonitoria:
  def __init__(self, monitorias=None, reservas=None):
    self.monitorias = monitorias if monitorias is not None else []
    self.reservas = reservas if reservas is not None else []

  def _buscar_monitoria(self, nome_disciplina):
    for monitoria in self.monitorias:
      if monitoria.disciplina == nome_disciplina:
        return monitoria
    raise ValueError(f"Disciplina '{nome_disciplina}' não possui monitoria cadastrada.")

  def ListarDisciplinas(self):
    return [m.disciplina for m in self.monitorias]

  def HorariosDisponiveis(self, nome_disciplina):
    monitoria = self._buscar_monitoria(nome_disciplina)
    return [h for h in monitoria.horarios if not h.reservado]

  def ReservarHorario(self, aluno, nome_da_disciplina, horario_da_reserva, topico_da_duvida):
    if not topico_da_duvida or not topico_da_duvida.strip():
      raise ValueError("É obrigatório informar o tópico da dúvida.")

    monitoria = self._buscar_monitoria(nome_da_disciplina)

    if horario_da_reserva not in monitoria.horarios:
      raise ValueError("Horário não pertence a esta disciplina.")
    if horario_da_reserva.reservado:
      raise ValueError("Horário já reservado.")

    reserva = Reserva(aluno, nome_da_disciplina, horario_da_reserva, topico_da_duvida)
    horario_da_reserva.reservado = True
    self.reservas.append(reserva)
    return reserva