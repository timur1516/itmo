package lab4.classes;

import lab4.Exceptions.NameError;

import java.util.Objects;

public abstract class Essence {
    private String name = "Безымянный";

    public Essence(String name) {
        if(name == null || name == ""){
            throw new NameError("Сущность должна иметь имя!");
        }
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    @Override
    public String toString() {
        return "lab4.classes.Essence{" +
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
