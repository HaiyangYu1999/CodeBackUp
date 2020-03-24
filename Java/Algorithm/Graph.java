public class Graph
{
    private final int V;
    private int E;
    private LinkedBag<Integer>[] adj;
    public Graph(int V)
    {
        this.V=V;
        this.E=0;
        adj= (LinkedBag<Integer>[]) new LinkedBag[V];
        for(int v=0;v<V;++v)
        {
            adj[v]=new LinkedBag<>();
        }
    }

    public int V()
    {
        return this.V;
    }

    public int E()
    {
        return this.E;
    }

    public void addEdge(int v,int w)
    {
        adj[v].add(w);
        adj[w].add(v);
        ++E;
    }

    public Iterable<Integer> adj(int v)
    {
        return adj[v];
    }

    public String toString()
    {
        String s=V+" vertices, "+E+"edges\n";
        for(int v=0;v<V;++v)
        {
            s+=v+": ";
            for(int w:adj(v))
            {
                s+=w+" ";
            }
            s+="\n";
        }
        return s;
    }
    public static void main(String[] args)
    {
        Graph a=new Graph(10);
        a.addEdge(1,2);
        a.addEdge(4,5);
        System.out.println(a.toString());
    }
}
