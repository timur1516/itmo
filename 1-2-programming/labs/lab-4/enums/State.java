package lab4.enums;

import lab4.interfaces.Describable;

public enum State implements Describable {
    NERVOUS{
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case MALE -> "взволнован";
                case FEMALE -> "взволнована";
                case UNKNOWN -> "взволнованы";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{NERVOUS}";
        }
    },
    NORMAL{
        @Override
        public String describe(Gender gender) {
            return switch (gender) {
                case UNKNOWN -> "чувствуют себя нормально";
                default -> "чувстсвует себя нормально";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{NORMAL}";
        }
    },
    SCARED{
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case MALE -> "испуган";
                case FEMALE -> "испугана";
                case UNKNOWN -> "испуганы";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{SCARED}";
        }
    },
    WHITE{
        @Override
        public String describe(Gender gender) {
            return switch (gender){
                case MALE -> "побледнел";
                case FEMALE -> "побледнела";
                case UNKNOWN -> "побледнели";
            };
        }
        @Override
        public String toString() {
            return "lab4.enums.Action{WHITE}";
        }
    }
}
