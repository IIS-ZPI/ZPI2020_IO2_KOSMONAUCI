public class Main  implements IArithmeticsMult, IArithmeticsPow, IArithmeticsDivision, IArithmeticsAdd, IArithmeticsDiff{
    public static void main(String[] args) {
        System.out.println("KOSMONAUCI\nDeveloper-WiktoriaRozanska\nJakubWijata\nDamianWdowiak\nMateuszRoslak\nDeveloper-ProjectAntZ");
    }

    @Override
    public double Division(double A, double B) {
        if(B == 0){
            return 0;
        }
        else{
            return A / B;
        }
    }

    @Override
    public double Multiplication(double A, double B) {
        return A * B;
    }

    @Override
    public double Addition(double A, double B) {
        return A + B;
    }

    @Override
    public double Pow(double A, double B) {
        return Math.pow(A, B);
    }

    @Override
    public double Difference(Double A, Double B) {
        return A - B;
    }

    //Comment 3
}
