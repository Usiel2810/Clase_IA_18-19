package puzzle8;

import java.util.*;

public class DepthFirstSolver {
    public static void resolver(int[][] estadoInicial) {
        Deque<StatePuzzle> pila = new ArrayDeque<>();
        Set<StatePuzzle> visitados = new HashSet<>();

        StatePuzzle inicial = new StatePuzzle(estadoInicial,
            encontrarFilaVacia(estadoInicial),
            encontrarColumnaVacia(estadoInicial), 0, null);
        pila.push(inicial);
        visitados.add(inicial);

        while (!pila.isEmpty()) {
            StatePuzzle actual = pila.pop();

            if (actual.esSolucion()) {
                imprimirSolucion(actual);
                return;
            }

            for (StatePuzzle vecino : generarVecinos(actual)) {
                if (!visitados.contains(vecino)) {
                    visitados.add(vecino);
                    pila.push(vecino);
                }
            }
        }
        System.out.println("No se encontró solución.");
    }

    // Los métodos auxiliares son idénticos a los de BreadthFirstSolver
}