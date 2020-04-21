import java.util.*;
public class LinkedDeque<Item> implements Iterable<Item>
{
    private Node first;
    private Node last;
    private int N=0;
    private class Node
    {
        Item item;
        Node previous;
        Node next;
    }

    public boolean isEmpty()
    {
        return N==0;
    }

    public int size()
    {
        return N;
    }

    public void pushleft(Item item)
    {
        Node T=new Node();
        T.item=item;
        T.next=first;
        T.previous=null;
        //first.previous=T;
        //first=T;
        if(T.next==null)
        {
            last=T;
            first=T;
        }
        else
        {
            first.previous=T;
            first=T;
        }

        ++N;
    }

    public Item popleft()
    {
        Item s = first.item;
        first=first.next;
        if (first==null)
        {
            last=null;
        }
        else
        {
            first.previous=null;
        }
        --N;
        return s;
    }

    public void pushright(Item item)
    {
        Node T=new Node();
        T.item=item;
        T.next=null;
        T.previous=last;
        if (T.previous==null)
        {
            last=T;
            first=T;
        }
        else
        {
            last.next=T;
            last=T;
        }
        ++N;
    }

    public Item popright()
    {
        Item s=last.item;
        if(last.previous==null)
        {
            last=null;
            first=null;
        }
        else
        {
            last=last.previous;
            last.next=null;
        }
        return s;
    }

    public Iterator<Item> iterator()
    {
        return new LinkedDequeIterator();
    }

    private class LinkedDequeIterator implements Iterator<Item>
    {
        Node current=first;
        public boolean hasNext()
        {
            return current!=null;
        }

        public Item next()
        {
            Item s = current.item;
            current=current.next;
            return s;
        }
    }

    public static void main(String[] args)
    {
        LinkedDeque<Integer> a = new LinkedDeque<Integer>();
        for(int i=0;i<15;++i)
        {
            a.pushright(i);
        }
        for(int i=0;i<15;++i)
        {
            System.out.println(a.popright());
        }
    }
}
