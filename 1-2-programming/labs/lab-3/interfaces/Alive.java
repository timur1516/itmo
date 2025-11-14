package lab3.interfaces;

import lab3.enums.Action;
import lab3.classes.Essence;
import lab3.enums.State;
public interface Alive {
    State getState();
    void setState(State state, Essence obj);
    void setState(State state);
    String completeAction(Action action, Essence var1);
    String completeAction(Action action);
}
