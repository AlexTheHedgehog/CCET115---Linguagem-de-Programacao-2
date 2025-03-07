#ok
#Ficou legal com dicionário nas disciplinas

class AlunoDisciplina:
    def __init__(self):
        pass

    def matricular_aluno(self, aluno, disciplina, nota):
        aluno.disciplinas_e_notas[disciplina] = nota
        disciplina.alunos.append(aluno)

    def listar_alunos_por_disciplina(self, disciplina):
        if disciplina.alunos:
            print(f'Alunos da disciplina {disciplina.nome}:\n')
            soma = 0

            for i in disciplina.alunos:
                soma += i.disciplinas_e_notas[disciplina]
                print(i.nome)

            print(f'Média dos alunos dessa disciplina: {soma / len(disciplina.alunos)}\n')
        else:
            print('Não há alunos matriculados nessa disciplina.')

    def listar_disciplinas_por_aluno(self, aluno):
        if aluno.disciplinas_e_notas:
            print(f'Disciplinas em que o aluno {aluno.nome} está matriculado:\n')
            soma = 0

            for i in aluno.disciplinas_e_notas.keys():
                soma += aluno.disciplinas_e_notas[i]
                print(i.nome)

            print(f'Média do aluno em relação a estas disciplinas: {soma / len(aluno.disciplinas_e_notas)}')
        else:
            print('Esse aluno não está matriculado em nenhuma disciplina.')

    def remover_matricula(self, aluno, disciplina):
        aluno.disciplinas_e_notas.pop(disciplina)
        disciplina.alunos.remove(aluno)