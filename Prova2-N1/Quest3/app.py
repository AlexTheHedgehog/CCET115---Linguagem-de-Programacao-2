#ok
#100%
from aluno import Aluno
from disciplina import Disciplina
from aluno_disciplina import AlunoDisciplina

aluno1 = Aluno('Daniel Gomes Chaves', 'chavesdaniel462@gmail.com')
aluno2 = Aluno('Fulano da Silva', 'daniel.chaves@sou.ufac.br')
aluno3 = Aluno('Ciclano Vieira', 'ablabla.blabla@sou.ufac.br')
aluno4 = Aluno('Beltrano Oliveira', 'beltrano.demais@sou.ufac.br')

disciplina1 = Disciplina('Linguagem de Programação I', 'LPI')
disciplina2 = Disciplina('Linguagem de Programação II', 'LPII')
disciplina3 = Disciplina('Algoritmos', 'ALG')

faculdade = AlunoDisciplina()

faculdade.matricular_aluno(aluno1, disciplina2, 10)
faculdade.matricular_aluno(aluno2, disciplina1, 5)
faculdade.matricular_aluno(aluno3, disciplina2, 3.5)
faculdade.matricular_aluno(aluno4, disciplina1, 9.6)
faculdade.matricular_aluno(aluno1, disciplina3, 5)

faculdade.listar_alunos_por_disciplina(disciplina1)
faculdade.listar_alunos_por_disciplina(disciplina2)

faculdade.listar_disciplinas_por_aluno(aluno1)

faculdade.remover_matricula(aluno1, disciplina3)

faculdade.listar_alunos_por_disciplina(disciplina3)