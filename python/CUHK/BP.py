import numpy as np


def sigmoid(x):
    return 1/(1+np.exp(-x))


def datadivision(In):
    b = np.loadtxt(In)
    step = 100
    for i in range(25):
        begin = i * step
        end = (i + 1) * step
        test = b[:, begin:end]
        train = np.delete(b, range(begin, end), axis=1)
        np.savetxt('Test{}.txt'.format(i), test)
        np.savetxt('Training{}.txt'.format(i), train)


def standardize(In,Out):
    data = np.loadtxt(In)
    #data=data.T
    m, n = np.size(data, 0), np.size(data, 1)
    for i in range(m):
        for j in range(n):
            data[i][j] = (data[i][j] - data[i].min()) / (data[i].max()-data[i].min())
    np.savetxt(Out, data)


def BPNeutualNetwork(database,d,q,l,eta,iteration_number=500):
    D=database
    theta = np.random.rand(l, 1)
    gamma = np.random.rand(q,1)
    v = np.random.rand(d, q)
    w = np.random.rand(q, l)
    alpha = np.zeros(q)
    beta = np.zeros(l)
    b = np.zeros(q)
    #y_estimate = np.zeros(l)
    E = 0
    g = np.zeros(l)
    for iteration in range(iteration_number):
        E = 0
        for column in range(np.size(D, 1)):
            x = D[:-1, column]
            y = D[-1][column]
            for i in range(np.size(v, 1)):
                alpha[i] = np.array(v[:, i]).dot(x)
            for h in range(np.size(b)):
                b[h]=sigmoid(alpha[h]-gamma[h])
            for i in range(np.size(w, 1)):
                beta[i] = np.array(w[:, i]).dot(b)
            y_estimate = sigmoid(beta - theta)
            E += 0.5 * (y_estimate - y).dot(y_estimate - y)
            g = y_estimate * (1 - y_estimate) * (y - y_estimate)
            w_delta = np.zeros((q, l))
            for i in range(np.size(b)):
                for j in range(np.size(g)):
                    w_delta[i][j] = eta * b[i] * g[j]
            theta_delta = np.zeros(np.size(theta))
            for j in range(np.size(g)):
                theta_delta[j] = -eta * g[j]
            e = np.zeros(np.size(b))
            sumh = np.zeros(np.size(b))
            for h in range(np.size(sumh)):
                for j in range(l):
                    sumh[h] += w[h][j] * g[j]
            e = b * (1 - b) * sumh
            v_delta = np.zeros((d, q))
            for i in range(np.size(x)):
                for h in range(np.size(e)):
                    v_delta[i][h] = eta * e[h] * x[i]
            gamma_delta = np.zeros((q, 1))
            for h in range(np.size(e)):
                gamma_delta[h] = -eta * e[h]
            w += w_delta
            theta += theta_delta
            v += v_delta
            gamma += gamma_delta
        E /= np.size(D, 1)
    return theta,gamma,v,w,E


def calculate(Testdata,v,w,theta,gamma):
    D=Testdata
    alpha = np.zeros(q)
    beta = np.zeros(l)
    b = np.zeros(q)
    y_array=[]
    for column in range(np.size(D, 1)):
        x = D[:-1, column]
        #y = D[-1][column]
        for i in range(np.size(v, 1)):
            alpha[i] = np.array(v[:, i]).dot(x)
        for h in range(np.size(b)):
            b[h] = sigmoid(alpha[h] - gamma[h])
        for i in range(np.size(w, 1)):
            beta[i] = np.array(w[:, i]).dot(b)
        y_estimate = sigmoid(beta - theta)[0][0]
        y_array.append(y_estimate)
    return y_array


if __name__=="__main__":
    #standardize('originaldiscrete.txt','originaldiscrete1.txt')
    Train=np.loadtxt('test_new.txt')
    Test=np.loadtxt('test_new.txt')

    d=6
    q=8
    l=1
    eta=1/100
    theta,gamma,v,w,E=BPNeutualNetwork(Train,d,q,l,eta,iteration_number=100)
    print(v)
    print(w)
    print(v.dot(w))
#    res=calculate(Test,v,w,theta,gamma)
#    sgn=[]
 #   k=0
  #  for i in res:
 #       if i>.5:
 #           sgn.append(1)
 #       else:
 #           sgn.append(0)
 #   for i in range(np.size(res)):
 #       if sgn[i]-Test[-1][i]==0:
  #          k+=1
#
 #   print(sgn)
  #  print(s/100,k/40)


