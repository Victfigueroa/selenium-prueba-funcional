# Edición realizada por Víctor Figueroa
# Objetivo: Integrar en Jenkins sin errores de codificación por caracteres Unicode

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")

buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Bogotá")
buscador.send_keys(Keys.RETURN)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='result-title-a']"))
    )
    print("OK - Prueba funcional: resultados encontrados")

    time.sleep(3)

    primer_resultado = driver.find_element(By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    assert primer_resultado.is_displayed(), "El primer resultado no está visible"
    print(f"OK - Primer resultado visible: {primer_resultado.text}")

    driver.save_screenshot("antes_clic.png")

    url_antes = driver.current_url
    print(f"URL antes de clic: {url_antes}")

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='result-title-a']")))
        primer_resultado.click()
    except (TimeoutException, ElementClickInterceptedException) as e:
        print(f"ERROR - Al hacer clic: {e}")
        driver.quit()
        exit(1)

    WebDriverWait(driver, 10).until(lambda d: d.current_url != url_antes)
    print(f"OK - Navegación exitosa a: {driver.current_url}")

    time.sleep(3)
    driver.save_screenshot("despues_clic.png")
    time.sleep(7)

except Exception as e:
    print(f"ERROR - Durante la prueba funcional: {e}")

driver.quit()

