public class DirectedDFS
{
    private boolean[] marked;
    public DirectedDFS(Digraph G,int s)
    {
        marked=new boolean[G.V()];
        dfs(G,s);
    }

    public DirectedDFS(Digraph G,Iterable<Integer> sources)
    {
        marked=new boolean[G.V()];
        for(int w:sources)
        {
            if(!marked[w])
                dfs(G,w);
        }
    }

    private void dfs(Digraph G,int s)
    {
        marked[s]=true;
        for(int w:G.adj(s))
        {
            if(!marked[w])
                dfs(G,w);
        }
    }
    public boolean marked(int v)
    {
        return marked[v];
    }

    public static void main(String[] args)
    {
        Digraph G=new Digraph(3);
        G.addEdge(1,2);
        DirectedDFS a=new DirectedDFS(G,1);
        boolean i=a.marked(2);
        System.out.println(i);
    }
}
