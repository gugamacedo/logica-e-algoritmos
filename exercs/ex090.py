# Leia o nome e média de um aluno, guardando também o status em um dicionário. No final exiba tudo
student = {}
student['Nome'] = str(input('Nome do aluno: ')).title()
student['Média'] = float(input('Média tirada: '))
if student['Média'] < 7:
    student['Status'] = 'Reprovado'
else:
    student['Status'] = 'Aprovado'
    
print()
for k, v in student.items():
    print(f'{k} = {v}')
