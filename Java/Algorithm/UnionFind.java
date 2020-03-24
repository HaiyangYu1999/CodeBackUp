public class UnionFind
{
    public static void main(String[] args)
    {
        UnionFindQUImproved a=new UnionFindQUImproved(10);
        a.union(1,2);
        a.union(2,3);
        a.union(1,7);
        a.union(5,4);
        a.union(3,8);
        a.union(9,0);
        System.out.println(a.connected(3,9));
        System.out.println(a.count());
    }
}

class UnionFindQF
{
    private int[] id;
    private int count;

    public UnionFindQF(int N)
    {
        id=new int[N];
        for(int i=0;i<N;++i)
        {
            id[i]=i;
        }
        count=N;
    }

    public int count()
    {
        return this.count;
    }

    private int find(int p)
    {
        return id[p];
    }

    public void union(int p, int q)
    {
        int pid = find(p);
        int qid = find(q);
        if (pid==qid)
        {
            return;
        }
        for(int i=0;i<id.length;++i)
        {
            if(id[i]==pid)
            {
                id[i]=qid;
            }
        }
        --count;
    }

    public boolean connected(int p,int q)
    {
        return (find(p)==find(q));
    }

}

class UnionFindQU
{
    private int[] id;
    private int count;

    public UnionFindQU(int N)
    {
        id=new int[N];
        for(int i=0;i<N;++i)
        {
            id[i]=i;
        }
        count=N;
    }

    public int count()
    {
        return this.count;
    }

    private int find(int p)
    {
        while(id[p]!=p)
        {
            p=id[p];
        }
        return p;
    }

    public void union(int p, int q)
    {
        int pid=find(p);
        int qid=find(q);
        if(pid==qid)
        {
            return;
        }
        id[qid]=pid;
        --count;
    }
    public boolean connected(int p,int q)
    {
        return (find(p)==find(q));
    }
}

class UnionFindQUImproved
{
    private int[] id;
    private int[] size;
    private int count;

    public UnionFindQUImproved(int N)
    {
        id=new int[N];
        size=new int[N];
        for(int i=0;i<N;++i)
        {
            id[i]=i;
            size[i]=1;
        }
        count=N;
    }

    public int count()
    {
        return this.count;
    }

    private int find(int p)
    {
        while(id[p]!=p)
        {
            p=id[p];
        }
        return p;
    }

    public void union(int p, int q)
    {
        int pid=find(p);
        int qid=find(q);
        if(pid==qid)
        {
            return;
        }
        if(size[pid]<size[qid])
        {
            id[pid]=qid;
            size[qid]+=size[pid];
        }
        else
        {
            id[qid]=pid;
            size[pid]+=size[qid];
        }
        --count;
    }
    public boolean connected(int p,int q)
    {
        return (find(p)==find(q));
    }
}