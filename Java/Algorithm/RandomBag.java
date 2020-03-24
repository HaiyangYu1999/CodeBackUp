import java.util.*;
public class RandomBag<Item>implements Iterable<Item>
{
    private Item[] a;
    private int N=0;

    public RandomBag()
    {
        a=(Item[]) new Object[1];

    }

    public void add(Item item)
    {
        if(this.size()==a.length)
        {
            resize(2*a.length);
        }
        a[N++]=item;
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
        RandomBag<String> a =new RandomBag<String>();
        a.add("Hello");
        a.add("world!");
        a.add("3");
        a.add("4");
        a.add("I'm");
        a.add("X");
        for(String s:a)
        {
            System.out.println(s);
        }
    }
}
