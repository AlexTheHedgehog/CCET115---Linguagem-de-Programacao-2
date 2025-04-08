class Boletim:
    @staticmethod
    def alunos_e_notas(arq1, arq2):
        alunos = list(arq1.read().split('\n'))
        notas = list(arq2.read().split('\n'))
        medias = [f'{(sum([float(j) for j in list(i.split())]) / len(i.split())):.1f}' for i in notas]
        alunos_e_notas = '\n'.join([f'Média do aluno {alunos[i]}: {medias[i]}' for i in range(len(alunos))])
        novo = open('novo.txt', 'w', encoding='utf-8')
        novo.write(alunos_e_notas)
        novo.close()

    @staticmethod
    def ordenar(arq):
        linhas = list(arq.read().split('\n'))
        medias = [float(i) for i in [j.split()[-1] for j in linhas]]
        alunos_em_ordem = []
        
        for i in set(medias):
            alunos_com_essa_nota = [j for j in linhas if str(i) in j]
            for j in alunos_com_essa_nota:
                alunos_em_ordem.append(j)
             
        
        print('\n'.join(alunos_em_ordem))