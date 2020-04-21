import java.util.LinkedList;
import java.util.Queue;

public class KruskalMinimumSpanningTree
{
    private Queue<Edge> mst;

    public KruskalMinimumSpanningTree(EdgeWeightedGraph G)
    {
        mst=new LinkedList<>();
        MinPQ<Edge> pq=new MinPQ<>(G.edges());
        UnionFindQF uf=new UnionFindQF(G.V());
        while(!pq.isEmpty()&&mst.size()<G.V()-1)
        {
            Edge e=pq.delMin();
            int v=e.either();
            int w=e.other(v);
            if(uf.connected(v,w))
                continue;
            uf.union(v,w);
            mst.offer(e);
        }
    }

    public Iterable<Edge> edges()
    {
        return mst;
    }

    public double weight()
    {
        double s=0;
        for(Edge e:edges())
        {
            s+=e.weight();
        }
        return s;
    }

    public static void main(String[] args)
    {
        EdgeWeightedGraph G=new EdgeWeightedGraph(5);
        G.addEdge(new Edge(3,4,1));
        G.addEdge(new Edge(4,0,1));
        KruskalMinimumSpanningTree tree=new KruskalMinimumSpanningTree(G);
        for(Edge e:tree.edges())
        {
            System.out.println(e);
        }
        System.out.println(tree.weight());
    }
}
