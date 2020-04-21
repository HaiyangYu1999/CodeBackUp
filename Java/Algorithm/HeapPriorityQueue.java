public class HeapPriorityQueue<Key extends Comparable<Key>>
{
    private Key[] a;
    private int N;

    public HeapPriorityQueue()
    {
        a=(Key[])new Comparable[1];
        N=0;
    }

    public HeapPriorityQueue(Key[] a)
    {
        this();
        for(Key i:a)
        {
            insert(i);
        }
    }

    private boolean less(int p,int q)
    {
        return a[p].compareTo(a[q])<0;
    }

    private void exch(int p,int q)
    {
        Key temp=a[q];
        a[q]=a[p];
        a[p]=temp;
    }

    private void swim(int k)
    {
        while(k>1 && a[k/2].compareTo(a[k])<0)
        {
            exch(k/2,k);
            k=k/2;
        }
    }

    private void sink(int k)
    {
        while(2*k<=N)
        {
            int j=2*k;
            if(j<N&&less(j,j+1))
            {
                ++j;
            }
            if(!less(k,j))
                break;
            exch(k,j);
            k=j;
        }
    }

    public boolean isEmpty()
    {
        return N==0;
    }
    public int size()
    {
        return N;
    }
    public void insert(Key v)
    {
        if(N==a.length-1)
        {
            resize(2*a.length);
        }
        a[++N]=v;
        swim(N);
    }

    public Key delMax()
    {
        Key max=a[1];
        exch(1,N--);
        a[N+1]=null;
        sink(1);
        if(N==a.length/4)
        {
            resize(a.length/2);
        }
        return max;
    }

    public Key max()
    {
        return a[1];
    }

    private void resize(int m)
    {
        Key[] temp = (Key[]) new Comparable[m];
        for (int i = 0; i < N+1; ++i) {
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
        HeapPriorityQueue<Integer> b=new HeapPriorityQueue<>(a);
        System.out.println(b.delMax());
        System.out.println(b.delMax());
        System.out.println(b.delMax());

    }
}
