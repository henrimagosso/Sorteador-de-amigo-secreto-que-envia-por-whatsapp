import pywhatkit
import random
import time


def coletar_dados():
    participantes = {}
    while True:
        nome = input("Digite o nome do participante (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        numero = input(
            "Digite o número de telefone do participante (com código do país e DDD): ")  # O numero deve ser inserido como +55ddd9xxxx-xxxx
        participantes[nome] = numero
    return participantes


def sortear_pares(participantes):
    nomes = list(participantes.keys())
    random.shuffle(nomes)
    pares = []

    for i in range(len(nomes)):
        remetente = nomes[i]
        destinatario = nomes[(i + 1) % len(nomes)]

        while remetente == destinatario:  # Possível causa do problema
            random.shuffle(nomes)
            destinatario = nomes[(i + 1) % len(nomes)]

        pares.append((remetente, destinatario))

    return pares


def enviar_mensagens(pares, participantes):
    for par in pares:
        remetente = par[0]
        destinatario_nome = par[1]
        destinatario_numero = participantes[destinatario_nome]
        mensagem = f"Olá {remetente}, você tirou o(a) {destinatario_nome} no Amigo Secreto!"

        # Enviar mensagem usando pywhatkit (incluir código do país)
        try:
            pywhatkit.sendwhatmsg(destinatario_numero, mensagem, time.localtime().tm_hour, time.localtime().tm_min + 1)
            print(f"Mensagem enviada para {remetente} com sucesso!")
            time.sleep(10)  # Aguardar 10 segundos para evitar bloqueio do WhatsApp
        except Exception as e:
            print(f"Erro ao enviar mensagem para {remetente}: {e}")


def main():
    participantes = coletar_dados()
    pares = sortear_pares(participantes)
    enviar_mensagens(pares, participantes)


if __name__ == "__main__":
    main()