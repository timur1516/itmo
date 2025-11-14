package lab2.Pokemons;
import lab2.Attacks.*;
import ru.ifmo.se.pokemon.*;
public class Tentacruel extends Tentacool{

    private final double hp = 80;
    private final double attack = 70;
    private final double defense = 65;
    private final double spAttack = 80;
    private final double spDefense = 120;
    private final double speed = 100;

    public Tentacruel(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
        setMove((new SandAttack()), (new Sketch()),
                (new Aeroblast()), (new ThunderShock()));
        setType(Type.WATER, Type.POISON);
    }
}
