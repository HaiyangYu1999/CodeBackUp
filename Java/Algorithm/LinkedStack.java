import java.util.*;
public class LinkedStack<Item> implements Iterable<Item>
{
    private class Node
    {
        Item item;
        Node next;
    }
    private Node first;
    private int N;

    public LinkedStack()
    {
        N=0;
        first=null;
    }

    public boolean isEmpty()
    {
        return N==0;
    }

    public int size()
    {
        return N;
    }

    public void push(Item item)
    {
        Node oldfirst=first;
        first=new Node();
        first.item=item;
        first.next=oldfirst;
        ++N;
    }

    public Item pop()
    {
        Item s= first.item;
        first=first.next;
        --N;
        return s;
    }

    public Iterator<Item> iterator()
    {
        return new LinkedStackIterator();
    }

    private class LinkedStackIterator implements Iterator<Item>
    {
        private Node current=first;
        public boolean hasNext()
        {
            return current!=null;
        }

        public Item next()
        {
            Item temp=current.item;
            current=current.next;
            return temp;
        }
        public void remove()
        {

        }
    }
    public static void main(String[] args)
    {
        LinkedStack<String> a =new LinkedStack<String>();
        a.push("Hello");
        a.push("world!");
        a.push("3");
        a.push("4");
        a.pop();
        a.pop();
        a.push("I'm");
        a.push("X");

        for(String s :a)
        {
            System.out.println(s);
        }
    }
}
