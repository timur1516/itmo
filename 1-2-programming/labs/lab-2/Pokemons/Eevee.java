package lab2.Pokemons;
import ru.ifmo.se.pokemon.*;

public class Eevee extends Pokemon{

    private final double hp = 55;
    private final double attack = 55;
    private final double defense = 50;
    private final double spAttack = 45;
    private final double spDefense = 65;
    private final double speed = 55;

    public Eevee(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
        setType(Type.NORMAL);
    }
}
