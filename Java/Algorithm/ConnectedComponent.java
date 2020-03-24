public class ConnectedComponent
{
    private boolean[] marked;
    private int[] id;
    private int count=0;

    public ConnectedComponent(Graph G)
    {
        marked=new boolean[G.V()];
        id=new int[G.V()];
        for(int s=0;s<G.V();++s)
        {
            if(!marked[s])
            {
                dfs(G,s);
                ++count;
            }
        }
    }

    private void dfs(Graph G,int v)
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

    public boolean connected(int v,int w)
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
        Graph G= new Graph(4);
        G.addEdge(0,1);
        G.addEdge(2,3);
        ConnectedComponent cc=new ConnectedComponent(G);
        System.out.println(cc.count());
        System.out.println(cc.connected(1,2));
    }
}
