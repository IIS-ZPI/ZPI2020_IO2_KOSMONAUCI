public class Main  implements IArithmeticsMult, IArithmeticsPow{
    public static void main(String[] args) {
        System.out.println("KOSMONAUCI\nDeveloper-WiktoriaRozanska\nJakubWijata\nDamianWdowiak\nMateuszRoslak\nDeveloper-ProjectAntZ");
    }

    @Override
    public double Multiplication(double a, double b) {
        return a*b;


    @Override
    public double Addition(double A, double B) {
        return A+B;

    }

    @Override
    public double Modulo(double A, double B) {
        return Math.pow(A, B);
    }
}
