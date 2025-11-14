package lab2.Pokemons;
import lab2.Attacks.*;

public class Dodrio extends Doduo{

    private final double hp = 60;
    private final double attack = 110;
    private final double defense = 70;
    private final double spAttack = 60;
    private final double spDefense = 60;
    private final double speed = 110;

    public Dodrio(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
        addMove((new HydroPump()));
    }
}
