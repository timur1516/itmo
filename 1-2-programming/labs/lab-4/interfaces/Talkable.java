package lab4.interfaces;

import lab4.classes.Human;

public interface Talkable {
    public void say(String phrase, Human companion);
    public void shout(String phrase);
    public void order(String phrase, Human companion);
    public void explain(String phrase);
    public void answer(String phrase);
}
