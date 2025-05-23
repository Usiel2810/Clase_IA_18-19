package 8Puzzle;

public class EightPuzzle {
    public static void main(String[] args) 
    {
        int[][] tableroInicial = {
            {2, 8, 4},
            {7, 0, 1},
            {6, 5, 3}
        };

        SolucionadorPuzzle.resolver(tableroInicial);
    }
}