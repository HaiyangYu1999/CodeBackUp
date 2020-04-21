import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class PrimMST
{
    private boolean[] marked;
    private Queue<Edge> mst;
    private PriorityQueue<Edge> pq;

    public PrimMST(EdgeWeightedGraph G)
    {
        pq=new PriorityQueue<>();
        marked=new boolean[G.V()];
        mst=new LinkedList<>();
        visit(G,0);
        while(!pq.isEmpty())
        {
            Edge e=pq.poll();
            int v=e.either(),w=e.other(v);
            if(marked[v]&&marked[w])
                continue;
            mst.offer(e);
            if(!marked[v]) visit(G,v);
            if(!marked[w]) visit(G,w);
        }
    }

    private void visit(EdgeWeightedGraph G,int v)
    {
        marked[v]=true;
        for(Edge e:G.adj(v))
        {
            if(!marked[e.other(v)])
                pq.add(e);
        }
    }

    public Iterable<Edge> edges()
    {
        return mst;
    }

    public double weight()
    {
        double weight=0;
        for(Edge i:edges())
        {
            weight+=i.weight();
        }
        return weight;
    }

    public static void main(String[] args)
    {

    }
}

