import java.util.PriorityQueue;

public class HeapSort
{
    public static void sort(Comparable[] a)
    {
        PriorityQueue<Comparable> b = new PriorityQueue<>();
        for(Comparable i:a)
        {
            b.add(i);
        }

        for(int i=0;i<a.length;++i)
        {
            a[i]=b.poll();
        }
    }

    public static void show(Comparable[] a)
    {
        for(int i=0;i<a.length;++i)
        {
            System.out.print(a[i]+" ");
        }
        System.out.println();
    }

    public static void main(String[] args)
    {
        Integer[] a=new Integer[27];
        for(int i=0;i<a.length;++i)
        {
            a[i]=(int)(Math.random()*100);
        }
        HeapSort.show(a);
        HeapSort.sort(a);
        HeapSort.show(a);
    }
}
