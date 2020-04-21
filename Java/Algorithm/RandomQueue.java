import java.util.*;
public class RandomQueue<Item> implements Iterable<Item>
{
    private Item[] a;
    private int N=0;

    public RandomQueue()
    {
        a=(Item[]) new Object[1];

    }

    public void enqueue(Item item)
    {
        if(this.size()==a.length)
        {
            resize(2*a.length);
        }
        a[N++]=item;
    }

    public Item dequeue()
    {
        int x =(int)(Math.random()*N);
        Item temp=a[x];
        a[x]=a[N-1];
        a[N-1]=null;
        --N;
        if(this.size()==a.length/4)
        {
            resize(a.length/2);
        }
        return temp;
    }
    private void resize(int m)
    {
        Item[] temp =(Item[]) new Object[m];
        for(int i=0;i<N;++i)
        {
            temp[i]=a[i];
        }
        a=temp;
    }

    public boolean isEmpty()
    {
        return N==0;
    }

    public int size()
    {
        return N;
    }

    public int getlength()
    {
        return a.length;
    }

    @Override
    public Iterator<Item> iterator() {
        return new randomiterator();
    }
    private class randomiterator implements Iterator<Item>
    {
        private int i=N;
        private int[] f=RandomShuffle.shuffle(N);
        public boolean hasNext()
        {
            return i>0;
        }
        public Item next()
        {
            return a[f[--i]];
        }
        public void remove()
        {

        }
    }
    public static void main(String args[])
    {
        RandomQueue<Integer> a =new RandomQueue<Integer>();
        for(int i=0;i<20;++i)
        {
            a.enqueue(i);
        }
        for(int i=0;i<20;++i)
        {
            int s =a.dequeue();
            System.out.println(s);
        }
    }
}

