# Documento Final: Prueba Funcional Automatizada con Selenium

**Autor:** Víctor Figueroa, Juan Villaman, Cristóbal de Jesus  
**Proyecto:** Pruebas funcionales con Selenium – Módulo 4, Clase “Pruebas Funcionales”  
**Repositorio:** [https://github.com/Victfigueroa/selenium-prueba-funcional]
**Fecha:** Junio 2025

---

## 1. ¿Qué validamos?

Se automatizó una prueba funcional sobre el sitio web **DuckDuckGo**, con los siguientes objetivos:

- Acceder al sitio web desde Selenium.
- Simular una búsqueda de la frase **"inmuebles en Bogotá"**.
- Validar la aparición de resultados.
- Hacer clic en el primer resultado visible.
- Confirmar que el navegador redirige exitosamente a un nuevo sitio (por ejemplo, **Fincaraíz**).
- Tomar capturas de pantalla antes y después del clic.

Además, se integró esta prueba en **Jenkins** como parte de un pipeline simple de CI.

---

## 2. ¿Qué podría fallar si esta prueba no existiera?

- **Cambios invisibles en el buscador**: si el campo de búsqueda cambiara de nombre (`name="q"`), la prueba detectaría la falla, evitando errores silenciosos.
- **Resultados vacíos**: sin esta validación, una regresión que afecte el motor de búsqueda pasaría desapercibida.
- **Navegación rota**: si los enlaces no redirigen correctamente, podría afectar la experiencia del usuario final sin ser detectado.
- **Integraciones CI rotas**: sin la prueba automatizada en Jenkins, estas fallas podrían llegar a producción sin ser detectadas.

---

## 3. Sugerencias para nuevos casos funcionales

- Validar búsquedas con resultados distintos: por ejemplo, `"departamentos en Valparaíso"`.
- Verificar que los títulos de los resultados contengan palabras clave relevantes.
- Probar qué ocurre si el campo de búsqueda queda vacío.
- Simular búsquedas con caracteres especiales o errores ortográficos.
- Integrar pruebas funcionales con herramientas de espera inteligente como `WebDriverWait` y validar cambios de elementos dinámicos.
- Generar reportes automáticos de pruebas usando `pytest` + `allure` o `pytest-html`.

---

## 4. Aportes y dificultades durante el desarrollo

- Ajuste del script para incluir `time.sleep()` y capturas automáticas.
- Manejo de errores usando `try-except` y `WebDriverWait`.
- Corrección del error `UnicodeEncodeError` en Jenkins eliminando caracteres Unicode (`✅ ❌`) y reemplazándolos por texto plano.
- Configuración del job en Jenkins (freestyle), activación del entorno virtual con `call venv\Scripts\activate` y ejecución controlada del script.

**Dificultades enfrentadas:**
- Descarga e instalación del `ChromeDriver` compatible con la versión 137.
- Error por incompatibilidad de consola Jenkins con caracteres Unicode.
- Necesidad de guardar la URL antes del clic para validar correctamente el cambio de página (`WebDriverWait(driver, 10).until(lambda d: d.current_url != url_antes)`).

---

## 5. Evidencias entregadas

- Archivo `test_busqueda.py` con pruebas funcionales completas y anotaciones de edición.
- Capturas de pantalla:
  - `antes_clic.png`: muestra la búsqueda en DuckDuckGo.
  - `despues_clic.png`: muestra la página del primer resultado.
  - Consola de Jenkins: evidencia de ejecución exitosa.
  - Historial de builds en Jenkins: éxito del job.
