package 8Puzzle;

import java.util.*;

class EstadoPuzzle {
    int[][] tableroActual;
    int filaVacia, columnaVacia;
    int costoTotal;
    int nivel;
    EstadoPuzzle estadoAnterior;

    public EstadoPuzzle(int[][] tablero, int filaVacia, int columnaVacia, int nivel, EstadoPuzzle estadoAnterior) 
    {
        this.tableroActual = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                this.tableroActual[i][j] = tablero[i][j];
            }
        }
        this.filaVacia = filaVacia;
        this.columnaVacia = columnaVacia;
        this.nivel = nivel;
        this.estadoAnterior = estadoAnterior;
        this.costoTotal = calcularCostoTotal();
    }

    private int calcularCostoTotal() 
    {
        int costoHeuristico = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (tableroActual[i][j] != 0) {
                    int filaObjetivo = (tableroActual[i][j] - 1) / 3;
                    int columnaObjetivo = (tableroActual[i][j] - 1) % 3;
                    costoHeuristico += Math.abs(i - filaObjetivo) + Math.abs(j - columnaObjetivo);
                }
            }
        }
        return costoHeuristico + nivel;
    }

    public boolean esEstadoFinal() 
    {
        int[][] tableroFinal = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
        return Arrays.deepEquals(tableroActual, tableroFinal);
    }

    public List<EstadoPuzzle> generarEstadosHijos() 
    {
        List<EstadoPuzzle> estadosHijos = new ArrayList<>();
        int[] movimientosFila = {-1, 0, 1, 0};
        int[] movimientosColumna = {0, 1, 0, -1};

        for (int i = 0; i < 4; i++) {
            int nuevaFila = filaVacia + movimientosFila[i];
            int nuevaColumna = columnaVacia + movimientosColumna[i];

            if (nuevaFila >= 0 && nuevaFila < 3 && nuevaColumna >= 0 && nuevaColumna < 3) {
                int[][] nuevoTablero = new int[3][3];
                for (int r = 0; r < 3; r++) {
                    for (int c = 0; c < 3; c++) {
                        nuevoTablero[r][c] = tableroActual[r][c];
                    }
                }
                nuevoTablero[filaVacia][columnaVacia] = nuevoTablero[nuevaFila][nuevaColumna];
                nuevoTablero[nuevaFila][nuevaColumna] = 0;
                estadosHijos.add(new EstadoPuzzle(nuevoTablero, nuevaFila, nuevaColumna, nivel + 1, this));
            }
        }
        return estadosHijos;
    }

    @Override
    public boolean equals(Object obj) 
    {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        EstadoPuzzle otro = (EstadoPuzzle) obj;
        return Arrays.deepEquals(tableroActual, otro.tableroActual);
    }

    @Override
    public int hashCode() 
    {
        return Arrays.deepHashCode(tableroActual);
    }
}