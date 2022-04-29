from ctypes.wintypes import FLOAT
import numpy as np
import random as rd

class mat_gen():

    # generates id matrix of size N x M
    def id_mat(self,n,m):

        # inits output mat
        out = np.zeros(n,m)
        dia_ind = 0

        for i in range(0,n):
            for k in range(0,m):
                if k == dia_ind:
                    out[i][k] = 1
                    dia_ind = dia_ind + 1

        return out


    def random(self,n,m,num_type = FLOAT, high = 10,low = -10):
        out = np.zeros(n,m)

        for i in range(0,n):
            for j in range(0,m):
                if num_type == 'int':
                    out[i][j] = rd.randint(low,high) 
                elif num_type == 'float':
                    sign = np.randint(-1,1)
                    out[i][j] = rd.random() * high * sign
                else:
                    sign = np.randint(-1,1)
                    out[i][j] = rd.random() * high * sign

    def matToId(self,mat):
        shape = np.shape(mat)
        out = np.zeros(shape[0],shape[1])

        if shape[0] != shape[1]:
            print("Error: Identity matrix must be square")
        else:
            for i in range(0,shape[0]):
                for j in range(0,shape[1]):
                    out[i][j] = 1

    