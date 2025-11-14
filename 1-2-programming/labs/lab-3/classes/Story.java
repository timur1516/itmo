package lab3.classes;
import lab3.enums.*;
public class Story {
    private Story() {}

    public static void tell() {
        Human king = new Human("Король", Gender.MALE);
        Human hat = new Human("Свидетель", Gender.MALE);
        Human queen = new Human("Королева", Gender.FEMALE);
        Cup cup = new Cup("Чашка", "Стекло", "Красная");
        System.out.println(king.say("давайте показания и не волнуйтесь, не то я велю казнить вас на месте.", hat));
        hat.setName("Шляпа");
        hat.setState(State.NERVOUS);
        System.out.println(hat.completeAction(Action.STARE, queen));
        hat.setState(State.SCARED, cup);
    }
}
