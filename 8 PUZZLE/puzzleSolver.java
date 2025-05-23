package 8Puzzle;

import java.util.*;

class SolucionadorPuzzle {
    public static void resolver(int[][] tableroInicial) 
    {
        PriorityQueue<EstadoPuzzle> listaAbierta = new PriorityQueue<>(Comparator.comparingInt(a -> a.costoTotal));
        Set<EstadoPuzzle> listaCerrada = new HashSet<>();

        EstadoPuzzle estadoInicial = new EstadoPuzzle(tableroInicial, 1, 1, 0, null);
        listaAbierta.add(estadoInicial);

        while (!listaAbierta.isEmpty()) {
            EstadoPuzzle estadoActual = listaAbierta.poll();

            if (estadoActual.esEstadoFinal()) {
                mostrarSolucion(estadoActual);
                return;
            }

            listaCerrada.add(estadoActual);

            for (EstadoPuzzle estadoHijo : estadoActual.generarEstadosHijos()) {
                if (!listaCerrada.contains(estadoHijo)) {
                    listaAbierta.add(estadoHijo);
                }
            }
        }
        System.out.println("No Se Encontró Solución.");
    }

    private static void mostrarSolucion(EstadoPuzzle estadoFinal) 
    {
        List<EstadoPuzzle> caminoSolucion = new ArrayList<>();
        while (estadoFinal != null) {
            caminoSolucion.add(estadoFinal);
            estadoFinal = estadoFinal.estadoAnterior;
        }
        Collections.reverse(caminoSolucion);

        for (EstadoPuzzle estado : caminoSolucion) {
            imprimirTablero(estado.tableroActual);
            System.out.println();
        }
    }

    private static void imprimirTablero(int[][] tablero) 
    {
        for (int[] fila : tablero) {
            for (int valor : fila) {
                System.out.print(valor + " ");
            }
            System.out.println();
        }
    }
}