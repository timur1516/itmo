package lab2.Attacks;
import ru.ifmo.se.pokemon.*;
import java.util.Random;
public class Magnitude extends PhysicalMove {
    public Magnitude(){
        super(Type.GROUND, 0, 100);
    }

    @Override
    protected String describe() {
        return "использует атаку Magnitude";
    }

    @Override
    protected double calcBaseDamage(Pokemon pokemon, Pokemon pokemon1) {
        Random rand = new Random();
        int a = rand.nextInt(1, 101);
        double p = 0;
        if(a > 0 && a <= 5) p = 10;
        if(a > 5 && a <= 15) p = 30;
        if(a > 15 && a <= 35) p = 50;
        if(a > 35 && a <= 65) p = 70;
        if(a > 65 && a <= 85) p = 90;
        if(a > 85 && a <= 95) p = 110;
        if(a > 95 && a <= 100) p = 150;

        return (0.4 * (double)pokemon.getLevel() + 2.0) * p / 150.0;
    }
}
