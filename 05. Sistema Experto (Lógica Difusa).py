# Sistema Experto de Diagnóstico Asistido con Lógica Difusa
# Desarrollado por: Asistente de Soporte Técnico
# Función: Detección de fallos en hardware y software con evaluación difusa

class DiagnosticoAsistidoDifuso:
    def __init__(self):
        self.respuestas = {}
        self.informe = ""
        self.precision = 0

    def definir_base_conocimiento(self):
        """Configura el conjunto de reglas de diagnóstico con pesos difusos"""
        self.reglas = [
            {
                'condiciones': [
                    ('no_inicia', 0.8), 
                    ('sin_indicadores', 0.9)
                ],
                'conclusion': 'Falla en alimentación eléctrica',
                'sugerencia': 'Revise el cable de corriente y fuente de poder',
                'confianza_base': 90
            },
            {
                'condiciones': [
                    ('enciende', 0.7), 
                    ('sin_imagen', 0.9), 
                    ('ventiladores_operando', 0.8)
                ],
                'conclusion': 'Fallo en pantalla o tarjeta gráfica',
                'sugerencia': 'Verificar cableado de video y tarjeta de gráficos',
                'confianza_base': 85
            },
            {
                'condiciones': [
                    ('enciende', 0.6), 
                    ('pitidos_repetidos', 0.95)
                ],
                'conclusion': 'Problema con la memoria RAM',
                'sugerencia': 'Retirar y reinstalar los módulos de RAM',
                'confianza_base': 88
            },
            {
                'condiciones': [
                    ('desempeño_bajo', 0.85), 
                    ('ruido_ventiladores', 0.75)
                ],
                'conclusion': 'Sobrecalentamiento del procesador',
                'sugerencia': 'Limpiar sistema térmico y cambiar pasta disipadora',
                'confianza_base': 75
            },
            {
                'condiciones': [
                    ('error_pantalla', 0.8), 
                    ('reinicios_aleatorios', 0.7)
                ],
                'conclusion': 'Error de software o drivers',
                'sugerencia': 'Actualizar drivers y ejecutar diagnóstico en modo seguro',
                'confianza_base': 70
            },
            {
                'condiciones': [
                    ('sin_internet', 0.9), 
                    ('otros_conectados', 0.85)
                ],
                'conclusion': 'Fallo de configuración de red',
                'sugerencia': 'Reiniciar adaptador de red y revisar parámetros',
                'confianza_base': 80
            }
        ]

    def obtener_datos_usuario(self):
        """Solicita entradas al usuario final con grados de certeza"""
        print("=== SISTEMA DIFUSO DE ANÁLISIS - IDENTIFICACIÓN DE FALLAS ===")
        print("Indique el grado de certeza para cada síntoma (0-100%):\n")

        preguntas = {
            'no_inicia': '¿Qué tan seguro está de que el equipo no enciende en absoluto? (0-100)%: ',
            'sin_indicadores': '¿Qué tan seguro está de que no hay luces ni señales visibles? (0-100)%: ',
            'enciende': '¿Qué tan seguro está de que el equipo arranca pero no funciona correctamente? (0-100)%: ',
            'sin_imagen': '¿Qué tan seguro está de que la pantalla permanece en negro? (0-100)%: ',
            'ventiladores_operando': '¿Qué tan seguro está de que se escuchan los ventiladores funcionando? (0-100)%: ',
            'pitidos_repetidos': '¿Qué tan seguro está de que se oyen sonidos repetitivos al encender? (0-100)%: ',
            'desempeño_bajo': '¿Qué tan seguro está de que el sistema responde lentamente? (0-100)%: ',
            'ruido_ventiladores': '¿Qué tan seguro está de que los ventiladores hacen ruido fuerte? (0-100)%: ',
            'error_pantalla': '¿Qué tan seguro está de que ha aparecido una pantalla azul con errores? (0-100)%: ',
            'reinicios_aleatorios': '¿Qué tan seguro está de que el equipo se reinicia inesperadamente? (0-100)%: ',
            'sin_internet': '¿Qué tan seguro está de que no tiene acceso a internet? (0-100)%: ',
            'otros_conectados': '¿Qué tan seguro está de que otros dispositivos se conectan sin problema? (0-100)%: '
        }

        for clave, pregunta in preguntas.items():
            while True:
                try:
                    valor = float(input(pregunta).strip('%')) / 100.0
                    if 0 <= valor <= 1:
                        self.respuestas[clave] = valor
                        break
                    else:
                        print("Por favor ingrese un valor entre 0 y 100.")
                except ValueError:
                    print("Entrada inválida. Ingrese un número entre 0 y 100.")

    def evaluar_diagnostico_difuso(self):
        """Evalúa reglas con lógica difusa usando el método de Mamdani"""
        resultados = []
        
        for regla in self.reglas:
            # Aplicar operador AND difuso (mínimo)
            grado_activacion = 1.0
            for condicion, peso in regla['condiciones']:
                valor_usuario = self.respuestas.get(condicion, 0.0)
                grado_condicion = min(valor_usuario, peso)
                grado_activacion = min(grado_activacion, grado_condicion)
            
            if grado_activacion > 0:
                # Calcular confianza ajustada
                confianza_ajustada = regla['confianza_base'] * grado_activacion
                resultados.append({
                    'conclusion': regla['conclusion'],
                    'sugerencia': regla['sugerencia'],
                    'confianza': confianza_ajustada,
                    'grado_activacion': grado_activacion
                })
        
        # Ordenar resultados por confianza descendente
        resultados.sort(key=lambda x: x['confianza'], reverse=True)
        return resultados

    def presentar_diagnostico_difuso(self, resultados):
        """Muestra el diagnóstico final al usuario con lógica difusa"""
        print("\n" + "="*50)
        print("RESULTADO DEL DIAGNÓSTICO DIFUSO")
        print("="*50)

        if resultados:
            print("\nPosibles diagnósticos ordenados por confianza:")
            for i, resultado in enumerate(resultados[:3], 1):  # Mostrar top 3
                print(f"\nOpción #{i}:")
                print(f"Diagnóstico: {resultado['conclusion']}")
                print(f"Grado de activación: {resultado['grado_activacion']*100:.1f}%")
                print(f"Confianza ajustada: {resultado['confianza']:.1f}%")
                print(f"Recomendación: {resultado['sugerencia']}")
                
                if resultado['confianza'] >= 80:
                    print("✅ Diagnóstico con alta certeza")
                elif resultado['confianza'] >= 60:
                    print("⚠️ Diagnóstico con certeza moderada")
                else:
                    print("❓ Diagnóstico con baja certeza")
        else:
            print("❌ No se encontraron diagnósticos relevantes con la información proporcionada.")
            print("Sugerencia: Consulte a un técnico especializado o proporcione más detalles.")

    def ejecutar(self):
        """Proceso principal del sistema con lógica difusa"""
        self.definir_base_conocimiento()
        self.obtener_datos_usuario()
        resultados = self.evaluar_diagnostico_difuso()
        self.presentar_diagnostico_difuso(resultados)

        print("\n¿Desea realizar un nuevo análisis? (si/no)")
        if input().lower() in ['si', 'sí', 's', 'yes', 'y']:
            self.respuestas = {}
            self.ejecutar()

# Función principal
def main():
    print("Inicializando Diagnóstico Asistido con Lógica Difusa...")
    sistema = DiagnosticoAsistidoDifuso()
    sistema.ejecutar()
    print("\n¡Gracias por utilizar el sistema inteligente de Diagnóstico Asistido!")

# Ejecutar el programa
if __name__ == "__main__":
    main()