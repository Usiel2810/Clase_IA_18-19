package puzzle8;

import java.util.Arrays;

public class StatePuzzle {
    int[][] tablero;
    int filaVacia;
    int columnaVacia;
    int nivel;
    StatePuzzle padre;
    int costo; // Para A* (costo = nivel + heurística)

    public StatePuzzle(int[][] tablero, int filaVacia, int columnaVacia, int nivel, StatePuzzle padre) {
        this.tablero = new int[3][3];
        for (int i = 0; i < 3; i++) {
            System.arraycopy(tablero[i], 0, this.tablero[i], 0, 3);
        }
        this.filaVacia = filaVacia;
        this.columnaVacia = columnaVacia;
        this.nivel = nivel;
        this.padre = padre;
        this.costo = 0;
    }

    public boolean esSolucion() {
        int[][] solucion = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
        return Arrays.deepEquals(tablero, solucion);
    }

    public int calcularHeuristica() {
        // Distancia Manhattan
        int distancia = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int valor = tablero[i][j];
                if (valor != 0) {
                    int filaObjetivo = (valor - 1) / 3;
                    int colObjetivo = (valor - 1) % 3;
                    distancia += Math.abs(i - filaObjetivo) + Math.abs(j - colObjetivo);
                }
            }
        }
        return distancia;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        StatePuzzle otro = (StatePuzzle) obj;
        return Arrays.deepEquals(tablero, otro.tablero);
    }

    @Override
    public int hashCode() {
        return Arrays.deepHashCode(tablero);
    }
}