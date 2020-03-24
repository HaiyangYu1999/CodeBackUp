import java.util.Stack;

public class DirectedCycle
{
    private boolean[] marked;
    private int[] edgeTo;
    private Stack<Integer> cycle;
    private boolean[] onStack;

    public DirectedCycle(Digraph G)
    {
        marked=new boolean[G.V()];
        edgeTo=new int[G.V()];
        onStack=new boolean[G.V()];
        for(int v=0;v<G.V();++v)
        {
            if(!marked[v])
                dfs(G,v);
        }
    }

    private void dfs(Digraph G,int v)
    {
        onStack[v]=true;
        marked[v]=true;
        for(int w:G.adj(v))
        {
            if(this.hasCycle())
                return;
            else if(!marked[w])
            {
                edgeTo[w]=v;
                dfs(G,w);
            }
            else if(onStack[w])
            {
                cycle=new Stack<>();
                for(int x=v;x!=w;x=edgeTo[x])
                {
                    cycle.push(x);
                }
                cycle.push(v);
                cycle.push(w);
            }
        }
        onStack[v]=false;
    }
    public boolean hasCycle()
    {
        return cycle!=null;
    }
    public Iterable<Integer> cycle()
    {
        return cycle;
    }

    public static void main(String[] args)
    {
        Digraph G=new Digraph(5);
        G.addEdge(0,1);
        G.addEdge(1,2);
        G.addEdge(2,3);
        G.addEdge(0,3);
        DirectedCycle a=new DirectedCycle(G);
        System.out.println(a.hasCycle());
    }
}
