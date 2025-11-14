package lab2.Attacks;
import ru.ifmo.se.pokemon.*;

public class CrossChop extends PhysicalMove {
    public CrossChop(){
        super(Type.FIGHTING, 100, 80);
    }

    @Override
    protected String describe() {
        return "использует атаку Cross Chop";
    }

    @Override
    protected double calcCriticalHit(Pokemon pokemon, Pokemon pokemon1) {
        if (1./8. > Math.random()) {
            System.out.println("Критический удар!");
            return 2.0;
        } else {
            return 1.0;
        }
    }
}
