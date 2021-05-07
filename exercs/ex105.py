# notas() pode receber várias notas de alunos, e vai retornar um dicionário com as seguintes informações:
# quantidade de notas, a maior e menor nota, média e status (opcional)
def notas(*n, status=False):
    alunos = {
        'Qtd notas': len(n),
        'Maior nota': max(n),
        'Menor nota': min(n),
        'Média notas': round(sum(n)/len(n), 2)
    }
    if status:
        if alunos['Média notas'] >= 7:
            alunos['Status'] = 'Aprovado'
        elif alunos['Média notas'] >= 5:
            alunos['Status'] = 'Recuperação'
        else:
            alunos['Status'] = 'Reprovado'
    return alunos

resp = notas(5, 8, 3, 3, status=True)
for k, v in resp.items():
    print(f'{k}: {v}')
