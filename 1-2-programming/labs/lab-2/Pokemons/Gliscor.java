package lab2.Pokemons;
import lab2.Attacks.*;
import ru.ifmo.se.pokemon.*;

public class Gliscor extends Gligar{

    private final double hp = 75;
    private final double attack = 95;
    private final double defense = 125;
    private final double spAttack = 45;
    private final double spDefense = 75;
    private final double speed = 95;

    public Gliscor(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
        setMove((new Charge()), (new CrossChop()),
                (new Endeavor()), (new Magnitude()));
        setType(Type.GROUND, Type.FLYING);
    }
}
