package lab2.Attacks;
import ru.ifmo.se.pokemon.*;

public class SandAttack extends StatusMove {
    public SandAttack(){
        super(Type.GROUND, 0, 100);
    }

    @Override
    protected String describe() {
        return "выполняет Sand Attack";
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        Effect e = new Effect().stat(Stat.ACCURACY, -1);

        pokemon.addEffect(e);
    }
}
