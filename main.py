
import streamlit as st

st.title("Test de Autoevaluación")

st.write("Por favor, responde honestamente cada una de las siguientes afirmaciones seleccionando la opción que mejor describa tu experiencia.")

opciones = ["Nunca", "Algunas veces", "Casi siempre", "Siempre"]

respuestas = {}

respuestas[" [El tener que asistir diariamente a clases me cansa."] = st.radio("1.  [El tener que asistir diariamente a clases me cansa.", opciones, key="pregunta_1")

respuestas[" [Mis problemas escolares me deprimen fácilmente"] = st.radio("2.  [Mis problemas escolares me deprimen fácilmente", opciones, key="pregunta_2")

respuestas[" [Durante las clases me siento somnoliento"] = st.radio("3.  [Durante las clases me siento somnoliento", opciones, key="pregunta_3")

respuestas[" [Creo que estudiar hace que me sienta agotado"] = st.radio("4.  [Creo que estudiar hace que me sienta agotado", opciones, key="pregunta_4")

respuestas[" [Cada vez me es mas difícil concentrarme en las clases"] = st.radio("5.  [Cada vez me es mas difícil concentrarme en las clases", opciones, key="pregunta_5")

respuestas[" [Me desilusionan mis estudios"] = st.radio("6.  [Me desilusionan mis estudios", opciones, key="pregunta_6")

respuestas[" [Antes de terminar mi horario de clases ya me siento cansado"] = st.radio("7.  [Antes de terminar mi horario de clases ya me siento cansado", opciones, key="pregunta_7")

respuestas[" [No me interesa asistir a clases"] = st.radio("8.  [No me interesa asistir a clases", opciones, key="pregunta_8")

respuestas[" [Cada vez me cuesta más trabajo ponerle atención al maestro"] = st.radio("9.  [Cada vez me cuesta más trabajo ponerle atención al maestro", opciones, key="pregunta_9")

respuestas[" [El asistir a clases se me hace aburrido"] = st.radio("10.  [El asistir a clases se me hace aburrido", opciones, key="pregunta_10")

respuestas[" [Siento que estudiar me está desgastando físicamente."] = st.radio("11.  [Siento que estudiar me está desgastando físicamente.", opciones, key="pregunta_11")

respuestas[" [Cada vez me siento más frustrado por ir a la escuela."] = st.radio("12.  [Cada vez me siento más frustrado por ir a la escuela.", opciones, key="pregunta_12")

respuestas[" [No creo terminar con éxito mis estudios."] = st.radio("13.  [No creo terminar con éxito mis estudios.", opciones, key="pregunta_13")

respuestas[" [Siento que tengo más problemas para recordar lo que estudio."] = st.radio("14.  [Siento que tengo más problemas para recordar lo que estudio.", opciones, key="pregunta_14")

respuestas[" [Creo que estudiar me está desgastando emocionalmente."] = st.radio("15.  [Creo que estudiar me está desgastando emocionalmente.", opciones, key="pregunta_15")

respuestas["Unnamed: 23"] = st.radio("16. Unnamed: 23", opciones, key="pregunta_16")

respuestas["Unnamed: 24"] = st.radio("17. Unnamed: 24", opciones, key="pregunta_17")

respuestas["Unnamed: 25"] = st.radio("18. Unnamed: 25", opciones, key="pregunta_18")

respuestas["Unnamed: 26"] = st.radio("19. Unnamed: 26", opciones, key="pregunta_19")

respuestas["Unnamed: 27"] = st.radio("20. Unnamed: 27", opciones, key="pregunta_20")

respuestas["Unnamed: 28"] = st.radio("21. Unnamed: 28", opciones, key="pregunta_21")

respuestas["Unnamed: 29"] = st.radio("22. Unnamed: 29", opciones, key="pregunta_22")

respuestas["Unnamed: 30"] = st.radio("23. Unnamed: 30", opciones, key="pregunta_23")

respuestas["Unnamed: 31"] = st.radio("24. Unnamed: 31", opciones, key="pregunta_24")

respuestas["Unnamed: 32"] = st.radio("25. Unnamed: 32", opciones, key="pregunta_25")

respuestas["Unnamed: 33"] = st.radio("26. Unnamed: 33", opciones, key="pregunta_26")

respuestas["Unnamed: 34"] = st.radio("27. Unnamed: 34", opciones, key="pregunta_27")

respuestas["Unnamed: 35"] = st.radio("28. Unnamed: 35", opciones, key="pregunta_28")

respuestas["Unnamed: 36"] = st.radio("29. Unnamed: 36", opciones, key="pregunta_29")

respuestas["Unnamed: 37"] = st.radio("30. Unnamed: 37", opciones, key="pregunta_30")

respuestas["Unnamed: 38"] = st.radio("31. Unnamed: 38", opciones, key="pregunta_31")

respuestas["Unnamed: 39"] = st.radio("32. Unnamed: 39", opciones, key="pregunta_32")

if st.button("Enviar respuestas"):
    st.success("¡Gracias por completar el test!")
    st.write("Tus respuestas:")
    for pregunta, respuesta in respuestas.items():
        st.write(f"**{pregunta}**: {respuesta}")
