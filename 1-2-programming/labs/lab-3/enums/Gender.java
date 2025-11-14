package lab3.enums;

public enum Gender {
    MALE{
        @Override
        public String toString() {
            return "Gender{MALE}";
        }
    },
    FEMALE{
        @Override
        public String toString() {
            return "Gender{FEMALE}";
        }
    };
}
