package lab4.Exceptions;
import lab4.classes.Human;
import lab4.enums.Action;

public class NoObjectForAction extends RuntimeException{
    static private String message = "Необходимо указать объект к которму применено действие!";
    Human human;
    Action action;
    public NoObjectForAction(Human human, Action action){
        super(message);
        this.human = human;
        this.action = action;
    }

    @Override
    public String getMessage() {
        String resultMessage = message;
        resultMessage += "\n" + "При попытке выполения дейсвия " + this.action.toString() + " человеком " + this.human.getName() +
                ", не был передан объект над которым выполнятеся действие";
        return resultMessage;
    }
}
