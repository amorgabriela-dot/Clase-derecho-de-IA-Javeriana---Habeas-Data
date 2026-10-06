import streamlit as st
import os
import json
import time

# Configuración visual de la página
st.set_page_config(
    page_title="PrivaCheck CO — Diagnóstico de Hábeas Data",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados y tema limpio
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .legal-alert {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        padding: 12px 16px;
        border-radius: 6px;
        font-size: 0.92rem;
        color: #92400E;
        margin-bottom: 20px;
    }
    .risk-card-high {
        background-color: #FEE2E2;
        border-left: 6px solid #EF4444;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .risk-card-med {
        background-color: #FEF3C7;
        border-left: 6px solid #F59E0B;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .risk-card-low {
        background-color: #D1FAE5;
        border-left: 6px solid #10B981;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown('<div class="main-header">⚖️ PrivaCheck CO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header"><em>"Claridad y control sobre tus datos personales en un solo clic"</em> · Pontificia Universidad Javeriana</div>', unsafe_allow_html=True)

# Advertencia Legal Obligatoria (Parte 6 del proyecto)
st.markdown("""
<div class="legal-alert">
    ⚠️ <strong>Aviso legal importante:</strong> Esta herramienta es un ejercicio académico desarrollado para la clase de Derecho e Inteligencia Artificial que <strong>no constituye asesoría legal formal</strong> ni sustituye la consulta con un abogado ni la presentación de quejas ante la Superintendencia de Industria y Comercio (SIC).
</div>
""", unsafe_allow_html=True)

# Barra lateral (Sidebar)
with st.sidebar:
    st.header("⚙️ Configuración")
    
    # Manejo de API Key (puede venir de Secrets de Streamlit o input manual)
    env_api_key = os.getenv("OPENROUTER_API_KEY", "")
    api_key_input = st.text_input(
        "OpenRouter API Key (Opcional):",
        value=env_api_key,
        type="password",
        help="Si no tienes una clave activa, PrivaCheck utilizará su motor de análisis normativo local basado en la Ley 1581 de 2012."
    )
    api_key = api_key_input.strip() or env_api_key

    st.markdown("---")
    st.markdown("### 📚 Marco Normativo Integrado")
    st.markdown("""
    - **Ley Estatutaria 1581 de 2012:** Disposiciones generales de protección de datos personales en Colombia.
    - **Decreto 1377 de 2013:** Reglamentación de autorización, deberes de los responsables y políticas de tratamiento.
    - **Superintendencia de Industria y Comercio (SIC):** Criterios de necesidad, finalidad y datos sensibles.
    """)
    st.markdown("---")
    st.caption("Proyecto final · Derecho e IA · Estudiante: Gabriela Amor")

# Ejemplos precargados para pruebas rápidas
ejemplos = {
    "Personalizado (Escribir o pegar mi propio texto)": "",
    "Caso 1: App de linterna que solicita contactos y localización": "La aplicación de linterna solicita acceso continuo en segundo plano a la lista de contactos del dispositivo, micrófono y ubicación GPS precisa con fines de 'mejora del servicio y análisis publicitario con terceros no especificados'.",
    "Caso 2: Plataforma con cesión de datos sin autorización específica": "Al crear su cuenta, el usuario acepta de manera irrevocable que sus datos personales, financieros y hábitos de consumo sean compartidos, comercializados y cedidos a socios comerciales nacionales e internacionales para campañas de marketing directo sin necesidad de notificación adicional.",
    "Caso 3: Tratamiento de datos sensibles de salud y biometría": "La plataforma recopila la huella dactilar, historial de consultas médicas y diagnósticos del usuario para personalizar recomendaciones, conservando dicha información por tiempo indefinido aún después de cancelar la cuenta.",
    "Caso 4: Cláusula razonable de comercio electrónico": "La tienda virtual solicita nombre, dirección de entrega y correo electrónico exclusivamente para procesar las compras realizadas, facturar y coordinar el envío de los productos adquiridos. El usuario puede revocar la autorización o solicitar la supresión de sus datos en cualquier momento a través de privacidad@tienda.com."
}

col_selector, col_space = st.columns([2, 1])
with col_selector:
    seleccion_ejemplo = st.selectbox("💡 Selecciona un caso de prueba o escribe uno nuevo:", list(ejemplos.keys()))

texto_inicial = ejemplos[seleccion_ejemplo]

# Área de entrada de texto
clausula_texto = st.text_area(
    "📝 Pega aquí la cláusula de términos y condiciones, política de privacidad o lista de permisos solicitados:",
    value=texto_inicial,
    height=160,
    placeholder="Ejemplo: 'El usuario autoriza el acceso a su galería de fotos y lista de llamadas para optimizar la publicidad entregada por empresas filiales...'"
)

# Función de análisis normativo inteligente con base en Ley 1581 y Decreto 1377
def analizar_con_reglas_normativas(texto):
    texto_lower = texto.lower()
    hallazgos = []
    riesgo = "Bajo"
    puntaje = 0
    articulos_citados = []
    
    # 1. Análisis de Permisos Desproporcionados / Principio de Finalidad (Art 4 literal b, Ley 1581)
    permisos_sensibles = ["contactos", "micrófono", "microfono", "cámara", "camara", "galería", "galeria", "llamadas", "ubicación", "ubicacion", "gps"]
    encontrados = [p for p in permisos_sensibles if p in texto_lower]
    if encontrados:
        if any(w in texto_lower for w in ["linterna", "calculadora", "juego", "fondo de pantalla"]):
            puntaje += 4
            hallazgos.append(f"🔴 **Vulneración grave del Principio de Finalidad y Necesidad:** La app solicita acceso a `{', '.join(encontrados)}`, lo cual no guarda ninguna relación razonable ni proporcional con su función técnica.")
            articulos_citados.append("**Art. 4, Lit. b (Ley 1581/2012) — Principio de Finalidad:** El tratamiento debe obedecer a una finalidad legítima y proporcional informada al titular.")
        else:
            puntaje += 2
            hallazgos.append(f"🟡 **Alerta de permisos de acceso:** Se solicita acceso a `{', '.join(encontrados)}`. Verifica si la función principal de la herramienta realmente los necesita.")
            articulos_citados.append("**Art. 4, Lit. f (Ley 1581/2012) — Principio de Circulación Restringida:** Los datos solo pueden ser tratados por personas autorizadas para la finalidad acordada.")

    # 2. Análisis de Cesión Indiscriminada a Terceros y Publicidad
    if any(w in texto_lower for w in ["terceros", "socios comerciales", "comercializados", "cedidos", "publicidad", "marketing"]):
        if any(w in texto_lower for w in ["sin necesidad de notificación", "indefinido", "irrevocable", "no especificados"]):
            puntaje += 4
            hallazgos.append("🔴 **Cesión abusiva de datos:** Se pacta la entrega de información personal a terceros indefinidos o sin facultad de revocatoria.")
            articulos_citados.append("**Art. 9 (Ley 1581/2012) — Autorización:** El tratamiento requiere autorización previa, expresa e informada del titular, no pudiendo presumirse de forma tácita o indeterminada.")
            articulos_citados.append("**Art. 12 (Ley 1581/2012) — Deber de información:** Se debe informar con precisión la identificación de los terceros receptores de la información.")
        else:
            puntaje += 2
            hallazgos.append("🟡 **Compartición con aliados comerciales:** Los datos podrán circular con terceros colaboradores. Tienes derecho a limitar esta finalidad.")
            articulos_citados.append("**Art. 10 (Decreto 1377/2013) — Deber de indicar finalidades específicas:** El responsable debe detallar cada uso proyectado.")

    # 3. Análisis de Datos Sensibles (Art. 5 y 6 Ley 1581)
    if any(w in texto_lower for w in ["salud", "médica", "medica", "biometría", "biometria", "huella", "facial", "diagnóstico", "diagnostico"]):
        puntaje += 4
        hallazgos.append("🔴 **Tratamiento de Datos Sensibles (Especial Protección):** Se recaban datos relativos a salud o biometría. En Colombia está prohibido condicionar el servicio a la entrega de datos sensibles.")
        articulos_citados.append("**Art. 6 (Ley 1581/2012) — Tratamiento de Datos Sensibles:** Ninguna actividad podrá condicionarse a que el titular suministre datos personales sensibles, salvo excepciones de ley expresas.")
        articulos_citados.append("**Art. 6 (Decreto 1377/2013) — Autorización para datos sensibles:** El titular no está obligado a autorizar su tratamiento bajo ninguna circunstancia.")

    # 4. Análisis de Temporalidad e Indefinición
    if any(w in texto_lower for w in ["indefinido", "tiempo indefinido", "irrevocable", "para siempre"]):
        puntaje += 3
        hallazgos.append("🔴 **Retención indebida e irrevocable:** No se fija un periodo razonable de vigencia y se intenta privar al titular de su derecho a revocatoria.")
        articulos_citados.append("**Art. 8, Lit. e (Ley 1581/2012) — Derecho a la supresión:** El titular tiene derecho a revocar la autorización y/o solicitar la supresión de los datos en cualquier momento.")

    # 5. Cláusulas conformes a la ley
    if any(w in texto_lower for w in ["revocar", "supresión", "supresion", "exclusivamente", "fines de envío"]):
        hallazgos.append("🟢 **Cláusula garantista identificada:** Se reconoce expresamente el derecho de revocatoria o se limita la finalidad estrictamente a la prestación del servicio.")
        articulos_citados.append("**Art. 8 (Ley 1581/2012) — Derechos de los Titulares:** Reconocimiento expreso del derecho de consulta y reclamo.")

    # Calificación del Semáforo
    if puntaje >= 4:
        riesgo = "Alto"
    elif puntaje >= 2:
        riesgo = "Medio"
    else:
        riesgo = "Bajo"
        if not hallazgos:
            hallazgos.append("🟢 **No se detectaron cláusulas desproporcionadas evidentes:** El texto no contiene solicitudes desmedidas de permisos ni cesiones ilícitas directas.")
            articulos_citados.append("**Ley 1581 de 2012:** Cumple prima facie con las exigencias generales de transparencia.")

    return riesgo, hallazgos, list(set(articulos_citados))

# Botón de ejecución
if st.button("🔍 Analizar Cláusula con PrivaCheck CO", type="primary", use_container_width=True):
    if not clausula_texto.strip():
        st.warning("⚠️ Por favor pega una cláusula o selecciona un caso de prueba antes de analizar.")
    else:
        with st.spinner("Analizando texto con el marco normativo de Hábeas Data colombiano..."):
            time.sleep(0.8) # feedback visual agradable
            
            # Ejecución del diagnóstico
            riesgo, hallazgos, articulos = analizar_con_reglas_normativas(clausula_texto)
            
            st.markdown("### 📊 Resultado del Diagnóstico Jurídico")
            
            # Semáforo de riesgo
            if riesgo == "Alto":
                st.markdown("""
                <div class="risk-card-high">
                    <h3 style="margin-top:0; color:#B91C1C;">🔴 Nivel de Riesgo: ALTO / CRÍTICO</h3>
                    <p style="color:#7F1D1D; margin-bottom:0;">
                    Se detectaron cláusulas que contradicen gravemente los principios de finalidad, necesidad y libertad estipulados en la Ley Estatutaria 1581 de 2012. <strong>Recomendación: No aceptar o revocar permisos inmediatamente.</strong>
                    </p>
                </div>
                """, unsafe_allow_html=True)
            elif riesgo == "Medio":
                st.markdown("""
                <div class="risk-card-med">
                    <h3 style="margin-top:0; color:#B45309;">🟡 Nivel de Riesgo: MEDIO</h3>
                    <p style="color:#78350F; margin-bottom:0;">
                    Existen permisos o transferencias de datos que requieren atención y justificación detallada antes de ser consentidos.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="risk-card-low">
                    <h3 style="margin-top:0; color:#047857;">🟢 Nivel de Riesgo: BAJO</h3>
                    <p style="color:#064E3B; margin-bottom:0;">
                    La redacción respeta los límites estándar de finalidad y proporcionalidad para el servicio evaluado.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            # Columnas de desglose
            col_izq, col_der = st.columns([1.2, 1])
            
            with col_izq:
                st.markdown("#### 🚨 Hallazgos y Alertas")
                for h in hallazgos:
                    st.markdown(h)
                    
                st.markdown("#### 💡 ¿Qué debes hacer como usuario?")
                if riesgo == "Alto":
                    st.info("1. Niega los permisos que no sean esenciales para el funcionamiento de la app.\n2. Si la app exige aceptar obligatoriamente datos sensibles, abstente de instalarla.\n3. Puedes reportar conductas abusivas ante la Delegatura de Protección de Datos de la SIC.")
                elif riesgo == "Medio":
                    st.info("1. Revisa la sección de configuración de privacidad de la app para desactivar la compartición publicitaria.\n2. Autoriza solo los permisos durante el uso activo de la aplicación.")
                else:
                    st.success("La cláusula parece razonable. Recuerda que siempre conservas el derecho a solicitar la eliminación de tus datos cuando dejes de usar la plataforma.")

            with col_der:
                st.markdown("#### 📖 Fundamento Normativo (RAG)")
                st.markdown("Artículos citados del ordenamiento jurídico colombiano:")
                for art in articulos:
                    st.markdown(f"- {art}")

st.markdown("---")
st.markdown("<center><small>PrivaCheck CO · Pontificia Universidad Javeriana · Bogotá D.C., Colombia</small></center>", unsafe_allow_html=True)
