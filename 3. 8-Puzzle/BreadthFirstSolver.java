package puzzle8;

import java.util.*;

public class BreadthFirstSolver {
    public static void resolver(int[][] estadoInicial) {
        Queue<StatePuzzle> cola = new LinkedList<>();
        Set<StatePuzzle> visitados = new HashSet<>();

        StatePuzzle inicial = new StatePuzzle(estadoInicial, 
            encontrarFilaVacia(estadoInicial), 
            encontrarColumnaVacia(estadoInicial), 0, null);
        cola.add(inicial);
        visitados.add(inicial);

        while (!cola.isEmpty()) {
            StatePuzzle actual = cola.poll();

            if (actual.esSolucion()) {
                imprimirSolucion(actual);
                return;
            }

            for (StatePuzzle vecino : generarVecinos(actual)) {
                if (!visitados.contains(vecino)) {
                    visitados.add(vecino);
                    cola.add(vecino);
                }
            }
        }
        System.out.println("No se encontró solución.");
    }

    private static List<StatePuzzle> generarVecinos(StatePuzzle estado) {
        List<StatePuzzle> vecinos = new ArrayList<>();
        int[] movimientosFila = {-1, 0, 1, 0};
        int[] movimientosColumna = {0, 1, 0, -1};

        for (int i = 0; i < 4; i++) {
            int nuevaFila = estado.filaVacia + movimientosFila[i];
            int nuevaColumna = estado.columnaVacia + movimientosColumna[i];

            if (nuevaFila >= 0 && nuevaFila < 3 && nuevaColumna >= 0 && nuevaColumna < 3) {
                int[][] nuevoTablero = new int[3][3];
                for (int r = 0; r < 3; r++) {
                    System.arraycopy(estado.tablero[r], 0, nuevoTablero[r], 0, 3);
                }
                nuevoTablero[estado.filaVacia][estado.columnaVacia] = nuevoTablero[nuevaFila][nuevaColumna];
                nuevoTablero[nuevaFila][nuevaColumna] = 0;
                vecinos.add(new StatePuzzle(nuevoTablero, nuevaFila, nuevaColumna, estado.nivel + 1, estado));
            }
        }
        return vecinos;
    }

    private static void imprimirSolucion(StatePuzzle estadoFinal) {
        List<StatePuzzle> camino = new ArrayList<>();
        while (estadoFinal != null) {
            camino.add(estadoFinal);
            estadoFinal = estadoFinal.padre;
        }
        Collections.reverse(camino);

        System.out.println("\nSolución encontrada en " + (camino.size() - 1) + " movimientos:");
        for (StatePuzzle estado : camino) {
            imprimirTablero(estado.tablero);
            System.out.println();
        }
    }

    private static void imprimirTablero(int[][] tablero) {
        for (int[] fila : tablero) {
            for (int valor : fila) {
                System.out.print(valor + " ");
            }
            System.out.println();
        }
    }

    private static int encontrarFilaVacia(int[][] tablero) {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (tablero[i][j] == 0) return i;
        return -1;
    }

    private static int encontrarColumnaVacia(int[][] tablero) {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (tablero[i][j] == 0) return j;
        return -1;
    }
}