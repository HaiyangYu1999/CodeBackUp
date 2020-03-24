import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Stack;

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
        double[][] cmi=new double[7][7];
        cmi[0]=new double[]{2.2774,0.4733,0.4176,0.9615,0.6343,0.3158,0.6986};
        cmi[1]=new double[]{0.4733,2.1146,0.427,0.5486,0.6577,0.2212,0.4996};
        cmi[2]=new double[]{0.4176,0.427,2.3009,0.2837,0.2082,0.3031,0.2887};
        cmi[3]=new double[]{0.9615,0.5486,0.2837,2.1897,0.8958,0.2956,1.1077};
        cmi[4]=new double[]{0.6343,0.6577,0.2082,0.8958,2.1595,0.2434,0.9272};
        cmi[5]=new double[]{0.3158,0.2212,0.3031,0.2956,0.2434,2.2651,0.3615};
        cmi[6]=new double[]{0.6986,0.4996,0.2887,1.1077,0.9272,0.3615,2.156};

        EdgeWeightedGraph G=new EdgeWeightedGraph(7);
        for(int i=0;i<7;++i)
        {
            for(int j=0;j<i;++j)
            {
                G.addEdge(new Edge(i,j,-cmi[i][j]));
            }
        }
        PrimMST pmst=new PrimMST(G);
        for(Edge i:pmst.edges())
        {
            System.out.println(i);
        }

    }
}

class Edge implements Comparable<Edge>
{
    private final int v;
    private final int w;
    private final double weight;
    public Edge(int v,int w,double weight)
    {
        this.v=v;
        this.w=w;
        this.weight=weight;
    }
    public double weight()
    {
        return weight;
    }
    public int either()
    {
        return v;
    }
    public int other(int vertex)
    {
        if(vertex==this.v)
            return w;
        else if(vertex==this.w)
            return v;
        else throw new RuntimeException("Inconsistent edge");
    }
    @Override
    public int compareTo(Edge that)
    {
        if(this.weight<that.weight)
            return -1;
        else if(this.weight>that.weight)
            return 1;
        else return 0;
    }
    @Override
    public String toString()
    {
        return String.format("%d--%d %.2f",v,w,weight);
    }
}

class EdgeWeightedGraph
{
    private final int V;
    private int E;
    private Stack<Edge>[] adj;
    public EdgeWeightedGraph(int V)
    {
        this.V=V;
        this.E=0;
        adj=(Stack<Edge>[]) new Stack[V];
        for(int i=0;i<V;++i)
        {
            adj[i]=new Stack<>();
        }
    }
    public int V()
    {
        return V;
    }
    public int E()
    {
        return E;
    }
    public void addEdge(Edge e)
    {
        int v=e.either(),w=e.other(v);
        adj[v].add(e);
        adj[w].add(e);
        ++E;
    }
    public Iterable<Edge> adj(int v)
    {
        return adj[v];
    }
    public Iterable<Edge> edges()
    {
        Stack<Edge> b=new Stack<>();
        for(int i=0;i<V;++i)
        {
            for(Edge e:adj[i])
            {
                if(e.other(i)>i)
                    b.add(e);
            }
        }
        return b;
    }
    @Override
    public String toString()
    {
        String s=V+" vertices, "+E+"edges\n";
        for(int v=0;v<V;++v)
        {
            s+=v+": ";
            for(Edge w:adj(v))
            {
                s+=w+" ";
            }
            s+="\n";
        }
        return s;
    }
}
