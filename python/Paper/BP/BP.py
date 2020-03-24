import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))


def datadivision(In):
    b = np.loadtxt(In)
    step = 54
    for i in range(5):
        begin = i * step
        end = (i + 1) * step
        test = b[:, begin:end]
        train = np.delete(b, range(begin, end), axis=1)
        np.savetxt('Test{}.txt'.format(i), test)
        np.savetxt('Training{}.txt'.format(i), train)


def standardize(In,Out):
    data = np.loadtxt(In)
    m, n = np.size(data, 0), np.size(data, 1)
    for i in range(m):
        for j in range(n):
            data[i][j] = (data[i][j] - data[i].min()) / (data[i].max()-data[i].min())
    np.savetxt(Out, data)
    return data[7].mean(),data[7].std()


def BPNeutualNetwork(database,d,q,l,eta,iteration_number=500):
    D=database
    theta = np.random.rand(l, 1)
    gamma = np.random.rand(q,1)
    v = np.random.rand(d, q)
    w = np.random.rand(q, l)
    alpha = np.zeros(q)
    beta = np.zeros(l)
    b = np.zeros(q)
    y_estimate = np.zeros(l)
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
    mu,sigma=standardize('dataPlusPrecipitation.txt','dataAfterStandardize.txt')
    datadivision('dataAfterStandardize.txt')
    for i in range(5):
        Train=np.loadtxt('Training{}.txt'.format(i))
        Test=np.loadtxt('Test{}.txt'.format(i))
        d=7
        q=10
        l=1
        eta=0.01
        theta,gamma,v,w,E=BPNeutualNetwork(Train,d,q,l,eta,iteration_number=100)
        res=calculate(Test,v,w,theta,gamma)
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        P = R = F1 = 0
        for i in range(np.size(res)):
            t = Test[:, i]
            if res[i] < 0.5 and t[7] < 0.5:
                tp += 1
            if res[i] < 0.5 and t[7] > 0.5:
                fp += 1
            if res[i] > 0.5 and t[7] < 0.5:
                fn += 1
            if res[i] > 0.5 and t[7] > 0.5:
                tn += 1
        P = tp / (tp + fp)
        R = tp / (tp + fn)
        F1 = 2 * P * R / (P + R)
        print('P=', P, ',R=', R, ',F1=', F1)
