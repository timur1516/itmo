package lab2.Attacks;
import ru.ifmo.se.pokemon.*;

public class ThunderShock extends SpecialMove {
    public ThunderShock(){
        super(Type.ELECTRIC, 40, 100);
    }

    @Override
    protected String describe() {
        return "использует специальную атаку Thunder Shock";
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        Effect e = new Effect().chance(0.1);
        e.paralyze(pokemon);
    }
}
