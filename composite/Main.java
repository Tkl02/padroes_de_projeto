import Component.Component;
import Composite.Composite;
import Leaf.Leaf;

public class Main {
    public static void clientCode(Component component) {
        System.out.print("RESULT: " + component.operation());
    }


// para cria uma "box" usa-se → Composite tree = new Composite();
// para criar uma "folha" usa-se → Leaf leaf = new Leaf();



    public static void main(String[] args) {
        Composite tree = new Composite(); //criando arvore

        Composite branch1 = new Composite(); //criando galho a esquerda da arvore
        branch1.add(new Leaf());
        branch1.add(new Leaf());

        Composite branch2 = new Composite();// criando gralho centrall
        Composite branch3 = new Composite();// gralho a esquerda do central
        branch3.add(new Leaf());
        branch3.add(new Leaf());
        Composite branch4 = new Composite();// gralho a direita do central
        branch4.add(new Leaf());
        branch4.add(new Leaf());

        //jogando galhos no galho central
        branch2.add(branch3);
        branch2.add(branch4);

        Composite branch5 = new Composite();// criando galho a direita da arvore
        branch5.add(new Leaf());
        branch5.add(new Leaf());


        tree.add(branch1);
        tree.add(branch2);
        tree.add(branch3);

        System.out.println("Sistema de Arvore:");
        clientCode(tree);
        System.out.println("\n");


    }
}