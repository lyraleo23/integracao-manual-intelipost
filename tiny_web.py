import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def start_tiny(user, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)

    #site de acesso
    driver.get("https://erp.tiny.com.br/login")

    #tempo de espera
    driver.implicitly_wait(10)

    #login
    driver.find_element(By.NAME, "username").click()
    driver.find_element(By.NAME, "username").send_keys(user)
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys(password)

    #tempo de espera
    driver.implicitly_wait(10)

    #Clicar botão de login
    driver.find_element(
    By.XPATH,"//*[contains(text(),'entrar no Olist Tiny')]").click()

    #Confirma login
    try:
        driver.find_element(By.XPATH, '//*[@id="bs-modal-ui-popup"]/div/div/div/div[3]/button[1]').click()
    except:
        driver.implicitly_wait(5)
    time.sleep(5)

    return driver

def login_tiny(driver, user, password):
    #site de acesso
    driver.get("https://erp.tiny.com.br/login")

    #tempo de espera
    driver.implicitly_wait(10)

    #login
    driver.find_element(By.NAME, "username").click()
    driver.find_element(By.NAME, "username").send_keys(user)
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys(password)

    #tempo de espera
    driver.implicitly_wait(10)

    #Clicar botão de login
    driver.find_element(
    By.XPATH,"//*[contains(text(),'entrar no Olist Tiny')]").click()

    #Confirma login
    try:
        driver.find_element(By.XPATH, '//*[@id="bs-modal-ui-popup"]/div/div/div/div[3]/button[1]').click()
    except:
        driver.implicitly_wait(5)
    time.sleep(5)

    return driver

def remove_vendedor_contato(driver):
    # Editar
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="root-contatos"]/div/div/div[1]/div/div/div[1]/button[4]').click()
    time.sleep(5)

    # dados complementares
    driver.find_element(By.XPATH, '//*[@id="root-contatos"]/div/div/div[2]/div[2]/div[1]/ul/li[2]/a').click()
    driver.implicitly_wait(5)

    # Vendedor
    driver.find_element(By.XPATH, '//*[@id="root-contatos"]/div/div/div[2]/div[2]/div[2]/div[5]/div/input').click()
    driver.implicitly_wait(5)
    # driver.find_element(By.XPATH, '//*[@id="root-contatos"]/div/div/div[2]/div[2]/div[2]/div[5]/div/input').clear()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="root-contatos"]/div/div/div[2]/div[2]/div[2]/div[5]/div/input').send_keys('Qualquer vendedor')
    driver.find_element(By.XPATH, '//*[@id="root-contatos"]/div/div/div[2]/div[2]/div[1]/ul/li[2]/a').click()
    driver.implicitly_wait(5)
    time.sleep(5)

    # salvar
    driver.find_element(By.XPATH, '//*[@id="root-contatos"]/div/div/div[2]/div[3]/div/div/button[1]').click()
    driver.implicitly_wait(5)
    time.sleep(10)
    return

def remover_rps(driver):
    # Clica em editar
    driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[7]/div[1]/div/button').click()
    time.sleep(5)

    # Clica no campo RPS
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="numero"]').clear()
    driver.find_element(By.XPATH, '//*[@id="numero"]').send_keys('')
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="numeroNFSe"]').click()
    time.sleep(5)

    # Clica em salvar
    driver.find_element(By.XPATH, '//*[@id="botaoSalvar"]').click()
    driver.implicitly_wait(5)
    time.sleep(5)
    return

def integrar_intelipost(driver, option_number):
    # Clica na opção de Integrar com a Intelipost
    driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div[2]/div[1]/div[2]/div/div[1]/button[1]').click()
    time.sleep(7)

    # Clica na opção de filtros
    driver.find_element(By.XPATH, '//*[@id="formExpedicaoAgrupamento"]/div[1]/div[2]/div[2]/div[3]/div[1]/ul/li[3]/a').click()
    time.sleep(1)

    # Clica na opção de forma de envio
    driver.find_element(By.ID, 'idFormaEnvioAgrupamentoCotacao').click()
    time.sleep(1)

    # Seleciona todos os envios da transportadora
    driver.find_element(By.XPATH, f'//*[@id="idFormaEnvioAgrupamentoCotacao"]/option[{option_number}]').click()
    time.sleep(3)

    # Clica no botão de enviar
    driver.find_element(By.XPATH, '//*[@id="tabelaInclusaoAgrupamento"]/thead/tr/th[1]/span').click()

    # Confirma a seleção
    driver.find_element(By.XPATH, '//*[@id="formExpedicaoAgrupamento"]/div[2]/div/div[2]/div[2]/button[1]').click()
    time.sleep(2)

    # Clica no botão de confirmar
    driver.find_element(By.XPATH, '//*[@id="bs-modal-ui-popup"]/div/div/div/div[3]/button[1]').click()
    time.sleep(10)
    
    driver.find_element(By.XPATH, '//*[@id="bs-modal-ui-popup"]/div/div/div/div[3]/button').click()
