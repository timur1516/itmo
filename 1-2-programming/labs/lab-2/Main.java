package lab2;
import lab2.Pokemons.*;
import ru.ifmo.se.pokemon.*;

public class Main {
    public static void main(String[] args) {
        Battle b = new Battle();
        b.addAlly((new Tentacruel("Tent", 1)));
        b.addAlly((new Gliscor("Glis", 1)));
        b.addAlly((new Steelix("Stee", 1)));

        b.addFoe((new Glaceon("Glac", 1)));
        b.addFoe((new Dodrio("Dodr", 1)));
        b.addFoe((new Snubbull("Snub", 1)));
        b.go();
    }
}
