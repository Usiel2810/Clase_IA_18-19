package puzzle8;

public class EightPuzzle {
    public static void main(String[] args) {
        int[][] tableroInicial = {
            {2, 8, 4},
            {7, 0, 1},
            {6, 5, 3}
        };

        System.out.println("=== Búsqueda en Anchura (BFS) ===");
        BreadthFirstSolver.resolver(tableroInicial);

        System.out.println("\n=== Búsqueda en Profundidad (DFS) ===");
        DepthFirstSolver.resolver(tableroInicial);

        System.out.println("\n=== Búsqueda A* ===");
        AStarSolver.resolver(tableroInicial);
    }
}