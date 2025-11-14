package lab2.Attacks;
import ru.ifmo.se.pokemon.*;

public class Aeroblast extends SpecialMove {
    public Aeroblast(){
        super(Type.FLYING, 100, 95);
    }

    @Override
    protected String describe() {
        return "использует специальную атаку Aeroblast";
    }
    //увеличение шанса критического удара до 1/8
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
