package Component;

public abstract class Component {
    private Component parent;

    public Component getParent() {
        return parent;
    }

    public void setParent(Component parent) {
        this.parent = parent;
    }

    public void add(Component component) {
    }

    public void remove(Component component) {
    }

    public boolean isComposite() {
        return false;
    }

    public abstract String operation();
}
