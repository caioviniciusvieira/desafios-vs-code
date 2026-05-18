def calcular_notas (soma, nome):
    i = 0
    for nota in range(3):
        i+=1
        nota = float(input(f"informe a {i}º nota do aluno - {nome}:"))
        soma += nota
    return soma 
   
def calcular_maior_media(media, nome, maior,alunoMaiorMedia):
    if media > maior:
        maior = media
        aluno_maior_media = nome
        print(aluno_maior_media)
        return maior, aluno_maior_media
    else:
        aluno_maior_media = alunoMaiorMedia
        print(aluno_maior_media)
        return maior, aluno_maior_media   
    
def boletim():
    aprovados = []
    reprovados = []
    medias = []
    quant_alunos = int(input("Informe a quantidade de alunos: "))
    contador_alunos=0
    maior_media = 0
    alunoMaiorMedia = ''
    
    for aluno in range(quant_alunos):
        soma_notas = 0
        contador_alunos+=1
        aluno = input(f"Informe o nome do {contador_alunos}º aluno:")
        soma_notas = calcular_notas(soma_notas, aluno)
        media = soma_notas/3
        if media >= 7:
            aprovados.append(aluno)
            medias.append(media)
        else:
            reprovados.append(aluno)
            medias.append(media)
                
        maior_media, alunoMaiorMedia = calcular_maior_media(media, aluno, maior_media,alunoMaiorMedia)
            
    print("Alunos aprovados:",aprovados)
    print("Alunos reprovados:",reprovados)
    print("Medias dos alunos:",medias)
    print("Maior média:",maior_media)
    print("Aluno com a maior média:",alunoMaiorMedia)

boletim()
