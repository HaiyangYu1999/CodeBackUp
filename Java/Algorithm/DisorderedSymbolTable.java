import java.util.Iterator;
public class DisorderedSymbolTable<Key,Value> implements Iterable<Key>
{
    private Node first;
    private int N;
    private class Node
    {
        Key key;
        Value val;
        Node next;
        public Node(Key key,Value val,Node next)
        {
            this.key=key;
            this.val=val;
            this.next=next;
        }
    }

    public Value get(Key key)
    {
        for(Node i=first;i!=null;i=i.next)
        {
            if(i.key.equals(key))
            {
                return i.val;
            }
        }
        return null;
    }

    public void put(Key key,Value val)
    {
        if(val==null)
        {
            delete(key);
        }
        for(Node i=first;i!=null;i=i.next)
        {
            if(i.key==key)
            {
                i.val=val;
                return;
            }
        }
        first=new Node(key,val,first);
        ++N;
    }

    public void delete(Key key)
    {
        if(first.key.equals(key))
        {
            first=first.next;
            --N;
            return;
        }
        Node i=first.next;
        Node previous=first;
        while(i!=null)
        {
            if(i.key.equals(key))
            {
                previous.next=previous.next.next;
                --N;
                return;
            }
            previous=i;
            i=i.next;
        }
    }

    public boolean contains(Key key)
    {
        return get(key)!=null;
    }

    public boolean isEmpty()
    {
        return N==0;
    }

    public int size()
    {
        return N;
    }

    @Override
    public Iterator<Key> iterator()
    {
        return new DisorderedSymbolTableIterator();
    }

    private class DisorderedSymbolTableIterator implements Iterator<Key> {
        Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public Key next()
        {
            Key s=current.key;
            current=current.next;
            return s;
        }
        public void remove()
        {

        }
    }


    public static void main(String[] args)
    {
        DisorderedSymbolTable<String,Integer> a = new DisorderedSymbolTable<>();
        for(int i=0;i<20;++i)
        {
            a.put(i+"",i*i);
        }
        a.put("01",1);
        a.delete("01");
        a.delete("12");
        a.delete("19");
        for(String i:a)
            System.out.println(i);
    }
}
