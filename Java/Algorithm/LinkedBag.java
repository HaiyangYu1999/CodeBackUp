import java.util.*;
public class LinkedBag<Item> implements Iterable<Item>
{
    private class Node
    {
        Item item;
        Node next;
    }
    private Node first;
    private int N;

    public LinkedBag()
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

    public void add(Item item)
    {
        Node oldfirst=first;
        first=new Node();
        first.item=item;
        first.next=oldfirst;
        ++N;
    }


    public Iterator<Item> iterator()
    {
        return new LinkedBagIterator();
    }

    private class LinkedBagIterator implements Iterator<Item>
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
        LinkedBag<String> a =new LinkedBag<String>();
        a.add("");
        a.add("w");
        a.add("3");
        a.add("4");
        a.add("");
        a.add("X");

        for(String s :a)
        {
            System.out.println(s);
        }
    }
}
