public class ArrayPriorityQueue <Key extends Comparable<Key>>
{
    private Key[] a;
    private int N;

    public ArrayPriorityQueue()
    {
        a=(Key[])new Comparable[1];
        N=0;
    }

    public ArrayPriorityQueue(Key[] b)
    {
        this();
        for(Key i:b)
        {
            this.insert(i);
        }
    }

    public int size()
    {
        return N;
    }

    public boolean isEmpty()
    {
        return N==0;
    }

    public void insert(Key v)
    {
        if(N==a.length)
        {
            resize(2*a.length);
        }
        a[N++]=v;
    }

    public Key max()
    {
        Key s=a[0];
        int j=0;
        for(int i=1;i<N;++i)
        {
            if (a[i].compareTo(s)>0)
            {
                s=a[i];
                j=i;
            }
        }
        return s;
    }

    private int maxId()
    {
        Key s=a[0];
        int j=0;
        for(int i=1;i<N;++i)
        {
            if (a[i].compareTo(s)>0)
            {
                s=a[i];
                j=i;
            }
        }
        return j;
    }

    public Key delMax()
    {
        int j=this.maxId();
        Key s=a[j];
        for(int i=j;i<=N-1;++i)
        {
            a[i]=a[i+1];
        }
        if(--N<a.length/4)
        {
            resize(a.length/2);
        }
        return s;
    }

    private void resize(int m)
    {
        Key[] temp = (Key[]) new Comparable[m];
        for (int i = 0; i < N; ++i) {
            temp[i] = a[i];
        }
        a = temp;
    }

    public static void main(String[] args)
    {
        Integer[] a=new Integer[27];
        for(int i=0;i<a.length;++i)
        {
            a[i]=(int)(Math.random()*100);
        }
        SelectionSort.show(a);
        SelectionSort.sort(a);
        SelectionSort.show(a);
        ArrayPriorityQueue<Integer> b=new ArrayPriorityQueue<>(a);
        System.out.println(b.delMax());

    }
}
