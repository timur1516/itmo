package lab4.enums;

import lab4.Exceptions.NoObjectForAction;
import lab4.classes.Essence;
import lab4.classes.Human;
import lab4.interfaces.Describable;

public enum Action implements Describable {
    BITE(true){
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case MALE -> "откусил кусок от";
                case FEMALE -> "откусила кусок от";
                case UNKNOWN -> "откусили кусок от";
            };
        }

        @Override
        public String toString() {
            return "lab4.enums.Action{BITE}";
        }
    },
    SHIFT(false){
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case UNKNOWN -> "переминаются с ноги на ногу";
                default -> "переминается с ноги на ногу";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{SHIFT}";
        }
    },
    SHAKE(false){
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case UNKNOWN -> "трясуться";
                default -> "трясётся";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{SHAKE}";
        }
    },
    STARE(true){
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case UNKNOWN -> "опасливо поглядывают на";
                default -> "опасливо поглядывает на";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{STARE}";
        }
    },
    GAZE(true){
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case UNKNOWN -> "пристально смотрят на";
                default -> "пристально смотрит на";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{GAZE}";
        }
        @Override
        public void applyEffect(Essence var1){
            Human smb;
            try{
                smb = (Human)var1;
            }catch (ClassCastException e){
                return;
            }
            smb.setState(State.WHITE);
        }
    },
    CHANGEPOS(false){
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case MALE -> "пересел";
                case FEMALE -> "пересела";
                case UNKNOWN -> "пересели";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{CHANGEPOS}";
        }
    },
    ROTATETO(true){
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case MALE -> "повернулся к";
                case FEMALE -> "повернулась к";
                case UNKNOWN -> "повернулись к";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{ROTATETO}";
        }
    },
    SQUIRM(false){
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case MALE -> "начал корчится как жук на булавке";
                case FEMALE -> "начала корчится как жук на булавке";
                case UNKNOWN -> "начали корчится как жук на булавке";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{SQUIRM}";
        }
    };
    private boolean isEssenceRequired;
    public void applyEffect(Essence var1){}
    private Action(boolean isEssenceRequired){
        this.isEssenceRequired = isEssenceRequired;
    }
    public void applySelfAction(Human var1){
        if(this.isEssenceRequired){
            throw new NoObjectForAction(var1, this);
        }
        System.out.println(var1.getName() + " " + this.describe(var1.getGender()));
    }
    public void applyEssenceAction(Human var1, Essence var2) {
        System.out.println(var1.getName() + " " + this.describe(var1.getGender()) + " " + var2.getName());
        this.applyEffect(var2);
    }
}