import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Topological
{
    private Iterable<Integer> order;
    public Topological(Digraph G)
    {
        DirectedCycle cyclefinder = new DirectedCycle(G);
        if(!cyclefinder.hasCycle())
        {
            DepthFirstOrder dfs=new DepthFirstOrder(G);
            order=dfs.post();
        }
    }
    public Iterable<Integer> order()
    {
        return order;
    }
    public boolean isDAG()
    {
        return order!=null;
    }

    public static void main(String[] args)
    {
        Digraph G=new Digraph(6);
        G.addEdge(0,1);
        G.addEdge(0,2);
        G.addEdge(0,3);
        G.addEdge(0,3);
        G.addEdge(2,1);
        G.addEdge(2,4);
        G.addEdge(3,4);
        G.addEdge(5,3);
        G.addEdge(5,4);
        Topological a=new Topological(G);
        Iterable<Integer> s=a.order();
        for(int w:s)
            System.out.println(w);
    }
}


class DepthFirstOrder
{
    private boolean[] marked;
    private LinkedQueue<Integer> pre;
    private LinkedQueue<Integer> post;
    private Stack<Integer> reversePost;
    public DepthFirstOrder(Digraph G)
    {
        G=G.reverse();
        pre=new LinkedQueue<>();
        post=new LinkedQueue<>();
        reversePost=new Stack<>();
        marked=new boolean[G.V()];
        for(int v=0;v<G.V();++v)
        {
            if(!marked[v])
                dfs(G,v);
        }
    }

    private void dfs(Digraph G,int v)
    {
        pre.enqueue(v);
        marked[v]=true;

        for(int w:G.adj(v))
        {
            if(!marked[w])
                dfs(G,w);
        }
        post.enqueue(v);
        reversePost.push(v);
    }
    public Iterable<Integer> pre()
    {
        return pre;
    }
    public Iterable<Integer> post()
    {
        return post;
    }
    public Iterable<Integer> reversePost()
    {
        return reversePost;
    }
}