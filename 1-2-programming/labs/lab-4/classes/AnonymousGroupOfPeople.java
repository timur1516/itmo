package lab4.classes;
import lab4.enums.Gender;
import lab4.interfaces.Writeable;

public class AnonymousGroupOfPeople extends Human implements Writeable {
    public AnonymousGroupOfPeople(String name, String job) {
        super(name, Gender.UNKNOWN, job);
    }

    @Override
    public Object write(String info, String font) {
        class Script {
            private String info;
            private String font;

            Script(String info, String font) {
                this.info = info;
                this.font = font;
            }

            @Override
            public String toString() {
                return "Script{" +
                        "info='" + info + '\'' +
                        ", font='" + font + '\'' +
                        '}';
            }
        }
        System.out.println(this.getName() + " записывают.");

        Script script = new Script(info, font);
        return script;
    }

    @Override
    public String toString() {
        return super.toString();
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }

    @Override
    public boolean equals(Object o) {
        return super.equals(o);
    }
}
