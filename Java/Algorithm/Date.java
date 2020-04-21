public class Date implements Comparable<Date>
{
    private int month;
    private int day;
    private int year;
    public Date(int month,int day,int year)
    {
        this.month=month;
        this.day=day;
        this.year=year;
    }
    @Override
    public int compareTo(Date that)
    {
        if(this.year<that.year)
        {
            return -1;
        }
        if(this.year>that.year)
        {
            return 1;
        }
        if (this.month<that.month)
        {
            return -1;
        }
        if(this.month>that.month)
        {
            return 1;
        }
        if (this.day<that.day)
        {
            return -1;
        }
        if(this.day>that.day)
        {
            return 1;
        }
        return 0;
    }

    @Override
    public String toString()
    {
        return this.year+"."+this.month+"."+this.day;
    }

    public static void main(String[] args)
    {
        Date[] a=new Date[12];
        for(int i=0;i<a.length;++i)
        {
            a[i]=new Date((int)(Math.random()*12+1),(int)(Math.random()*31+1),(int)(Math.random()*200+1900));
        }
        SelectionSort.show(a);
        SelectionSort.sort(a);
        SelectionSort.show(a);
    }
}
