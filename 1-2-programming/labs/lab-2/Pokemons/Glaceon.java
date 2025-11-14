package lab2.Pokemons;
import lab2.Attacks.*;
import ru.ifmo.se.pokemon.*;

public class Glaceon extends Eevee{

    private final double hp = 65;
    private final double attack = 60;
    private final double defense = 110;
    private final double spAttack = 130;
    private final double spDefense = 95;
    private final double speed = 65;

    public Glaceon(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
        setMove((new Charge()), (new CrossChop()),
                (new Endeavor()));
        setType(Type.ICE);
    }
}
