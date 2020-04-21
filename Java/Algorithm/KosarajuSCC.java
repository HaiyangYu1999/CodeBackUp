public class KosarajuSCC
{
    private boolean[] marked;
    private int[] id;
    private int count=0;

    public KosarajuSCC(Digraph G)
    {
        marked=new boolean[G.V()];
        id=new int[G.V()];
        DepthFirstOrder order=new DepthFirstOrder(G.reverse());
        for(int s:order.reversePost())
        {
            if(!marked[s])
            {
                dfs(G,s);
                ++count;
            }
        }
    }

    private void dfs(Digraph G,int v)
    {
        marked[v]=true;
        id[v]=count;
        for(int w:G.adj(v))
        {
            if(!marked[w])
            {
                dfs(G,w);
            }
        }
    }

    public boolean stronglyConnected(int v,int w)
    {
        return id[v]==id[w];
    }

    public int id(int v)
    {
        return id[v];
    }

    public int count()
    {
        return count;
    }

    public static void main(String[] args)
    {
        Digraph G= new Digraph(4);
        G.addEdge(0,1);
        G.addEdge(2,3);
        KosarajuSCC cc=new KosarajuSCC(G);
        System.out.println(cc.count());
        System.out.println(cc.stronglyConnected(1,2));
    }
}

