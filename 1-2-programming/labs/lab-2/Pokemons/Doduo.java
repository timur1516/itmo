package lab2.Pokemons;
import lab2.Attacks.*;
import ru.ifmo.se.pokemon.*;

public class Doduo extends Pokemon{

    private final double hp = 35;
    private final double attack = 85;
    private final double defense = 45;
    private final double spAttack = 35;
    private final double spDefense = 35;
    private final double speed = 75;

    public Doduo(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
        setMove((new Growl()));
        setType(Type.NORMAL, Type.FLYING);
    }
}
