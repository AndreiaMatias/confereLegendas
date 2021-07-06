def revisa_legendas():

    tratamento = {}
    revisar = {}

    #Solicita caminho do arquivo:
    arquivo = input("Informe o caminho completo do arquivo de legendagem: ")
    if '\\' in arquivo:
        arquivo.replace('\\', '/')
    #Abre o arquivo
    with open(arquivo, encoding="utf8") as subtitle:
        subtitles = subtitle.read().splitlines()


    i = 1

    #percorre cada legenda e cria dicionário contendo o número dela e o tamanho de cada linha.
    for sub in subtitles:
        if len(sub)>0 and sub[0] == '[' and sub[1].isdigit():
            list_sub = []
            tratamento[i] = ""
            i += 1
        elif len(sub)>0:
            list_sub.append(len(sub))
        tratamento[(i - 1)] = list_sub

    revisao = False

    #se uma linha tiver tamanho inferior a 50% da outra, suas informações são incluídas na variável revisar e a variável revisao se torna verdadeira.
    for k, v in tratamento.items():
        if len(v) > 1:
            if v[0] == v[1]:
                pass
            elif v[0] > v[1]:
                if (v[1]/v[0]) < 0.5:
                    revisao = True
                    revisar[k] = v[1]/v[0]*100
            else:
                if (v[0]/v[1]) < 0.5:
                    revisao = True
                    revisar[k] = v[0]/v[1]*100

    # Se houver legendas a revisar, apresenta o número delas e o percentual em relação à outra linha.
    if revisao == False:
        print("Não há legendas a revisar.")
    else:
        print("Verifique as seguintes legendas:")
        for k, v in revisar.items():
            print(f"Legenda nº{k}:\t {v:.2f}")

revisa_legendas()