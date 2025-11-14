package lab3.classes;

import java.util.Objects;

public abstract class Essence {
    private String name = "Безымянный";

    public Essence(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "lab3.classes.Essence{" +
                "name=" + this.name +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Essence essence = (Essence) o;
        return Objects.equals(this.name, essence.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.name);
    }
}
