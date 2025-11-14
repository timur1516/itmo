package lab2.Attacks;
import ru.ifmo.se.pokemon.*;

public class Rage extends PhysicalMove {
    public Rage(){
        super(Type.NORMAL, 20, 100);
    }

    @Override
    protected String describe() {
        return "использует атаку Rage";
    }

    @Override
    protected void applySelfEffects(Pokemon pokemon) {
        Effect e = new Effect().stat(Stat.ATTACK, +1);
        pokemon.addEffect(e);
    }
}
