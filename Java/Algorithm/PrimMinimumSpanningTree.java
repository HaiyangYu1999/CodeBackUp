public class PrimMinimumSpanningTree
{
    private Edge[] edgeTo;
    private double[] distTo;
    private boolean[] marked;
    private IndexMinPQ<Double> pq;

    public PrimMinimumSpanningTree(EdgeWeightedGraph G)
    {
        edgeTo=new Edge[G.V()];
        distTo=new double[G.V()];
        marked=new boolean[G.V()];
        pq=new IndexMinPQ<>(G.V());
        for(int v=0;v<G.V();++v)
        {
            distTo[v]=Double.POSITIVE_INFINITY;
        }
        distTo[0]=0;
        pq.insert(0,0.0);
        while(!pq.isEmpty())
        {
            visit(G,pq.delMin());
        }
    }
    private void visit(EdgeWeightedGraph G,int v)
    {
        marked[v]=true;
        for(Edge e:G.adj(v))
        {
            int w=e.other(v);
            if(marked[w])
                continue;
            if(e.weight()<distTo[w])
            {
                edgeTo[w]=e;
                distTo[w]=e.weight();
                if(pq.contains(w))
                    pq.change(w,distTo[w]);
                else
                    pq.insert(w,distTo[w]);
            }
        }
    }
    public Iterable<Edge> edges()
    {
        LinkedBag<Edge> mst=new LinkedBag<>();
        for(int v=1;v<edgeTo.length;++v)
        {
            if(edgeTo[v]!=null)
                mst.add(edgeTo[v]);
        }
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
        EdgeWeightedGraph G=new EdgeWeightedGraph(5);
        G.addEdge(new Edge(3,4,1));
        G.addEdge(new Edge(4,0,1));
        PrimMinimumSpanningTree tree=new PrimMinimumSpanningTree(G);
        for(Edge e:tree.edges())
        {
            System.out.println(e);
        }
        System.out.println(tree.weight());
    }
}
