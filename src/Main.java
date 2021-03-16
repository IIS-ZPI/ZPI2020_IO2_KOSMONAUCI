public class Main implements IArithmeticsDivision{
    public static void main(String[] args) {
        System.out.println("KOSMONAUCI\nDeveloper-WiktoriaRozanska\nJakubWijata\nDamianWdowiak\nMateuszRoslak\nDeveloper-ProjectAntZ");
    }

    @Override
    public double Division(double A, double B) {
        if(B == 0){
            return 0;
        }
        else{
            return A/B;
        }
    }
}
