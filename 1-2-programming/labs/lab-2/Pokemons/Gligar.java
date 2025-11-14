package lab2.Pokemons;
import ru.ifmo.se.pokemon.*;

public class Gligar extends Pokemon{

    private final double hp = 65;
    private final double attack = 75;
    private final double defense = 105;
    private final double spAttack = 35;
    private final double spDefense = 65;
    private final double speed = 85;

    public Gligar(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
        setType(Type.GROUND, Type.FLYING);
    }
}
