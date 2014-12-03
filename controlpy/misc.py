from __future__ import division, print_function

import numpy as np
import scipy.linalg



def steady_state_kalman_filter(A, H, Q, R):
    X = np.matrix(scipy.linalg.solve_discrete_are(A.T, H.T, Q, R))
    
    #compute the kalman filter gain
    K = np.matrix(X*H.T*scipy.linalg.inv(H*X*H.T + R))
    
    eigVals, eigVecs = scipy.linalg.eig(A-B*K)
    
    return K, X, eigVals
    

    
def gramian_controllability(A, B):
    '''Compute the controllability gramian of the stable continuous time system.
    
    dx = A*x + B*u
    
    '''
    eigVals, eigVecs = scipy.linalg.eig(A)
    if np.max(np.real(eigVals)) >= 0:
        print('Cannot compute gramian for A, has an eigen value with real part:',np.max(np.real(eigVals)))
        return None
    
    Wc = scipy.linalg.solve_lyapunov(A, -B*B.T)
    return Wc
    
    
    
    
    
    
    
    
    