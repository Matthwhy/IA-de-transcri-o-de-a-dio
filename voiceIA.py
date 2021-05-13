import speech_recognition as sr

def recon(reconhecedor,microfone):
    with microfone as somprincipal:
        reconhecedor.adjust_for_ambient_noise(somprincipal)
        audio = reconhecedor.listen(somprincipal)

    response = {
        "sucesso": True,
        "erro": None,
        "transcricao":None
    }

    try:
        response["transcricao"] = reconhecedor.recognize_google(audio, language='pt-BR')
    
    except sr.RequestError:
        response["sucesso"] = False
        response["erro"] = "API não disponivel"
    
    except sr.UnknownValueError:
        response["erro"] = "Não entendi sua fala"
    
    return response

if __name__ == "__main__":
    reconhecedor = sr.Recognizer()
    microfone = sr.Microphone()

    NFALA = 10
    NSEMFALA = 10

    print('\n### Programa funcionando ###')

    for i in range(NFALA):
        for j in range(NSEMFALA):
            print('\n TESTE {} - Fale no microfone \n'.format(i+1))

            somteste = recon(reconhecedor, microfone)

            if somteste["transcricao"]:
                break
            if not somteste["sucesso"]:
                break
            print("Eu não entendi. repita\n")

        if somteste["erro"]:
            print("erro: {} \n".format(somteste["erro"]))

        print("Voce disse: {}".format(somteste["transcricao"]))