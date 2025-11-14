package lab3.enums;

import lab3.interfaces.Describable;

public enum State implements Describable {
    NERVOUS{
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case MALE -> "взволнован";
                case FEMALE -> "взволнована";
            };
        }
        @Override
        public String toString() {
            return "lab3.enums.Action{NERVOUS}";
        }
    },
    NORMAL{
        @Override
        public String describe(Gender gender) {
            return "чувствует себя номально";
        }
        @Override
        public String toString() {
            return "lab3.enums.Action{NORMAL}";
        }
    },
    SCARED{
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case MALE -> "испуган";
                case FEMALE -> "испугана";
            };
        }
        @Override
        public String toString() {
            return "lab3.enums.Action{SCARED}";
        }
    };
}
