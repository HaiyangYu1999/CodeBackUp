import java.util.*;
public class LinkedQueue<Item> implements Iterable<Item>
{
    private Node first;
    private Node last;
    private int N;

    private class Node
    {
        Item item;
        Node next;
    }

    public LinkedQueue()
    {
        this.first=null;
        this.last=null;
        this.N=0;
    }

    public boolean isEmpty()
    {
        return N==0;
    }

    public int size()
    {
        return N;
    }

    public void enqueue(Item item)
    {
        Node oldlast=last;
        last = new Node();
        last.item=item;
        last.next=null;
        if(this.isEmpty())
        {
            first=last;
        }
        else
        {
            oldlast.next=last;
        }
        ++N;
    }

    public Item dequeue()
    {
        Item s = first.item;
        first=first.next;
        --N;
        if(this.isEmpty())
            last=null;
        return s;
    }
    public Iterator<Item> iterator()
    {
        return new LinkedQueueIterator();
    }
    private class LinkedQueueIterator implements Iterator<Item>
    {
        Node current =first;
        public Item next()
        {
            Item s=current.item;
            current=current.next;
            return s;
        }
        public boolean hasNext()
        {
            return current!=null;
        }

        public void remove()
        {

        }
    }
    public static void main(String[] args)
    {
        LinkedQueue<Integer> a= new LinkedQueue<Integer>();
        Scanner in = new Scanner(System.in);
        while(in.hasNextInt())
        {
            int d=in.nextInt();
            a.enqueue(d);
        }
        for(int s :a)
        {
            System.out.println(s);
        }
    }
}
