package lab4.classes;
import lab4.interfaces.Flyable;
abstract class MagicClothesItem extends Human.ClothesItem implements Flyable{

    public MagicClothesItem(String name, String material, String color) {
        super(name, material, color);
    }

    public MagicClothesItem(String name, String material, String color, Human carrier) {
        super(name, material, color, carrier);
    }
}
