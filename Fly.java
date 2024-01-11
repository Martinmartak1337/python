import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Fly {
    public static void main(String[] args){
        System.out.println(new Fly().idealVectorValue(5, 2, 1, 8));
        mainGameLoop();
        //System.out.println(new Fly().returnTheLastListOfCharacters(new Fly().forwardList(new Fly().createField(), 7), 7));
    }
    public List createField(){
        return new ArrayList(64);
    }
    public int randomReturn(){
        return new Random().nextInt(0, 8);
    }
    public double idealVectorValue(double... values){
        double f = 0.00;
        for( double m: values){
            f+=Math.pow(m, values.length);
        }
        return Math.pow(f, 1/values.length);
    }
    public static char[] characterTypesForField(){
        char[] a = new char[2];
        a[0] = '#';
        a[1] = '$';
        return a;
    }
    public List forwardList(List mewNew, int n){
        char[] f=characterTypesForField();
        int k = 0;
        while (k < 64){
            mewNew.add(0);
            k++;
        }
        for (int i = 0; i < n; i++) {
            mewNew.set(i*8+randomReturn(), f[0]);
        }
        mewNew.set(56+randomReturn(), f[1]);
        return mewNew;
}
    public List<Integer> Counter(List<Integer> a, int c, int b){
        a.stream().
                filter(integer -> a.size() > 0).close();
        a.set(c, b);
        return a;
    }
    public List returnTheLastListOfCharacters(List i, int m){
       return i.subList(m*8, (m*8)+8);
    }
    public static List mainGameLoop(){
        List l  = new Fly().returnTheLastListOfCharacters(new Fly().forwardList(new Fly().createField(), 7), 7);
        System.out.println(l);

        return l;
    }
}
