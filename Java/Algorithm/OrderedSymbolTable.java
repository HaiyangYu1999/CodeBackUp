import java.util.Iterator;
import java.util.Queue;

public class OrderedSymbolTable<Key extends Comparable<Key>, Value> implements Iterable<Key>
{
    private Key[] keys;
    private Value[] vals;
    private int N;
    public OrderedSymbolTable()
    {
        keys=(Key[])new Comparable[1];
        vals=(Value[])new Object[1];
        N=0;
    }
    public int size()
    {
        return N;
    }
    public boolean isEmpty()
    {
        return N==0;
    }

    public boolean contains(Key key)
    {
        int i=rank(key);
        return i<N&&key.compareTo(keys[i])==0;
    }

    private int rank(Key key)
    {
        int lo=0;
        int hi=N-1;
        while(lo<=hi)
        {
            int mid = lo+(hi-lo)/2;
            int cmp=key.compareTo(keys[mid]);
            if(cmp==0)
            {
                return mid;
            }
            else if(cmp>0)
            {
                lo=mid+1;
            }
            else
            {
                hi=mid-1;
            }
        }
        return lo;
    }
    public Value get(Key key)
    {
        int j=rank(key);
        if(j<N&&key.compareTo(keys[j])==0)
        {
            return vals[j];
        }
        else
        {
            return null;
        }
    }
    private void resize(int m)
    {
        Key[] temp =(Key[]) new Comparable[m];
        for(int i=0;i<N;++i)
        {
            temp[i]=keys[i];
        }
        keys=temp;
        Value[] tem =(Value[]) new Object[m];
        for(int i=0;i<N;++i)
        {
            tem[i]=vals[i];
        }
        vals=tem;
    }
    public void put(Key key,Value val)
    {
        if(val==null)
        {
            delete(key);
            return;
        }
        if(N==keys.length)
        {
            resize(2*keys.length);
        }
        int i=rank(key);
        if(i<N&&key.compareTo(keys[i])==0)
        {
            vals[i]=val;
        }
        else
        {
            for(int j=N;j>i;--j)
            {
                keys[j]=keys[j-1];
                vals[j]=vals[j-1];
            }
            keys[i]=key;
            vals[i]=val;
            ++N;
        }
    }
    public void delete(Key key)
    {
        int i=rank(key);
        if(i<N&&key.compareTo(keys[i])==0)
        {
            for(int j=i;j<N-1;++j)
            {
                keys[j]=keys[j+1];
                vals[j]=vals[j+1];
            }
            --N;
        }
        if(N<=keys.length/4)
        {
            resize(keys.length/2);
        }
    }
    public Key select(int k)
    {
        return keys[k];
    }

    public Key max()
    {
        return keys[N-1];
    }
    public Key min()
    {
        return keys[0];
    }

    public Key ceiling(Key key)
    {
        int i = rank(key);
        if(i==N)
            return null;
        return keys[i];
    }
    public Key floor(Key key)
    {
        int i =rank(key);
        if(i==0)
        {
            if(key.compareTo(keys[0])==0)
                return keys[0];
            else
                return null;
        }

        if(i==N)
            return keys[N-1];
        if(i<N&&key.compareTo(keys[i])==0)
            return keys[i];
        return keys[i-1];
    }
    public Iterator<Key> iterator()
    {
        return new OrderedSymbolTableIterator();
    }
    private class OrderedSymbolTableIterator implements Iterator<Key>
    {
        int size=N;
        public boolean hasNext()
        {
            return size!=0;
        }

        public Key next()
        {
            Key s=keys[size-1];
            --size;
            return s;
        }
        public void remove() {}
    }

    public Iterable<Key> keys(Key lo,Key hi)
    {
        LinkedQueue<Key> q=new LinkedQueue<Key>();
        for(int i=rank(lo);i<rank(hi);++i)
        {
            q.enqueue(keys[i]);
        }
        if(contains(hi))
            q.enqueue(keys[rank(hi)]);
        return q;
    }

    public Iterable<Key> keys()
    {
        LinkedQueue<Key> q=(LinkedQueue<Key>) keys(keys[0],keys[N-1]);
        return q;
    }

    public static void main(String[] args)
    {
        OrderedSymbolTable<Double,Integer> a = new OrderedSymbolTable<>();
        for(int i=0;i<21;++i)
        {
            a.put((double)i,i*i);
        }
        Iterable<Double> q = a.keys();
        for(double i:q)
        {
            System.out.println(i);
        }
    }
}
