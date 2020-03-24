import java.util.Stack;

public class DepthFirstDirectedPaths
{
    private boolean[] marked;
    private int[] edgeTo;
    private final int s;

    public DepthFirstDirectedPaths(Digraph G,int s)
    {
        marked=new boolean[G.V()];
        edgeTo=new int[G.V()];
        this.s=s;
        dfs(G,s);
    }

    private void dfs(Digraph G,int v)
    {
        marked[v]=true;
        for(int w:G.adj(v))
        {
            if(!marked[w])
            {
                edgeTo[w]=v;
                dfs(G,w);
            }
        }
    }

    public boolean hasPathTo(int v)
    {
        return marked[v];
    }

    public Iterable<Integer> pathTo(int v)
    {
        if(!hasPathTo(v)) return null;
        Stack<Integer> path=new Stack<>();
        for(int x=v;x!=s;x=edgeTo[x])
        {
            path.push(x);
        }
        path.push(s);
        return path;
    }

    public static void main(String args[])
    {
        Digraph G=new Digraph(6);
        G.addEdge(1,2);
        G.addEdge(2,3);
        G.addEdge(3,4);
        G.addEdge(4,5);
        DepthFirstDirectedPaths path1=new DepthFirstDirectedPaths(G,1);
        if(path1.hasPathTo(5))
        {
            Iterable<Integer> a = path1.pathTo(5);
            for (int w : a) {
                System.out.println(w);
            }
        }
    }
}
