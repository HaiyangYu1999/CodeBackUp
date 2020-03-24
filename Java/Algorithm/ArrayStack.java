import java.util.*;
public class ArrayStack<Item>implements Iterable<Item>
{
    private Item[] a;
    private int N=0;

    public ArrayStack()
    {
        a=(Item[]) new Object[1];
    }

    public void push(Item item)
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
    public Item pop()
    {
        Item s=a[--N];
        a[N]=null;
        if (N==a.length/4)
        {
            resize(a.length/2);
        }
        return s;
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
        return new reverseiterator();
    }
    private class reverseiterator implements Iterator<Item>
    {
        private int i=N;
        public boolean hasNext()
        {
            return i>0;
        }
        public Item next()
        {
            return a[--i];
        }
        public void remove()
        {

        }
    }
    public static void main(String args[])
    {
        ArrayStack<String> a =new ArrayStack<String>();
        a.push("Hello");
        a.push("world!");
        a.push("3");
        a.push("4");
        a.pop();
        a.pop();
        a.push("I'm");
        a.push("X");
        for(String s:a)
        {
            System.out.println(s);
        }
    }
}
