class RedSemantica:
    def __init__(self):
        self.conceptos = {}
    
    def agregar_concepto(self, nombre):
        if nombre not in self.conceptos:
            self.conceptos[nombre] = {}
    
    def agregar_relacion(self, origen, tipo_rel, destino):
        self.agregar_concepto(origen)
        self.agregar_concepto(destino)
        
        if tipo_rel not in self.conceptos[origen]:
            self.conceptos[origen][tipo_rel] = []
        
        self.conceptos[origen][tipo_rel].append(destino)
    
    def obtener_relaciones(self, concepto):
        if concepto in self.conceptos:
            return self.conceptos[concepto]
        return {}
    
    def consultar(self, concepto, tipo_rel):
        if concepto in self.conceptos and tipo_rel in self.conceptos[concepto]:
            return self.conceptos[concepto][tipo_rel]
        return []
    
    def mostrar_red(self):
        for concepto, relaciones in self.conceptos.items():
            print(f"Concepto: {concepto}")
            for relacion, destinos in relaciones.items():
                for destino in destinos:
                    print(f"  →{relacion}→ {destino}")


# Ejemplo con animales
if __name__ == "__main__":
    conocimiento = RedSemantica()
    
    # Jerarquía taxonómica
    conocimiento.agregar_relacion("Animal", "es_un", "Ser vivo")
    conocimiento.agregar_relacion("Mamífero", "es_un", "Animal")
    conocimiento.agregar_relacion("Ave", "es_un", "Animal")
    conocimiento.agregar_relacion("Pez", "es_un", "Animal")
    
    conocimiento.agregar_relacion("León", "es_un", "Mamífero")
    conocimiento.agregar_relacion("Gato", "es_un", "Mamífero")  
    conocimiento.agregar_relacion("Elefante", "es_un", "Mamífero")
    
    conocimiento.agregar_relacion("Águila", "es_un", "Ave")
    conocimiento.agregar_relacion("Búho", "es_un", "Ave")
    
    conocimiento.agregar_relacion("Tiburón", "es_un", "Pez")
    conocimiento.agregar_relacion("Pez payaso", "es_un", "Pez")
    
    # Características
    conocimiento.agregar_relacion("Mamífero", "tiene", "pelaje")
    conocimiento.agregar_relacion("Ave", "tiene", "plumas")
    conocimiento.agregar_relacion("Pez", "tiene", "escamas")
    
    # Habilidades
    conocimiento.agregar_relacion("León", "puede", "rugir")
    conocimiento.agregar_relacion("Gato", "puede", "maullar")
    conocimiento.agregar_relacion("Elefante", "puede", "trompetear")
    conocimiento.agregar_relacion("Águila", "puede", "volar alto")
    conocimiento.agregar_relacion("Búho", "puede", "girar cabeza 270°")
    conocimiento.agregar_relacion("Tiburón", "puede", "detectar sangre")
    conocimiento.agregar_relacion("Pez payaso", "puede", "vivir en anémonas")
    
    # Limitaciones
    conocimiento.agregar_relacion("Búho", "no puede", "mover los ojos")
    conocimiento.agregar_relacion("Tiburón", "no puede", "dejar de nadar")
    
    print("Red de conocimiento animal:")
    conocimiento.mostrar_red()
    
    print("\nConsultas específicas:")
    print(f"¿Qué es un León? {conocimiento.consultar('León', 'es_un')}")
    print(f"¿Qué puede hacer un Elefante? {conocimiento.consultar('Elefante', 'puede')}")
    print(f"¿Qué características tienen los peces? {conocimiento.consultar('Pez', 'tiene')}")
    print(f"¿Qué limitaciones tiene un Búho? {conocimiento.consultar('Búho', 'no puede')}")