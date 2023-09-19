package Composite;

import Component.Component;

import java.util.ArrayList;
import java.util.List;

public class Composite extends Component {
    private List<Component> children = new ArrayList<>();

    @Override //simula a substituicao de um metodo
    public void add(Component component) {
        children.add(component);
        component.setParent(this);
    }

    @Override
    public void remove(Component component) {
        children.remove(component);
        component.setParent(null);
    }

    @Override
    public boolean isComposite() {
        return true;
    }

    @Override
    public String operation() {
        List<String> results = new ArrayList<>();
        for (Component child : children) {
            results.add(child.operation());
        }
        return "Branch(" + String.join("+", results) + ")";
    }
}