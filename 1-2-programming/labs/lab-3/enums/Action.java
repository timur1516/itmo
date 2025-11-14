package lab3.enums;

import lab3.interfaces.Describable;
import lab3.classes.*;

public enum Action implements Describable {
    BITE{
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case MALE -> "откусил кусок от";
                case FEMALE -> "откусила кусок от";
            };
        }

        @Override
        public String toString() {
            return "lab3.enums.Action{BITE}";
        }
    },
    SHIFT{
        @Override
        public String describe(Gender gender) {
            return "переминается с ноги на ногу";
        }
        @Override
        public String toString() {
            return "lab3.enums.Action{SHIFT}";
        }
    },
    STARE{
        @Override
        public String describe(Gender gender) {
            return "опасливо поглядывает на";
        }
        @Override
        public String toString() {
            return "lab3.enums.Action{STARE}";
        }
    };
    public String applySelfAction(Human var1) {
        return var1.getName() + " " + this.describe(var1.getGender());
    }
    public String applyEssenceAction(Human var1, Essence var2) {
        return var1.getName() + " " + this.describe(var1.getGender()) + " " + var2.getName();
    }
}
