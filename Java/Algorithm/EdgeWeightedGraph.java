public class EdgeWeightedGraph
{
    private final int V;
    private int E;
    private LinkedBag<Edge>[] adj;
    public EdgeWeightedGraph(int V)
    {
        this.V=V;
        this.E=0;
        adj=(LinkedBag<Edge>[]) new LinkedBag[V];
        for(int i=0;i<V;++i)
        {
            adj[i]=new LinkedBag<>();
        }
    }
    public int V()
    {
        return V;
    }
    public int E()
    {
        return E;
    }
    public void addEdge(Edge e)
    {
        int v=e.either(),w=e.other(v);
        adj[v].add(e);
        adj[w].add(e);
        ++E;
    }
    public Iterable<Edge> adj(int v)
    {
        return adj[v];
    }
    public Iterable<Edge> edges()
    {
        LinkedBag<Edge> b=new LinkedBag<>();
        for(int i=0;i<V;++i)
        {
            for(Edge e:adj[i])
            {
                if(e.other(i)>i)
                    b.add(e);
            }
        }
        return b;
    }
    public String toString()
    {
        String s=V+" vertices, "+E+"edges\n";
        for(int v=0;v<V;++v)
        {
            s+=v+": ";
            for(Edge w:adj(v))
            {
                s+=w+" ";
            }
            s+="\n";
        }
        return s;
    }

    public static void main(String[] args)
    {
        EdgeWeightedGraph G=new EdgeWeightedGraph(5);
        G.addEdge(new Edge(3,4,1));
        G.addEdge(new Edge(4,0,1));
        System.out.println(G+"");
    }
}
