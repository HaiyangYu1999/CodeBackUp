public class ShellSort
{
    public static void sort(Comparable[] a)
    {
        int N=a.length;
        int h=1;
        while(h<N/3)
        {
            h=3*h+1;
        }
        while(h>1)
        {
            for(int i=h;i<N;++i)
            {
                for(int j=i;j>=h && less(a[j],a[j-h]);j=j-h)
                {
                    exch(a,j,j-h);
                }
            }
            h=h/3;
        }
    }

    private static boolean less(Comparable p,Comparable q)
    {
        return p.compareTo(q)<0;
    }

    private static void exch(Comparable[] a,int i,int j)
    {
        Comparable temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }

    public static void show(Comparable[] a)
    {
        for(Comparable i:a)
        {
            System.out.print(i+" ");
        }
        System.out.println();
    }

    public static boolean isSorted(Comparable[] a)
    {
        for(int i=0;i<a.length-1;++i)
        {
            if(less(a[i+1],a[i]))
            {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args)
    {
        Integer[] a=new Integer[20];
        for(int i=0;i<a.length;++i)
        {
            a[i]=(int)(Math.random()*100);
        }
        SelectionSort.show(a);
        SelectionSort.sort(a);
        SelectionSort.show(a);
    }
}
