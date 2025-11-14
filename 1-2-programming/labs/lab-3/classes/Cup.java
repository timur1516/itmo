package lab3.classes;

public class Cup extends Essence {
    private String material;
    private String color;
    public Cup(String name, String material, String color) {
        super(name);
        this.color = color;
        this.material = material;
    }

    @Override
    public String toString() {
        return "lab3.classes.Cup{" +
                "name=" + this.getName() +
                ", material=" + this.material +
                ", color=" + color +
                '}';
    }
}
