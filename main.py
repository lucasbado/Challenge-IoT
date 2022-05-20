import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import os.path

#Declarar as variáveis
recon = sr.Recognizer()
resposta = ""
parar = False
#converter o resultado da hora em string
hora = (str(datetime.today().hour) + ":" + str(datetime.today().minute))

#Setando o laço oara identificar o microfone
with sr.Microphone() as source:
#Abrindo o audio do microfone dentro do laço
    while not parar:
        audio = recon.listen(source, timeout=None)
        res = recon.recognize_google(audio, language='pt-BR')
        resposta = res.lower() #Setando todas as respostas para minusculo
        print("Texto reconhecido: ", resposta.lower())

        if resposta == "ok sexta-feira": #condição para que inicie a voz do robo
            robo = pyttsx3.init()
            robo.say("Olá mestre seja bem vindo, o que deseja?")
            print("Olá mestre seja bem vindo, o que deseja?")
            robo.setProperty("voice", b'brasil')
            robo.setProperty('rate', 140)
            robo.setProperty('volume', 1)
            robo.runAndWait()

            while True:

                audio = recon.listen(source, timeout=None) #abertura do microfone para o comando de voz com timeout = None para que ele nao de erro por execer o tempo
                res = recon.recognize_google(audio, language='pt-BR')
                resposta = res.lower()
                print("Texto reconhecido: ", resposta)

                if "youtube" in resposta: #condições para que entre no laço será: source(audio do microfone) = "youtube"
                    robo.say("Abrindo youtube")
                    robo.runAndWait() #executa os comando derivados ao nosso robo.
                    webbrowser.open('https://www.youtube.com/', autoraise=True)
                    break

                if "notícias" in resposta:
                    robo.say("Abrindo Cnn")
                    robo.runAndWait()
                    webbrowser.open('https://www.cnnbrasil.com.br/', autoraise=True)
                    break

                if "que horas são" in resposta:
                    robo.say(hora)
                    print(hora)
                    robo.runAndWait()
                    break

                if "criar evento" in resposta:
                    fala = "Ok, qual evento devo cadastrar?"
                    robo.say(fala)
                    print(fala)
                    robo.runAndWait()

                    audio = recon.listen(source, timeout=None) #abrindo o mic para cadastrar o evento
                    resAgenda = recon.recognize_google(audio, language='pt-BR')

                    file_exists = os.path.exists('agenda.txt')

                    if not file_exists: #se o arquivo txt nao existir, ele vai criar um arquivo
                        text_file = open("agenda.txt", "w")
                        text_file.write(resAgenda)
                        text_file.close()
                        robo.say("Evento cadastrado")
                        robo.runAndWait()
                        print("Evento cadastrado")
                        break

                    else:
                        text_file = open("agenda.txt", "a") #caso exista, ele irá escrever em uma outra linha
                        text_file.write("\n" + resAgenda)
                        text_file.close()

                        robo.say("Evento cadastrado")
                        print("Evento cadastrado")
                        break

                if "ler agenda" in resposta:
                    with open("agenda.txt") as file: #irá ler tudo que estiver no arquivo .txt
                        for line in file:
                            line = line.strip()
                            robo.say(line)
                            robo.runAndWait()
                        break

                if "assuntos do momento" in resposta:
                    robo.say("Mostrando as trendings")
                    robo.runAndWait()
                    webbrowser.open('https://twitter.com/explore/tabs/trending', autoraise=True)
                    break

                if "ativar protocolo 06" in resposta:
                    robo.say("Ativando protocolo")
                    robo.runAndWait()
                    os.startfile('C:\Riot Games\Riot Client/RiotClientServices.exe') #inicia algum .exe no seu computador
                    webbrowser.open('https://music.youtube.com/watch?v=n2qTCfDOysM&list=RDAMVMPwnHHAIi0XQ',
                                    autoraise=True)
                    break

                if "calculadora" in resposta:
                    robo.say("abrindo calculadora")
                    robo.runAndWait()
                    print("Quais valores deseja multiplicar? ")
                    audio = recon.listen(source, timeout=None)
                    contatxt = recon.recognize_google(audio, language='pt-BR')
                    if contatxt == "fechar":
                        break
                    conta = contatxt.split()
                    if conta[1] == "+":
                        print("Resultado: ", contatxt, " = ", str(int(conta[0]) + int(conta[2])))
                        robo.say(str(int(conta[0]) + int(conta[2])))
                        robo.runAndWait()
                        break


                    elif conta[1] == "-":
                        print("Resultado: ", contatxt, " = ", str(int(conta[0]) - int(conta[2])))
                        robo.say(str(int(conta[0]) - int(conta[2])))
                        robo.runAndWait()
                        break

                    elif conta[1] == "x":
                        print("Resultado: ", contatxt, " = ", str(int(conta[0]) * int(conta[2])))
                        robo.say(str(int(conta[0]) * int(conta[2])))
                        robo.runAndWait()
                        break

                    elif conta[1] == "/":
                        print("Resultado: ", contatxt, " = ", str(int(conta[0]) / int(conta[2])))
                        robo.say(str(int(conta[0]) / int(conta[2])))
                        robo.runAndWait()
                        break

                if "cuida da casa" in resposta:
                    robo.say("OK! Até mais tarde senhor!")
                    robo.runAndWait()
                    parar = True
                    break
