import java.util.HashSet;
import java.util.Stack;

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
        else
            return v;
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

class Graph
{
    private final int V;
    private int E;
    private HashSet<Edge>[] adj;
    public Graph(int V)
    {
        this.V=V;
        this.E=0;
        adj=(HashSet<Edge>[]) new HashSet[V];
        for(int i=0;i<V;++i)
        {
            adj[i]=new HashSet<>();
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
        HashSet<Edge> b=new HashSet<>();
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
    public int checkempty()
    {
        for(int i=0;i<V();++i)
        {
            int nu=0;
            for(Edge e:adj(i))
                ++nu;
            if(nu==0)
                return i;
        }
        return -1;
    }

}

public class Dijkstra
{
    private double[] distTo;
    private Edge[] edgeTo;
    private boolean[] marked;
    public Dijkstra(Graph G,int s)
    {
        distTo=new double[G.V()];
        edgeTo=new Edge[G.V()];
        marked=new boolean[G.V()];
        for(int i=0;i<G.V();++i)
        {
            distTo[i]=Double.POSITIVE_INFINITY;
        }
        distTo[s]=0;
        while(!checkEmpty())
        {
            int w=getMin();
            marked[w]=true;
            for(Edge e:G.adj(w))
            {
                relax(e);
            }
        }
    }
    private boolean checkEmpty()
    {
        for(int i=0;i<marked.length;++i)
        {
            if(!marked[i])
                return false;
        }
        return true;
    }
    private int getMin()
    {
        int j=0;
        double dist=Double.POSITIVE_INFINITY;
        for(int i=0;i<distTo.length;++i)
        {
            if(!marked[i])
            {
                if(dist>distTo[i])
                {
                    j=i;
                    dist=distTo[i];
                }
            }
        }
        return j;
    }
    private void relax(Edge e)
    {
        int v=e.either();
        int w=(marked[v])?e.other(v):v;
        v=e.other(w);
        if (distTo[w] > distTo[v] + e.weight())
        {
            distTo[w] = distTo[v] + e.weight();
            edgeTo[w] = e;
        }
    }
    public double distTo(int v)
    {
        return distTo[v];
    }


    public Iterable<Edge> pathTo(int v)
    {
        Stack<Edge> path = new Stack<>();
        int j=v;
        for (Edge e = edgeTo[v]; e != null; e = edgeTo[j])
        {
            path.push(e);
            j=e.other(j);

        }
        return path;
    }
    public static void main(String[] args)
    {
        Graph G=new Graph(63);
        G.addEdge(new Edge(0,1,132));
        G.addEdge(new Edge(1,2,81));
        G.addEdge(new Edge(2,3,35));
        G.addEdge(new Edge(3,5,117));
        G.addEdge(new Edge(2,4,118));
        G.addEdge(new Edge(4,5,50));
        G.addEdge(new Edge(4,6,74));
        G.addEdge(new Edge(6,7,59));
        G.addEdge(new Edge(5,7,78));
        G.addEdge(new Edge(7,9,339));
        G.addEdge(new Edge(7,8,39));
        G.addEdge(new Edge(8,10,92));
        G.addEdge(new Edge(10,11,239));
        G.addEdge(new Edge(10,12,164));
        G.addEdge(new Edge(12,14,80));
        G.addEdge(new Edge(9,14,112));
        G.addEdge(new Edge(9,16,343));
        G.addEdge(new Edge(16,19,125));
        G.addEdge(new Edge(12,13,238));
        G.addEdge(new Edge(11,59,116));
        G.addEdge(new Edge(59,13,75));
        G.addEdge(new Edge(13,15,83));
        G.addEdge(new Edge(15,21,135));
        G.addEdge(new Edge(14,21,95));
        G.addEdge(new Edge(14,18,111));
        G.addEdge(new Edge(18,19,131));
        G.addEdge(new Edge(19,22,42));
        G.addEdge(new Edge(21,61,110));
        G.addEdge(new Edge(18,61,98));
        G.addEdge(new Edge(61,20,137));
        G.addEdge(new Edge(20,15,111));
        G.addEdge(new Edge(20,27,90));
        G.addEdge(new Edge(27,26,92));
        G.addEdge(new Edge(26,25,43));
        G.addEdge(new Edge(25,61,91));
        G.addEdge(new Edge(25,22,84));
        G.addEdge(new Edge(22,23,135));
        G.addEdge(new Edge(23,40,155));
        G.addEdge(new Edge(40,29,132));
        G.addEdge(new Edge(26,24,147));
        G.addEdge(new Edge(24,23,123));
        G.addEdge(new Edge(24,29,96));
        G.addEdge(new Edge(29,30,48));
        G.addEdge(new Edge(30,28,52));
        G.addEdge(new Edge(27,28,202));
        G.addEdge(new Edge(29,31,114));
        G.addEdge(new Edge(31,32,54));
        G.addEdge(new Edge(32,30,106));
        G.addEdge(new Edge(32,33,50));
        G.addEdge(new Edge(28,33,109));
        G.addEdge(new Edge(31,34,92));
        G.addEdge(new Edge(32,34,91));
        G.addEdge(new Edge(17,16,0));
        G.addEdge(new Edge(33,34,105));
        G.addEdge(new Edge(33,35,93));
        G.addEdge(new Edge(34,35,50));
        G.addEdge(new Edge(34,36,106));
        G.addEdge(new Edge(35,36,93));
        G.addEdge(new Edge(36,37,93));
        G.addEdge(new Edge(37,38,84));
        G.addEdge(new Edge(38,39,99));
        G.addEdge(new Edge(38,41,347));
        G.addEdge(new Edge(41,42,121));
        G.addEdge(new Edge(42,43,49));
        G.addEdge(new Edge(43,45,36));
        G.addEdge(new Edge(45,46,61));
        G.addEdge(new Edge(46,47,89));
        G.addEdge(new Edge(47,36,89));
        G.addEdge(new Edge(47,48,32));
        G.addEdge(new Edge(48,35,34));
        G.addEdge(new Edge(48,49,36));
        G.addEdge(new Edge(49,33,69));
        G.addEdge(new Edge(49,44,76));
        G.addEdge(new Edge(44,43,51));
        G.addEdge(new Edge(44,42,19));
        G.addEdge(new Edge(41,52,88));
        G.addEdge(new Edge(52,51,137));
        G.addEdge(new Edge(51,42,87));
        G.addEdge(new Edge(51,50,44));
        G.addEdge(new Edge(50,28,150));
        G.addEdge(new Edge(50,44,91));
        G.addEdge(new Edge(52,53,109));
        G.addEdge(new Edge(53,62,126));
        G.addEdge(new Edge(53,54,189));
        G.addEdge(new Edge(54,51,105));
        G.addEdge(new Edge(54,55,133));
        G.addEdge(new Edge(55,62,206));
        G.addEdge(new Edge(55,20,143));
        G.addEdge(new Edge(55,56,188));
        G.addEdge(new Edge(56,57,41));
        G.addEdge(new Edge(57,13,110));
        G.addEdge(new Edge(56,60,118));
        G.addEdge(new Edge(60,58,115));
        G.addEdge(new Edge(58,57,93));
        G.addEdge(new Edge(58,59,118));
        Dijkstra sp=new Dijkstra(G,0);
        for(Edge e:sp.pathTo(39))
        {
            System.out.println(e);
        }
        System.out.println(sp.distTo(39));
    }
}




