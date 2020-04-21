public class QuickSort
{
    public static void sort(Comparable[] a)
    {
        RandomShuffle.shuffle(a);
        sort(a,0,a.length-1);
    }

    private static void sort(Comparable[] a,int lo,int hi)
    {
        if(hi<=lo)
        {
            return;
        }
        int j=partition(a,lo,hi);
        sort(a,lo,j-1);
        sort(a,j+1,hi);
    }

    private static int partition(Comparable[] a,int lo,int hi)
    {
        int i=lo;
        int j=hi+1;
        Comparable v=a[lo];
        while(true)
        {
            while(less(a[++i],v))
            {
                if(i>=hi)
                    break;
            }
            while(less(v,a[--j]))
            {
                if(j<=lo)
                    break;
            }
            if(i>=j)
                break;
            exch(a,i,j);
        }
        exch(a,lo,j);
        return j;
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
    public static void main(String[] args)
    {
        Integer[] a=new Integer[20];
        for(int i=0;i<a.length;++i)
        {
            a[i]=(int)(Math.random()*100);
        }
        QuickSort.show(a);
        QuickSort.sort(a);
        QuickSort.show(a);
    }
}
