package lab2.Attacks;
import ru.ifmo.se.pokemon.*;
public class Sketch extends StatusMove {
    public Sketch(){
        super(Type.NORMAL, 0, 0);
    }
    @Override
    protected String describe() {
        return "выполняет Sketch";
    }
}
