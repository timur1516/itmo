package lab2.Pokemons;
import ru.ifmo.se.pokemon.*;
public class Tentacool extends Pokemon{
    private final double hp = 40;
    private final double attack = 40;
    private final double defense = 35;
    private final double spAttack = 50;
    private final double spDefense = 100;
    private final double speed = 70;
    Tentacool(String name, int level){
        super(name, level);
        setStats(hp, attack, defense, spAttack, spDefense, speed);
    }
}
