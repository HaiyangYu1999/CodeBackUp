import java.util.Iterator;

public class LinearProbingHashST<Key,Value>
{
    private int N;
    private int M=16;
    private Key[] keys;
    private Value[] vals;
    public LinearProbingHashST()
    {
        keys=(Key[])new Object[M];
        vals=(Value[])new Object[M];
    }
    public LinearProbingHashST(int M)
    {
        keys=(Key[])new Object[M];
        vals=(Value[])new Object[M];
        this.M=M;
    }
    private int hash(Key key)
    {
        return (key.hashCode()&0x7fffffff)%M;
    }
    public int getsize()
    {
        return N;
    }
    private void resize(int cap)
    {
        LinearProbingHashST<Key,Value> t;
        t=new LinearProbingHashST<Key,Value>(cap);
        for(int i=0;i<M;++i)
        {
            if(keys[i]!=null)
                t.put(keys[i],vals[i]);
        }
        keys=t.keys;
        vals=t.vals;
        M=t.M;
    }
    public void put(Key key,Value val)
    {
        if(N>=M/2)
            resize(2*M);
        int i;
        for(i=hash(key);keys[i]!=null;i=(i+1)%M)
        {
            if(keys[i].equals(key))
            {
                vals[i]=val;
                return;
            }
        }
        keys[i]=key;
        vals[i]=val;
        ++N;
    }
    public Value get(Key key)
    {
        for(int i=hash(key);keys[i]!=null;i=(i+1)%M)
        {
            if(keys[i].equals(key))
            {
                return vals[i];
            }
        }
        return null;
    }
    public boolean contains(Key key)
    {
        for(int i=hash(key);keys[i]!=null;i=(i+1)%M)
        {
            if(keys[i].equals(key))
            {
                return true;
            }
        }
        return false;
    }
    public void delete(Key key)
    {
        if(!contains(key))
            return;
        int i=hash(key);
        while(!key.equals(keys[i]))
            i=(i+1)%M;
        keys[i]=null;
        vals[i]=null;
        i=(i+1)%M;
        while(keys[i]!=null)
        {
            Key keyRedo=keys[i];
            Value valRedo=vals[i];
            keys[i]=null;
            vals[i]=null;
            --N;
            put(keyRedo,valRedo);
            i=(i+1)%M;
        }
        --N;
        if(N>0&&N==M/8)
            resize(M/2);
    }
    public Iterable<Key> keys()
    {
        LinkedQueue<Key> q=new LinkedQueue<Key>();
        for(int i=0;i<M;++i)
        {
            if(keys[i]!=null)
                q.enqueue(keys[i]);
        }
        return q;
    }
    public static void main(String[] args)
    {
        LinearProbingHashST<Double,Integer> a = new LinearProbingHashST<>();
        for(double i=0.0;i<21;++i)
        {
            a.put(-i,(int)(i*i));
        }
        a.delete(2.0);
        Iterable<Double> q=a.keys();
        for(double i:q)
            System.out.println(i);
    }
}
