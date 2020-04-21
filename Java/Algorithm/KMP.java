public class KMP
{
    private static int[] getNext(String p)
    {
        int[] next=new int[p.length()];
        next[0] = -1;

        int i = 0, j = -1;

        while (i != p.length() - 1)
        {
            if (j == -1 || p.charAt(i) == p.charAt(j))
            {
                ++i;
                ++j;
                next[i] = j;
            }
            else
            {
                j = next[j];
            }
        }
        return next;
    }

    public static int kmp(String txt,String pat)
    {
        int[] next=getNext(pat);

        int i = 0, j = 0;
        while(i != txt.length() && j != pat.length())
        {
            if (j == -1 || txt.charAt(i) == pat.charAt(j))
            {
                ++i;
                ++j;
            }
            else
            {
                j = next[j];
            }
        }

        return j == pat.length() ? i - j: -1;
    }

    public static void main(String[] args)
    {
        String pat="asd";
        String txt="asasasasasasasasdasd";
        System.out.println(KMP.kmp(txt,pat));
    }

}
