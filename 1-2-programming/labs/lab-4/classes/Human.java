package lab4.classes;

import lab4.Exceptions.NameError;
import lab4.Exceptions.WearingException;
import lab4.enums.Action;
import lab4.enums.Gender;
import lab4.enums.State;
import lab4.interfaces.Alive;
import lab4.interfaces.Talkable;
import lab4.interfaces.Writeable;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Human extends Essence implements Alive, Talkable {
    private State state;
    private Gender gender;
    private String job = "Безработный";
    private ArrayList<Human.ClothesItem> clothes = new ArrayList<>();
    public Human(String name, Gender gender) {
        super(name);
        this.gender = gender;
        this.state = State.NORMAL;
    }
    public Human(String name, Gender gender, String job) {
        super(name);
        this.gender = gender;
        this.state = State.NORMAL;
        this.job = job;
    }

    private class Phrase{
        String phrase;
        String verb = "сказал";
        Essence companion = null;
        public Phrase(String phrase){
            this.phrase = phrase;
        }
        public Phrase(String phrase, String verb){
            this.phrase = phrase;
            this.verb = verb;
        }
        public Phrase(String phrase, String verb, Essence companion){
            this.phrase = phrase;
            this.verb = verb;
            this.companion = companion;
        }
        public Phrase(String phrase, Essence companion){
            this.phrase = phrase;
            this.companion = companion;
        }
        public void say(){
            String verb = switch (Human.this.gender){
                case MALE -> this.verb;
                case FEMALE -> this.verb + "а";
                case UNKNOWN -> this.verb + "и";
            };
            if(this.companion == null){
                System.out.println(Human.this.getName() + " " + verb + ": " + this.phrase);
            }
            else{
                System.out.println(this.companion.getName() + ", " + verb + " " + Human.this.getName() + ", " + this.phrase);
            }
        }
    }
    public void say(String phrase, Human companion) {
        (new Human.Phrase(phrase, companion)).say();
    }
    public void shout(String phrase) {
        (new Human.Phrase(phrase, "закричал")).say();
    }
    public void order(String phrase, Human companion) {
        (new Human.Phrase(phrase,"приказал", companion)).say();
    }
    public void explain(String phrase) {
        (new Human.Phrase(phrase, "объяснил")).say();
    }
    public void answer(String phrase) {
        (new Human.Phrase(phrase, "ответил")).say();
    }

    public static class ClothesItem extends Thing {
        protected boolean weared = false;
        protected Human carrier = null;

        public ClothesItem(String name, String material, String color) {
            super(name, material, color);
        }

        public ClothesItem(String name, String material, String color, Human carrier) {
            super(name, material, color);
            if (carrier == null) {
                throw new NameError("Необходимо указать владельца для вещи " + name);
            }
            this.carrier = carrier;
            this.weared = true;
            this.carrier.addClothes(this);
        }

        public void wear(Human person) throws WearingException {
            if (this.weared) {
                throw new WearingException("Человек '" + person.getName() + "' пытается надеть вещь '" + this.getName() + "' которая уже надета человеком '" + this.carrier.getName() + "'!", this, person);
            }
            this.weared = true;
            this.carrier = person;
            this.carrier.addClothes(this);

            switch (carrier.getGender()) {
                case MALE -> System.out.println(carrier.getName() + " надел " + this.getName());
                case FEMALE -> System.out.println(carrier.getName() + " надела " + this.getName());
                case UNKNOWN -> System.out.println(carrier.getName() + " надели " + this.getName());
            }
        }

        public void unWear() throws WearingException {
            if (!this.weared) {
                throw new WearingException("Объект пытается снять вещь '" + this.getName() + "' которая не надета", this, this.carrier);
            }
            switch (carrier.getGender()) {
                case MALE -> System.out.println(carrier.getName() + " снял " + this.getName());
                case FEMALE -> System.out.println(carrier.getName() + " сняла " + this.getName());
                case UNKNOWN -> System.out.println(carrier.getName() + " сняли " + this.getName());
            }
            this.carrier.removeClothes(this);
            this.weared = false;
            this.carrier = null;
        }

        @Override
        public String toString() {
            return "ClothesItem{" +
                    "weared=" + weared +
                    ", carrier=" + carrier +
                    '}';
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            if (!super.equals(o)) return false;
            ClothesItem that = (ClothesItem) o;
            return weared == that.weared && Objects.equals(carrier, that.carrier);
        }

        @Override
        public int hashCode() {
            return Objects.hash(super.hashCode(), weared, carrier);
        }
    }

    @Override
    public State getState() {
        return this.state;
    }

    public Gender getGender() {
        return this.gender;
    }
    public String getJob(){
        return this.job;
    }
    @Override
    public void setState(State state, Essence obj) {
        this.state = state;
        System.out.println(this.getName() + " " + this.state.describe(this.gender));

        if(state == State.SCARED) this.completeAction(Action.BITE, obj);
    }

    @Override
    public void setState(State state) {
        this.state = state;
        System.out.println(this.getName() + " " + this.state.describe(this.gender));

        if(state == State.NERVOUS) this.completeAction(Action.SHIFT);
        if(state == State.WHITE) this.completeAction(Action.SQUIRM);
    }

    public void addClothes(Human.ClothesItem clothes){
        this.clothes.add(clothes);
    }
    public void removeClothes(Human.ClothesItem clothes){
        this.clothes.remove(clothes);
    }

    @Override
    public void completeAction(Action action, Essence var1) {
        action.applyEssenceAction(this, var1);
    }
    @Override
    public void completeAction(Action action) {
        action.applySelfAction(this);
        if(action == Action.SHAKE){
            ArrayList<MagicClothesItem> itemsToFly = new ArrayList<>();
            for(Human.ClothesItem item : this.clothes){
                if(item instanceof MagicClothesItem) {
                    itemsToFly.add((MagicClothesItem) item);
                }
            }

            for(MagicClothesItem item : itemsToFly){
                item.fly();
            }
        }
    }

    @Override
    public String toString() {
        return "lab4.classes.Human{" +
                "name=" + this.getName() +
                ", state=" + this.state +
                ", gender=" + this.gender +
                ", job=" + this.job +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Human human = (Human) o;
        return Objects.equals(this.state, human.state) && Objects.equals(this.gender, human.gender) && Objects.equals(this.job, human.job);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), state, gender, job);
    }
}
