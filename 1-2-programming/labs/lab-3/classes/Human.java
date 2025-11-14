package lab3.classes;

import lab3.enums.Action;
import lab3.enums.Gender;
import lab3.enums.State;
import lab3.interfaces.Alive;

import java.util.Objects;

public class Human extends Essence implements Alive {
    private State state;
    private Gender gender;
    public Human(String name, Gender gender) {
        super(name);
        this.gender = gender;
        this.state = State.NORMAL;
    }

    @Override
    public State getState() {
        return this.state;
    }

    public Gender getGender() {
        return this.gender;
    }

    @Override
    public void setState(State state, Essence obj) {
        this.state = state;
        System.out.println(this.getName() + " " + this.state.describe(this.gender));

        if(state == State.SCARED) System.out.println(this.completeAction(Action.BITE, obj));
    }

    @Override
    public void setState(State state) {
        this.state = state;
        System.out.println(this.getName() + " " + this.state.describe(this.gender));

        if(state == State.NERVOUS) System.out.println(this.completeAction(Action.SHIFT));
    }

    @Override
    public String completeAction(Action action, Essence var1) {
        return action.applyEssenceAction(this, var1);
    }
    @Override
    public String completeAction(Action action) {
        return action.applySelfAction(this);
    }
    public String say(String phrase) {

        String verb = switch (this.gender){
            case MALE -> "сказал";
            case FEMALE -> "сказала";
        };
        return this.getName() + " " + verb + ": " + phrase;
    }
    public String say(String phrase, Human var1) {
        String verb = switch (this.gender){
            case MALE -> "сказал";
            case FEMALE -> "сказала";
        };
        return var1.getName() + "," + "- " + verb + " " + this.getName() + " -," + phrase;
    }

    @Override
    public String toString() {
        return "lab3.classes.Human{" +
                "name=" + this.getName() +
                ", state=" + this.state +
                ", gender=" + this.gender +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Human human = (Human) o;
        return Objects.equals(this.state, human.state) && Objects.equals(this.gender, human.gender);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), state, gender);
    }
}
