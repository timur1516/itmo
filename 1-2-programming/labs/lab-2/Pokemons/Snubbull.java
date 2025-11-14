package lab2.Pokemons;
import lab2.Attacks.*;
import ru.ifmo.se.pokemon.*;

public class Snubbull extends Pokemon{

    private final double hp = 60;
    private final double attack = 80;
    private final double defense = 50;
    private final double spAttack = 40;
    private final double spDefense = 40;
    private final double speed = 30;

    public Snubbull(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
        setMove((new Growl()), (new HydroPump()),
                (new IcePunch()), (new Rage()));
        setType(Type.FAIRY);
    }
}
