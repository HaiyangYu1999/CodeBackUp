public class MergeSort
{
    private static Comparable[] aux;

    public static void sort(Comparable[] a)
    {
        aux= new Comparable[a.length];
        sort(a,0,a.length-1);
    }

    private static void sort(Comparable[] a,int lo,int hi)
    {
        if(lo>=hi)
        {
            return;
        }
        int mid =lo+(hi-lo)/2;
        sort(a,lo,mid);
        sort(a,mid+1,hi);
        merge(a,lo,mid,hi);
    }

    private static void merge(Comparable[] a,int lo,int mid,int hi)
    {
        int i=lo;
        int j=mid+1;
        for(int s=lo;s<hi+1;++s)
        {
            aux[s]=a[s];
        }
        for(int k=i;k<j;++k)
        {
            if(i>mid)
            {
                a[k]=aux[j++];
            }
            else if(j>hi)
            {
                a[k]=aux[i++];
            }
            else if(less(aux[j],aux[i]))
            {
                a[k]=aux[j++];
            }
            else
            {
                a[k]=aux[i++];
            }
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
        MergeSort.show(a);
        MergeSort.sort(a);
        MergeSort.show(a);
    }
}
