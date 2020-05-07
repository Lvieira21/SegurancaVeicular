'''
Created on 16 de jun de 2018

@author: almer
Alterado por:Lucas Vieira
'''

import time
from playsound import playsound
from gtts import gTTS

class MensagemFalada(object):
    '''
    classdocs
    '''

    def scriptInicial(self):
        playsound("Mensagens Faladas\\boas-vindas.mp3")
        time.sleep(16)
        playsound("Mensagens Faladas\\auxilio-calibracao.mp3")
        time.sleep(4)
        playsound("Mensagens Faladas\\auxilio-calibracao-olhos-fechados.mp3")
        time.sleep(8)
    
    def scriptContagem(self):
        playsound("Mensagens Faladas\\contar-um.mp3")
        time.sleep(1)
        playsound("Mensagens Faladas\\contar-dois.mp3")
        time.sleep(1)
        playsound("Mensagens Faladas\\contar-tres.mp3")
        time.sleep(1)
        
    def scriptRegulagemOlhosAbertos(self):
        playsound("Mensagens Faladas\\ok-auxilio-calibracao-olhos-abertos.mp3")
        time.sleep(10)
    
    def scriptFimCalibragem(self):
        tts = gTTS(text='Pronto, calibração finalizada.', lang='pt')
        tts.save("Mensagens Faladas\\ok.mp3")
        playsound("Mensagens Faladas\\ok.mp3")
        
    def scriptIniciarExecucao(self, nome=""):
        tts = gTTS(text='Olá, ' + nome + '. Vamos iniciar a nossa viagem? Qualquer alerta eu irei te falar.', lang='pt')
        tts.save("Mensagens Faladas\\iniciar viagem.mp3")
        playsound("Mensagens Faladas\\iniciar viagem.mp3")
        tts = gTTS(text='' + nome + '. Acho melhor realizarmos uma pausa para descanço.', lang='pt')
        tts.save("Mensagens Faladas\\alerta.mp3")
    
    def scriptAlerta(self):
        playsound("Mensagens Faladas\\alerta.mp3")
        time.sleep(6)
