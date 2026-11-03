# 🧪 Casos de Prueba Documentados — PrivaCheck CO
**Hito M2 · Pontificia Universidad Javeriana · Asignatura: Derecho e Inteligencia Artificial**  
*Estudiante: Gabriela Amor*

Este documento registra los 5 casos de prueba obligatorios (más caso de control anti-alucinaciones) diseñados para validar la precisión jurídica, la capacidad de detección de cláusulas abusivas y el control de falsos positivos de **PrivaCheck CO**, contrastados contra la **Ley Estatutaria 1581 de 2012** y el **Decreto 1377 de 2013**.

---

## 📌 Tabla Resumen de Pruebas

| Caso | Tipo de Cláusula / Permiso | Nivel de Riesgo Esperado | Diagnóstico Obtenido | Norma Aplicable Identificada | Estado |
| :---: | :--- | :---: | :---: | :--- | :---: |
| **1** | Permisos desproporcionados (Linterna solicita contactos y GPS) | 🔴 Alto | 🔴 Alto | Ley 1581/2012: Art. 4 lit. b y lit. f | ✅ Pasó |
| **2** | Cesión masiva y comercialización a terceros sin autorización específica | 🔴 Alto | 🔴 Alto | Ley 1581/2012: Art. 9 y Art. 12; Dec. 1377/2013: Art. 10 | ✅ Pasó |
| **3** | Condicionamiento de servicio a entrega de datos sensibles (salud y biometría) | 🔴 Alto | 🔴 Alto | Ley 1581/2012: Art. 5 y Art. 6 (Parágrafo); Dec. 1377: Art. 6 | ✅ Pasó |
| **4** | Retención perpetua e irrevocabilidad de la autorización | 🔴 Alto | 🔴 Alto | Ley 1581/2012: Art. 8 lit. e; Dec. 1377/2013: Art. 8 y 9 | ✅ Pasó |
| **5** | Cláusula legítima y proporcionada de comercio electrónico | 🟢 Bajo | 🟢 Bajo | Ley 1581/2012: Art. 4 lit. b y Art. 8 | ✅ Pasó |
| **6** | Prueba anti-alucinaciones / Entrada irrelevante o vacía | Neutral | Rechazo / Advertencia | Marco general y advertencia legal | ✅ Pasó |

---

## 🔎 Detalle de los Casos de Prueba

### Caso 1: Permisos Desproporcionados frente a la Finalidad Técnica
- **Texto de prueba:**  
  > *"La aplicación de linterna solicita acceso continuo en segundo plano a la lista de contactos del dispositivo, micrófono y ubicación GPS precisa con fines de 'mejora del servicio y análisis publicitario con terceros no especificados'."*
- **Problema jurídico:** Vulneración flagrante del principio de necesidad y finalidad. Una herramienta de iluminación no tiene causal técnica ni jurídica que justifique recolectar libretas de direcciones ni geolocalización.
- **Resultado en PrivaCheck CO:**
  - **Semáforo:** 🔴 **Nivel de Riesgo: ALTO / CRÍTICO**.
  - **Hallazgo:** Vulneración grave del Principio de Finalidad y Necesidad.
  - **Fundamento normativo citado:**
    - `Art. 4, Lit. b (Ley 1581/2012) — Principio de Finalidad`: El tratamiento debe obedecer a una finalidad legítima y proporcional informada al titular.
    - `Art. 4, Lit. f (Ley 1581/2012) — Principio de Circulación Restringida`.
- **Dictamen:** **Éxito**. Detecta la asimetría entre la función del software y el permiso sensible.

---

### Caso 2: Cesión y Comercialización Indiscriminada a Terceros
- **Texto de prueba:**  
  > *"Al crear su cuenta, el usuario acepta de manera irrevocable que sus datos personales, financieros y hábitos de consumo sean compartidos, comercializados y cedidos a socios comerciales nacionales e internacionales para campañas de marketing directo sin necesidad de notificación adicional."*
- **Problema jurídico:** El consentimiento debe ser específico, informado y previo. No se pueden transferir datos a categorías abiertas de terceros ni forzar autorizaciones en blanco o irrevocables.
- **Resultado en PrivaCheck CO:**
  - **Semáforo:** 🔴 **Nivel de Riesgo: ALTO**.
  - **Hallazgo:** Cesión abusiva de datos y vulneración del deber de información de receptores.
  - **Fundamento normativo citado:**
    - `Art. 9 (Ley 1581/2012) — Autorización previa, expresa e informada`.
    - `Art. 12 (Ley 1581/2012) — Deber de informar al Titular los receptores de la información`.
    - `Art. 10 (Decreto 1377/2013) — Deber de indicar finalidades específicas`.
- **Dictamen:** **Éxito**. Cita adecuadamente los deberes de especificación de terceros receptores.

---

### Caso 3: Tratamiento Forzado de Datos Sensibles (Salud y Biometría)
- **Texto de prueba:**  
  > *"La plataforma recopila la huella dactilar, reconocimiento facial, historial de consultas médicas y diagnósticos del usuario para personalizar recomendaciones, siendo obligatorio su suministro para poder crear la cuenta."*
- **Problema jurídico:** El parágrafo del artículo 6 de la Ley 1581 y el Decreto 1377 prohíben taxativamente condicionar cualquier actividad al otorgamiento de datos sensibles. El usuario siempre tiene carácter facultativo.
- **Resultado en PrivaCheck CO:**
  - **Semáforo:** 🔴 **Nivel de Riesgo: ALTO / CRÍTICO**.
  - **Hallazgo:** Tratamiento forzado de datos especialmente protegidos (biometría y salud).
  - **Fundamento normativo citado:**
    - `Art. 6 (Ley 1581/2012) — Tratamiento de Datos Sensibles y Parágrafo (Prohibición de condicionamiento)`.
    - `Art. 6 (Decreto 1377/2013) — Carácter facultativo de la autorización`.
- **Dictamen:** **Éxito**. Identifica la gravedad constitucional de los datos sensibles en Colombia.

---

### Caso 4: Retención Indefinida e Intento de Prohibir la Revocatoria
- **Texto de prueba:**  
  > *"Los datos recopilados serán conservados por la empresa por tiempo indefinido e irrevocable, renunciando el usuario a cualquier solicitud posterior de eliminación o revocatoria de consentimiento."*
- **Problema jurídico:** Violación directa del derecho fundamental de hábeas data en su dimensión de autodeterminación informativa y supresión temporal (temporalidad del dato).
- **Resultado en PrivaCheck CO:**
  - **Semáforo:** 🔴 **Nivel de Riesgo: ALTO**.
  - **Hallazgo:** Retención perpetua indebida e intento ilícito de suprimir el derecho de cancelación.
  - **Fundamento normativo citado:**
    - `Art. 8, Lit. e (Ley 1581/2012) — Derecho a la supresión y revocatoria de autorización`.
    - `Art. 8 y 9 (Decreto 1377/2013) — Límites temporales de necesidad y deber de trámite de reclamos`.
- **Dictamen:** **Éxito**. Alerta que la renuncia a derechos de hábeas data se tiene por no escrita ante la SIC.

---

### Caso 5: Cláusula Garantista y Conforme al Ordenamiento (Control de Falsos Positivos)
- **Texto de prueba:**  
  > *"La tienda virtual solicita nombre, dirección de entrega y correo electrónico exclusivamente para procesar las compras realizadas, facturar y coordinar el envío de los productos adquiridos. El usuario puede revocar la autorización o solicitar la supresión de sus datos en cualquier momento a través de privacidad@tienda.com."*
- **Problema jurídico:** Cláusula estándar de comercio electrónico que respeta la finalidad directa y provee canal expedito para ejercicio de derechos ARCO/Hábeas Data.
- **Resultado en PrivaCheck CO:**
  - **Semáforo:** 🟢 **Nivel de Riesgo: BAJO**.
  - **Hallazgo:** Cláusula garantista identificada. No se detectan excesos de tratamiento.
  - **Fundamento normativo citado:**
    - `Art. 4, Lit. b y Art. 8 (Ley 1581/2012) — Tratamiento legítimo proporcional y respeto a los derechos del titular`.
- **Dictamen:** **Éxito**. La herramienta no emite falsas alarmas ante contratos redactados con apego a la ley.

---

### Caso 6: Prueba Anti-Alucinaciones y Límites de Alcance
- **Texto de prueba:**  
  > *"¿Cuánto cuesta el canon de arrendamiento comercial en Chapinero según el código civil?"* (o texto vacío / no relacionado con datos personales).
- **Comportamiento verificado:**
  - Si el usuario no ingresa cláusulas sobre datos personales, el sistema no inventa leyes de protección de datos ni alucina infracciones inexistentes.
  - Mantiene de forma inalterable la advertencia legal de la Parte 6: *"Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado."*
- **Dictamen:** **Éxito**. Cero alucinaciones normativas detectadas.
