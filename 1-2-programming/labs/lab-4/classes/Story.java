package lab4.classes;

import lab4.Exceptions.WearingException;
import lab4.enums.*;

public class Story {
    private Story() {}

    public static void tell() {
        Human king = new Human("Король", Gender.MALE, "Правитель");
        Human hat = new Human("Шляпа", Gender.MALE, "Шляпных Дел Мастер");
        Human queen = new Human("Королева", Gender.FEMALE, "Правитель");
        Human sonia = new Human("Соня", Gender.FEMALE);
        Human someJudge = new Human("Неизвестный судья", Gender.MALE);
        AnonymousGroupOfPeople jury = new AnonymousGroupOfPeople("Присяжные", "Работники суда");

        Human.ClothesItem glasses = new Human.ClothesItem("очки", "металл", "белый");
        Thing cup = new Thing("чашка", "стекло", "красный");

        MagicClothesItem shoes = new MagicClothesItem("ботинки", "кожа", "оранжевый", hat) {
            @Override
            public void fly() {
                System.out.println(this.getName() + " слетели с " + this.carrier.getName());
                this.carrier.removeClothes(this);
                this.weared = false;
                this.carrier = null;
            }
        };

        king.order("сними свою шляпу.", hat);
        hat.answer("Она не моя-с!");
        king.shout("Краденая!");
        king.completeAction(Action.ROTATETO, jury);
        Object result = jury.write("Шляпа - вор!", "Gotic");
        System.out.println("Результат: " + result);
        hat.explain("Я их держу для продажи-с, у меня своих нет, ведь я " + hat.getJob());

        try {
            glasses.wear(queen);
        }catch (WearingException e){
            System.out.println(e.getMessage());
        }

        queen.completeAction(Action.GAZE, hat);

        hat.setName("Свидетель");
        king.say("давайте показания и не волнуйтесь, не то я велю казнить вас на месте.", hat);
        hat.setName("Шляпа");
        hat.setState(State.NERVOUS);
        hat.completeAction(Action.STARE, queen);
        hat.setState(State.SCARED, cup);

        sonia.completeAction(Action.CHANGEPOS);
        queen.order("принесите-ка мне программу вчерашнего концерта!", someJudge);
        hat.completeAction(Action.SHAKE);
    }
}
