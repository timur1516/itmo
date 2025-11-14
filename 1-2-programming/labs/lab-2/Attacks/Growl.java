package lab2.Attacks;
import ru.ifmo.se.pokemon.*;
public class Growl extends StatusMove {
    public Growl(){
        super(Type.NORMAL, 0, 100);
    }

    @Override
    protected String describe() {
        return "выполняет Growl";
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        Effect e = new Effect().stat(Stat.ATTACK, -1);
        pokemon.addEffect(e);
    }
}
