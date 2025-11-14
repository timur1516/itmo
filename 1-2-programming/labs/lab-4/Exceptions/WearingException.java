package lab4.Exceptions;

import lab4.classes.Human;

public class WearingException extends Exception{
    private String message;
    private Human human;
    private Human.ClothesItem item;
    public WearingException(String message, Human.ClothesItem item, Human human){
        super(message);
        this.message = message;
        this.human = human;
        this.item = item;
    }

    @Override
    public String getMessage() {
        return "\n!!!EXCEPTION!!!\n" + message + "\n!!!EXCEPTION!!!\n";
    }
}
