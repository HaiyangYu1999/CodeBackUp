public class RandomShuffle
{
    public static int[] shuffle(int n)
    {
        int[] a =new int[n];
        for(int i=0;i<a.length;++i)
        {
            a[i]=i;
        }
        for(int i=n-1;i>0;--i)
        {
            int x=(int)(Math.random()*(i+1));
            int temp=a[x];
            a[x]=a[i];
            a[i]=temp;
        }
        return a;
    }
    public static void shuffle(Comparable[] a)
    {
        int n=a.length;
        int[] aux=shuffle(n);
        Comparable[] b =new Comparable[n];
        for(int i=0;i<n;++i)
        {
            b[i]=a[aux[i]];
        }
        a=b;
    }


    public static void main(String[] args)
    {
        int[] a=RandomShuffle.shuffle(10);
        for(int i:a)
        {
            System.out.println(i);
        }
    }
}
