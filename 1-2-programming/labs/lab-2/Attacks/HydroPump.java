package lab2.Attacks;
import  ru.ifmo.se.pokemon.*;
public class HydroPump extends SpecialMove {
    public HydroPump(){
        super(Type.WATER, 110, 80);
    }

    @Override
    protected String describe() {
        return "использует специальную атаку Hydro Pump";
    }
}
