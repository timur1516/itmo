package lab4.classes;
import lab4.Exceptions.NameError;

import java.util.Objects;

public class Thing extends Essence{
    private String material;
    private String color;
    public Thing(String name, String material, String color) {
        super(name);
        if(material == null || material == ""){
            throw new NameError("Необходимо указать материал для предмета " + name);
        }
        if(color == null || color == ""){
            throw new NameError("Необходимо указать цвет для предмета " + name);
        }
        this.material = material;
        this.color = color;
    }

    @Override
    public String toString() {
        return "Thing{" +
                "material='" + material +
                ", color='" + color +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Thing thing = (Thing) o;
        return Objects.equals(material, thing.material) && Objects.equals(color, thing.color);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), material, color);
    }
}
