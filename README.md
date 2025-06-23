# Prueba Funcional Automatizada con Selenium

**GRUPO 5:**  
- Juan Villaman  
- Cristóbal de Jesus  
- Víctor Figueroa

---

## Introducción

Este proyecto forma parte del módulo 4 del curso DevOps, enfocado en la automatización de pruebas funcionales con Selenium y Python. El objetivo es validar que una búsqueda en el sitio web DuckDuckGo funcione correctamente, asegurando que los resultados se muestren y que la navegación al primer resultado sea exitosa.

La automatización mejora la eficiencia en la detección temprana de fallos y permite integrar las pruebas en pipelines de CI/CD, en este caso mediante Jenkins. Esto asegura que la funcionalidad clave se mantenga estable en futuras versiones.

---

## Preguntas finales

### ¿Qué tipo de errores podrías detectar con esta prueba funcional?  
Esta prueba detecta errores como campos de búsqueda mal identificados, ausencia de resultados o enlaces rotos. Por ejemplo, validamos que DuckDuckGo muestra resultados y que el primer enlace redirige correctamente, evitando regresiones críticas.

### ¿Por qué es importante automatizar pruebas desde la perspectiva del usuario?  
Automatizar pruebas garantiza que las funciones esenciales, como buscar inmuebles, siempre funcionen para el usuario final. Así evitamos experiencias frustrantes, asegurando rapidez y precisión sin depender de pruebas manuales lentas o inconsistentes.

### ¿Qué limitaciones tiene Selenium y cómo las superarías?  
Selenium no maneja bien pruebas en entornos no web o interacciones complejas fuera del navegador. Superamos esto integrando esperas explícitas con `WebDriverWait` y manejando excepciones, además de combinar con otras herramientas para pruebas no web.
