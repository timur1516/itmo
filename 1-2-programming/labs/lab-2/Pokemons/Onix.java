package lab2.Pokemons;
import ru.ifmo.se.pokemon.*;

public class Onix extends Pokemon{

    private final double hp = 35;
    private final double attack = 45;
    private final double defense = 160;
    private final double spAttack = 30;
    private final double spDefense = 45;
    private final double speed = 70;

    public Onix(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
        setType(Type.ROCK, Type.GROUND);
    }
}
