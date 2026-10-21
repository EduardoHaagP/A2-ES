# Projeto Inicial — História de Prioridade Alta — Passo 5
---

## 1. Mapeamento de Classes e Responsabilidades

### Classes de Entidade

* **`Aluno`**: Representa o estudante que solicita a monitoria (`nome`, `ra`).
* **`Monitor`**: Representa o aluno monitor responsável pelo atendimento (`nome`, `ra`).
* **`Horario`**: Define a disponibilidade oferecida pelo monitor (`monitor`, `inicio`, `duracao_min = 30`, `reservado`).
* **`MonitoriaMateria`**: Associa uma disciplina ao seu monitor e à lista de horários oferecidos (`disciplina`, `monitor`, `horarios`).
* **`Reserva`**: Registra o agendamento efetuado (`aluno`, `disciplina`, `horario`, `topico`).

### Classe de Serviço

* **`SistemaMonitoria`**: Classe principal que gerencia o catálogo de monitorias e a lista de reservas do sistema (`monitorias`, `reservas`).
  * `ListarDisciplinas()`: Retorna a lista de nomes de disciplinas que possuem monitorias cadastradas.
  * `HorariosDisponiveis(nome_da_materia)`: Consulta e retorna os horários livres (não reservados) para a disciplina informada.
  * `ReservarHorario(aluno, nome_da_materia, horario_da_reserva, topico_da_duvida)`: Valida os dados, gera uma instância de `Reserva` com duração fixa de 30 minutos, atualiza o status do horário e o adiciona ao sistema.

---

## 2. Mapeamento de Critérios de Aceitação × Métodos × Testes (`unittest`)

### Critério 1: Sistema deve listar as disciplinas com monitoria disponível
* **Método Responsável**: `SistemaMonitoria.ListarDisciplinas()`
* **Caso de Sucesso**: `test_listar_disciplinas_com_monitoria_retorna_lista_correta()`  
  Verifica se o sistema retorna as disciplinas que possuem horários cadastrados.
* **Caso de Exceção/Falha**: `test_listar_disciplinas_sem_monitorias_cadastradas_retorna_lista_vazia()`  
  Verifica o comportamento do sistema quando não há disciplinas registradas.

### Critério 2: Sistema deve exibir apenas horários disponíveis (livres e não reservados)
* **Método Responsável**: `SistemaMonitoria.HorariosDisponiveis()`
* **Caso de Sucesso**: `test_exibir_apenas_horarios_nao_reservados()`  
  Garante que horários com `reservado = True` não aparecem na consulta.
* **Caso de Exceção/Falha**: `test_consultar_horarios_disciplina_inexistente_lanca_excecao()`  
  Garante que tentar buscar horários de uma matéria não cadastrada gera um erro/mensagem apropriada.

### Critério 3: Reserva gerada deve ter duração fixa de 30 min
* **Método Responsável**: `SistemaMonitoria.ReservarHorario()` e atributo `Horario.duracao_min`
* **Caso de Sucesso**: `test_reserva_gerada_com_duracao_30min()`  
  Confirma que o objeto `Reserva` criado herda ou define exatamente a duração fixa de 30 minutos.

### Critério 4: Informar o tópico da dúvida
* **Método Responsável**: `SistemaMonitoria.ReservarHorario()`
* **Caso de Sucesso**: `test_reservar_horario_com_topico_valido_sucesso()`  
  Confirma que a reserva é gravada corretamente com a string do tópico fornecida.
* **Caso de Exceção/Falha**: `test_reservar_horario_sem_topico_lanca_excecao()`  
  Verifica que a tentativa de reserva sem informar a dúvida (tópico vazio) é rejeitada pelo sistema.