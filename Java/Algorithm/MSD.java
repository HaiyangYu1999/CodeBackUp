public class MSD
{
    private static int R=256;
    private static final int M=15;
    private static String[] aux;
    private static int charAt(String s,int d)
    {
        return (d<s.length()) ? s.charAt(d) : -1;
    }
    public static void sort(String[] a)
    {
        int N=a.length;
        aux=new String[N];
        sort(a,0,N-1,0);
    }
    private static void sort(String[] a,int lo,int hi,int d)
    {
        if(hi<lo+M)
        {
            InsertionSort.sort(a);
            return;
        }
        int[] count=new int[R+2];
        for(int i=lo;i<hi;++i)
        {
            count[charAt(a[i],d)+2]++;
        }
        for(int r=0;r<R+1;++r)
            count[r+1]+=count[r];
        for(int i=lo;i<hi;++i)
        {
            aux[count[charAt(a[i],d)+1]++]=a[i];
        }
        for(int i=lo;i<hi;++i)
        {
            a[i]=aux[i-lo];
        }
        for(int r=0;r<R;++r)
        {
            sort(a,lo+count[r],lo+count[r+1]-1,d+1);
        }
    }

    public static void main(String[] args)
    {
        String[] a={"she","sells","seashells","by","the","sea","shore","and","the","shells"
        ,"she","sells","are","surely","seashells"};
        MSD.sort(a);
        for(String i:a)
        {
            System.out.println(i);
        }
    }
}
