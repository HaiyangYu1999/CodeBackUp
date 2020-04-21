public class Quick3string
{
    private static int charAt(String s,int d)
    {
        return (d<s.length()) ? s.charAt(d) : -1;
    }
    public static void sort(String[] a)
    {
        sort(a,0,a.length-1,0);
    }
    private static void exch(Comparable[] a,int i,int j)
    {
        Comparable temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }
    private static void sort(String[] a,int lo,int hi,int d)
    {
        if(hi<=lo)
            return;
        int lt=lo;
        int gt=hi;
        int v=charAt(a[lo],d);
        int i=lo+1;
        while(i<=gt)
        {
            int t=charAt(a[i],d);
            if(t<v)
            {
                exch(a,lt++,i++);
            }
            else if(t>v)
            {
                exch(a,i,gt--);
            }
            else
                i++;
        }
        sort(a,lo,lt-1,d);
        if(v>=0)
            sort(a,lt,gt,d+1);
        sort(a,gt+1,hi,d);
    }

    public static void main(String[] args)
    {
        String[] a={"she","sells","seashells","by","the","sea","shore","and","the","shells"
                ,"she","sells","are","surely","seashells"};
        Quick3string.sort(a);
        for(String i:a)
        {
            System.out.println(i);
        }
    }

}
