public class Digraph
{
    private final int V;
    private int E;
    private LinkedBag<Integer>[] adj;
    public Digraph(int V)
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
        ++E;
    }
    public Iterable<Integer> adj(int v)
    {
        return adj[v];
    }

    public Digraph reverse()
    {
        Digraph R=new Digraph(V);
        for(int v=0;v<V;++v)
        {
            for(int w:adj(v))
            {
                R.addEdge(w,v);
            }
        }
        return R;
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
        Digraph a=new Digraph(5);
        a.addEdge(3,4);
        a.addEdge(4,0);
        System.out.println(a.toString());
    }
}
