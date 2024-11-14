from tiny_web import start_tiny, integrar_intelipost
from bot_web import open_page

def main():
    contas_tiny = ['miligrama_nordeste', 'miligrama']
    transportadoras_miligrama = [
        '6', #Total Express
        '7', #Correios
        '8', #Envie Agora
        '25', #Jadlog
        '35', #Quality
        '36', #Entrega Full - Norte e Nordeste
        '37', #Total Express - Norte e Nordeste
    ]

    transportadoras_mili_nordeste = [
        '5', #Total Express
        '6', #Correios
    ]

    for conta in contas_tiny:
        print(conta)
        if conta == 'miligrama':
            user = 'bot_auto@miligrama'
            transportadoras = transportadoras_miligrama
        elif conta == 'miligrama_nordeste':
            user = 'bot_auto@mili_nordeste'
            transportadoras = transportadoras_mili_nordeste
        password = 'Acesso@Star123'

        driver = start_tiny(user, password)

        for transportadora in transportadoras:
            try:
                # Ir para Expedição
                url = 'https://erp.tiny.com.br/expedicao'
                open_page(driver, url)
                integrar_intelipost(driver, transportadora)
            except:
                driver = start_tiny(user, password)
                continue









    

main()