import numpy as np


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

    