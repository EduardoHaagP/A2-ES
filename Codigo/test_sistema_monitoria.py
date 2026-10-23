
import unittest
import datetime
from Codigo.Classes.ClassesEntidades import Aluno, Monitor, MonitoriaMateria, Horario, Reserva
from Codigo.Classes.ClassesServicos import SistemaMonitoria

class TestSistemaMonitoria(unittest.TestCase):
    def setUp(self):
        # Setup inicial comum para a maioria dos testes
        self.aluno = Aluno("João", "123456")
        self.monitor = Monitor("Maria", "654321")
        
        # Criação de horários (um livre, um já reservado)
        self.horario_livre = Horario(self.monitor, datetime.datetime(2026, 10, 20, 14, 0))
        self.horario_reservado = Horario(self.monitor, datetime.datetime(2026, 10, 20, 15, 0), reservado=True)
        
        self.monitoria = MonitoriaMateria("Cálculo", self.monitor, [self.horario_livre, self.horario_reservado])
        self.sistema = SistemaMonitoria(monitorias=[self.monitoria])

    # Critério 1
    def test_listar_disciplinas_com_monitoria_retorna_lista_correta(self):
        disciplinas = self.sistema.ListarDisciplinas()
        self.assertEqual(disciplinas, ["Cálculo"])

    def test_listar_disciplinas_sem_monitorias_cadastradas_retorna_lista_vazia(self):
        sistema_vazio = SistemaMonitoria()
        self.assertEqual(sistema_vazio.ListarDisciplinas(), [])

    # Critério 2
    def test_exibir_apenas_horarios_nao_reservados(self):
        horarios = self.sistema.HorariosDisponiveis("Cálculo")
        self.assertEqual(len(horarios), 1)
        self.assertFalse(horarios[0].reservado)
        self.assertEqual(horarios[0].inicio, self.horario_livre.inicio)

    def test_consultar_horarios_disciplina_inexistente_lanca_excecao(self):
        with self.assertRaises(ValueError) as context:
            self.sistema.HorariosDisponiveis("Física")
        self.assertTrue("não possui monitoria cadastrada" in str(context.exception))

    # Critério 3
    def test_reserva_gerada_com_duracao_30min(self):
        reserva = self.sistema.ReservarHorario(self.aluno, "Cálculo", self.horario_livre, "Dúvida em derivadas")
        self.assertEqual(reserva.horario.duracao_min, 30)

    # Critério 4
    def test_reservar_horario_com_topico_valido_sucesso(self):
        reserva = self.sistema.ReservarHorario(self.aluno, "Cálculo", self.horario_livre, "Dúvida em integrais")
        self.assertEqual(reserva.topico, "Dúvida em integrais")
        self.assertTrue(reserva.horario.reservado)
        self.assertIn(reserva, self.sistema.reservas)

    def test_reservar_horario_sem_topico_lanca_excecao(self):
        with self.assertRaises(ValueError) as context:
            self.sistema.ReservarHorario(self.aluno, "Cálculo", self.horario_livre, "")
        self.assertEqual(str(context.exception), "É obrigatório informar o tópico da dúvida.")

if __name__ == '__main__':
    unittest.main()