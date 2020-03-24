import java.util.Stack;

public class BreadthFirstDirectedPaths
{
    private boolean[] marked;
    private int[] edgeTo;
    private final int s;

    BreadthFirstDirectedPaths(Digraph G,int s)
    {
        marked=new boolean[G.V()];
        edgeTo=new int[G.V()];
        this.s=s;
        bfs(G,s);
    }

    private void bfs(Digraph G,int s)
    {
        LinkedQueue<Integer> queue=new LinkedQueue<>();
        marked[s]=true;
        queue.enqueue(s);
        while(!queue.isEmpty())
        {
            int v=queue.dequeue();
            for(int w: G.adj(v))
            {
                if(!marked[w])
                {
                    edgeTo[w]=v;
                    marked[w]=true;
                    queue.enqueue(w);
                }
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

    public static void main(String[] args)
    {
        Digraph G=new Digraph(4);
        G.addEdge(0,1);
        G.addEdge(1,2);
        G.addEdge(2,3);
        G.addEdge(0,3);
        BreadthFirstDirectedPaths path2 =new BreadthFirstDirectedPaths(G,0);
        Iterable<Integer> a =path2.pathTo(3);
        for(int w:a)
        {
            System.out.println(w);
        }
    }
}
