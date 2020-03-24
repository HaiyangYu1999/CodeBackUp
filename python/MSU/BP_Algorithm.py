import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

#standarize the input data
def standardize(In,Out):
    data = np.loadtxt(In)
    m, n = np.size(data, 0), np.size(data, 1)
    for i in range(m):
        for j in range(n):
            data[i][j] = (data[i][j] - data[i].min()) / (data[i].max()-data[i].min())
    np.savetxt(Out, data)

def BPNeutualNetwork(dataset,d,q,l,eta,iteration_number=500):
    D=dataset
    #randomly generate parameters
    theta = np.random.rand(l, 1)
    gamma = np.random.rand(q,1)
    v = np.random.rand(d, q)
    w = np.random.rand(q, l)
    #define intermediate variable
    alpha = np.zeros(q)
    beta = np.zeros(l)
    g = np.zeros(l)
    b = np.zeros(q)
    y_estimate = np.zeros(l)
    #define the error
    E = 0

    for iteration in range(iteration_number):
        E = 0
        for column in range(np.size(D, 1)):
            #get the output
            x = D[:-1, column]
            y = D[-1][column]
            for i in range(np.size(v, 1)):
                alpha[i] = np.array(v[:, i]).dot(x)
            for h in range(np.size(b)):
                b[h]=sigmoid(alpha[h]-gamma[h])
            for i in range(np.size(w, 1)):
                beta[i] = np.array(w[:, i]).dot(b)
            y_estimate = sigmoid(beta - theta)
            #get the error
            E += 0.5 * (y_estimate - y).dot(y_estimate - y)
            #gradient descent method
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
            #renew parameters
            w += w_delta
            theta += theta_delta
            v += v_delta
            gamma += gamma_delta
        #renew the error
        E /= np.size(D, 1)
    #return parameters
    return theta,gamma,v,w,E

#prediction on test set
def calculate(Testdata,v,w,theta,gamma):
    D=Testdata
    alpha = np.zeros(q)
    beta = np.zeros(l)
    b = np.zeros(q)
    y_array=[]
    for column in range(np.size(D, 1)):
        x = D[:-1, column]
        y = D[-1][column]
        for i in range(np.size(v, 1)):
            alpha[i] = np.array(v[:, i]).dot(x)
        for h in range(np.size(b)):
            b[h] = sigmoid(alpha[h] - gamma[h])
        for i in range(np.size(w, 1)):
            beta[i] = np.array(w[:, i]).dot(b)
        y_estimate = sigmoid(beta - theta)
        y_array.append(y_estimate)
    return y_array


if __name__=="__main__":
    standardize('Dataset.txt','DatasetNew.txt')
    d=7       #number of input layer
    q=10      #number of hidden layer
    l=1       #number of output layer
    eta=0.01  #learing rate
    Train = np.loadtxt('Trainingset.txt')
    Test = np.loadtxt('Testset.txt')
    theta,gamma,v,w,E=BPNeutualNetwork(Train,d,q,l,eta,iteration_number=100)
    res=calculate(Test,v,w,theta,gamma)
