package lab2.Attacks;
import ru.ifmo.se.pokemon.*;
public class IcePunch extends PhysicalMove{
    public IcePunch(){
        super(Type.ICE, 75, 100);
    }

    @Override
    protected String describe() {
        return "использует атаку Ice Punch";
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        Effect e = new Effect().chance(0.1);
        e.freeze(pokemon);
    }
}
