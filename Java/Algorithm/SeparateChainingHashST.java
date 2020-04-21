import java.util.Iterator;

public class SeparateChainingHashST<Key,Value>
{
    private int M;
    private int N;
    private DisorderedSymbolTable<Key,Value> st[];
    public SeparateChainingHashST()
    {
        this(997);
    }
    public SeparateChainingHashST(int M)
    {
        this.M=M;
        st=(DisorderedSymbolTable<Key, Value>[]) new DisorderedSymbolTable[M];
        for(int i=0;i<M;++i)
        {
            st[i]=new DisorderedSymbolTable<>();
        }
    }
    private int hash(Key key)
    {
        return (key.hashCode()&0x7fffffff)%M;
    }
    private Value get(Key key)
    {
        return st[hash(key)].get(key);
    }
    public void put(Key key,Value val)
    {
        st[hash(key)].put(key,val);
        N=0;
        for(int i=0;i<M;++i)
        {
            N=N+st[i].size();
        }
    }
    public void delete(Key key)
    {
        st[hash(key)].delete(key);
        N=0;
        for(int i=0;i<M;++i)
        {
            N=N+st[i].size();
        }
    }
    public Iterable<Key> keys()
    {
        LinkedQueue<Key> q=new LinkedQueue<Key>();
        for(int i=0;i<M;++i)
        {
            for(Key s:st[i])
            {
                q.enqueue(s);
            }
        }
        return q;
    }
    public int getsize()
    {
        return N;
    }
    public static void main(String[] args)
    {
        SeparateChainingHashST<Double,Integer> a = new SeparateChainingHashST<>();
        for(int i=0;i<21;++i)
        {
            a.put((double)i,i*i);
            System.out.println(a.getsize());
        }
        a.delete(20.0);
        a.delete(19.0);
        Iterable<Double> q = a.keys();
        for(double i:q)
        {
            System.out.println(i);
        }
        System.out.println(a.getsize());
    }
}
