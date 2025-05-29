package puzzle8;

import java.util.*;

public class AStarSolver {
    public static void resolver(int[][] estadoInicial) {
        PriorityQueue<StatePuzzle> colaPrioridad = new PriorityQueue<>(
            Comparator.comparingInt(a -> a.costo));
        Set<StatePuzzle> visitados = new HashSet<>();

        StatePuzzle inicial = new StatePuzzle(estadoInicial,
            encontrarFilaVacia(estadoInicial),
            encontrarColumnaVacia(estadoInicial), 0, null);
        inicial.costo = inicial.calcularHeuristica();
        colaPrioridad.add(inicial);
        visitados.add(inicial);

        while (!colaPrioridad.isEmpty()) {
            StatePuzzle actual = colaPrioridad.poll();

            if (actual.esSolucion()) {
                imprimirSolucion(actual);
                return;
            }

            for (StatePuzzle vecino : generarVecinos(actual)) {
                if (!visitados.contains(vecino)) {
                    vecino.costo = vecino.nivel + vecino.calcularHeuristica();
                    visitados.add(vecino);
                    colaPrioridad.add(vecino);
                }
            }
        }
        System.out.println("No se encontró solución.");
    }

    // Los métodos auxiliares son idénticos a los anteriores
}