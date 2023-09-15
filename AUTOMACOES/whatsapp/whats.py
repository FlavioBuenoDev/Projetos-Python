"""

Python + Selenium

2 Requisitos
 * Instalar o Selenium (pip install selenium)
 * Baixar o webdriver (chromedriver(para chrome) ou geckodriver(para firefox))
    Precisa barixar o ChromeDriver https://chromedriver.chromium.org/
"""

import pandas as pd

contatos_df = pd.read_excel(
    "C:/Users/flavio.bueno/Projetos_Python/whatsapp/Enviar.xlsx")
display(contatos_df)
