import java.util.Stack;

public class DepthFirstPaths
{
    private boolean[] marked;
    private int[] edgeTo;
    private final int s;

    public DepthFirstPaths(Graph G,int s)
    {
        marked=new boolean[G.V()];
        edgeTo=new int[G.V()];
        this.s=s;
        dfs(G,s);
    }

    private void dfs(Graph G,int v)
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
        Graph G=new Graph(6);
        G.addEdge(1,2);
        G.addEdge(2,3);
        G.addEdge(3,4);
        G.addEdge(4,5);
        DepthFirstPaths path1=new DepthFirstPaths(G,5);
        if(path1.hasPathTo(1))
        {
            Iterable<Integer> a = path1.pathTo(1);
            for (int w : a) {
                System.out.println(w);
            }
        }
    }
}
