package lab4.interfaces;

import lab4.classes.Essence;
import lab4.enums.Action;
import lab4.enums.State;
public interface Alive {
    State getState();
    void setState(State state, Essence obj);
    void setState(State state);
    void completeAction(Action action, Essence var1);
    void completeAction(Action action);
}
