package lab2.Attacks;
import ru.ifmo.se.pokemon.*;

public class Charge extends StatusMove {
    public Charge(){
        super(Type.ELECTRIC, 0, 0);
    }

    @Override
    protected String describe() {
        return "выполняет Charge";
    }

    @Override
    protected void applySelfEffects(Pokemon pokemon) {
        Effect e = new Effect().stat(Stat.SPECIAL_DEFENSE, +1);
        pokemon.addEffect(e);
    }
}
