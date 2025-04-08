from boletim import Boletim

alunos = open('alunos.txt', 'r', encoding='utf-8')
notas = open('notas.txt', 'r', encoding='utf-8')

Boletim.alunos_e_notas(alunos, notas)

alunos.close()
notas.close()

boletim = open('novo.txt', 'r', encoding='utf-8')
Boletim.ordenar(boletim)
boletim.close()