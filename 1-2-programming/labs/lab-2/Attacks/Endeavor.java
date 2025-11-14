package lab2.Attacks;
import ru.ifmo.se.pokemon.*;

public class Endeavor extends PhysicalMove {
    public Endeavor(){
        super(Type.NORMAL, 0, 100);
    }

    @Override
    protected String describe() {
        return "использует атаку Endeavor";
    }

    @Override
    protected boolean checkAccuracy(Pokemon pokemon, Pokemon pokemon1) {
        if(pokemon.getHP() < pokemon1.getHP()){
            pokemon1.setMod(Stat.HP, (int) Math.round(pokemon1.getHP() - pokemon.getHP()));
        }

        return super.checkAccuracy(pokemon, pokemon1);
    }
}
