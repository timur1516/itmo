package lab2.Pokemons;
import lab2.Attacks.*;
import ru.ifmo.se.pokemon.*;

public class Steelix extends Onix{

    private final double hp = 75;
    private final double attack = 85;
    private final double defense = 200;
    private final double spAttack = 55;
    private final double spDefense = 65;
    private final double speed = 30;

    public Steelix(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
        setMove((new Growl()), (new HydroPump()),
                (new IcePunch()));
        setType(Type.STEEL, Type.GROUND);
    }
}
