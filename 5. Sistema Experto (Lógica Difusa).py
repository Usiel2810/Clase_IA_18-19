# Sistema Experto de Diagnóstico Asistido
# Desarrollado por: Asistente de Soporte Técnico
# Función: Detección básica para identificar fallos en hardware y software

class DiagnosticoAsistido:
    def __init__(self):
        self.respuestas = {}
        self.informe = ""
        self.precision = 0

    def definir_base_conocimiento(self):
        """Configura El Conjunto De Reglas De Diagnóstico"""
        self.reglas = [
            {
                'condiciones': ['no_inicia', 'sin_indicadores'],
                'conclusion': 'Falla en alimentación eléctrica',
                'sugerencia': 'Revise el cable de corriente y fuente de poder',
                'confianza': 90
            },
            {
                'condiciones': ['enciende', 'sin_imagen', 'ventiladores_operando'],
                'conclusion': 'Fallo en pantalla o tarjeta gráfica',
                'sugerencia': 'Verificar cableado de video y tarjeta de gráficos',
                'confianza': 85
            },
            {
                'condiciones': ['enciende', 'pitidos_repetidos'],
                'conclusion': 'Problema con la memoria RAM',
                'sugerencia': 'Retirar y reinstalar los módulos de RAM',
                'confianza': 88
            },
            {
                'condiciones': ['desempeño_bajo', 'ruido_ventiladores'],
                'conclusion': 'Sobrecalentamiento del procesador',
                'sugerencia': 'Limpiar sistema térmico y cambiar pasta disipadora',
                'confianza': 75
            },
            {
                'condiciones': ['error_pantalla', 'reinicios_aleatorios'],
                'conclusion': 'Error de software o drivers',
                'sugerencia': 'Actualizar drivers y ejecutar diagnóstico en modo seguro',
                'confianza': 70
            },
            {
                'condiciones': ['sin_internet', 'otros_conectados'],
                'conclusion': 'Fallo de configuración de red',
                'sugerencia': 'Reiniciar adaptador de red y revisar parámetros',
                'confianza': 80
            }
        ]

    def obtener_datos_usuario(self):
        """Solicita entradas al usuario final"""
        print("=== SISTEMA DE ANÁLISIS - IDENTIFICACIÓN DE FALLAS ===")
        print("Conteste 'si' o 'no' a las siguientes preguntas = \n")

        preguntas = {
            'no_inicia': '¿El equipo no enciende en absoluto?',
            'sin_indicadores': '¿No se muestran luces ni señales visibles?',
            'enciende': '¿El equipo arranca pero no funciona correctamente?',
            'sin_imagen': '¿La pantalla permanece en negro?',
            'ventiladores_operando': '¿Se escuchan los ventiladores funcionando?',
            'pitidos_repetidos': '¿Se oyen sonidos repetitivos al encender?',
            'desempeño_bajo': '¿El sistema responde lentamente?',
            'ruido_ventiladores': '¿Los ventiladores hacen ruido fuerte?',
            'error_pantalla': '¿Ha aparecido una pantalla azul con errores?',
            'reinicios_aleatorios': '¿El equipo se reinicia inesperadamente?',
            'sin_internet': '¿No tiene acceso a internet?',
            'otros_conectados': '¿Otros dispositivos se conectan sin problema?'
        }

        for clave, pregunta in preguntas.items():
            while True:
                entrada = input(f"{pregunta} ").lower().strip()
                if entrada in ['si', 'sí', 's', 'yes', 'y']:
                    self.respuestas[clave] = True
                    break
                elif entrada in ['no', 'n']:
                    self.respuestas[clave] = False
                    break
                else:
                    print("Respuesta inválida. Use 'si' o 'no'.")

    def evaluar_diagnostico(self):
        """Evalúa reglas con base en las respuestas dadas"""
        mejor_coincidencia = None
        mejor_confianza = 0

        for regla in self.reglas:
            coincidencias = sum([1 for c in regla['condiciones'] if self.respuestas.get(c, False)])
            total = len(regla['condiciones'])
            porcentaje = (coincidencias / total) * 100

            if coincidencias == total and regla['confianza'] > mejor_confianza:
                mejor_coincidencia = regla
                mejor_confianza = regla['confianza']

        return mejor_coincidencia, mejor_confianza

    def presentar_diagnostico(self, resultado, confianza):
        """Muestra el diagnóstico final al usuario"""
        print("\n" + "="*50)
        print("RESULTADO DEL DIAGNÓSTICO")
        print("="*50)

        if resultado:
            print(f"Diagnóstico identificado = {resultado['conclusion']}")
            print(f"Grado de certeza = {confianza}%")
            print(f"Recomendación = {resultado['sugerencia']}")

            if confianza >= 80:
                print("✅ Diagnóstico con alta certeza")
            elif confianza >= 60:
                print("⚠️ Diagnóstico con certeza moderada")
            else:
                print("❓ Diagnóstico poco confiable")
        else:
            print("❌ No se pudo determinar el problema con la información dada.")
            print("Sugerencia = Consulte a un técnico especializado.")

    def ejecutar(self):
        """Proceso principal del sistema"""
        self.definir_base_conocimiento()
        self.obtener_datos_usuario()
        resultado, confianza = self.evaluar_diagnostico()
        self.presentar_diagnostico(resultado, confianza)

        print("\n¿Desea realizar un nuevo análisis? (si/no)")
        if input().lower() in ['si', 'sí', 's', 'yes', 'y']:
            self.respuestas = {}
            self.ejecutar()

# Función principal
def main():
    print("Inicializando Diagnóstico Asistido...")
    sistema = DiagnosticoAsistido()
    sistema.ejecutar()
    print("\n¡Gracias por utilizar el sistema inteligente de Diagnóstico Asistido!")

# Ejecutar el programa
if __name__ == "__main__":
    main()
