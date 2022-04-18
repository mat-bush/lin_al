import numpy as np

class mat_multiple():

    def mat_vect(self,A,X):
#         # A: matix 
#         # X: Vector

        if (np.shape(A)[1] != np.shape(X)[0]):
            # handles vectors being mismatched size error
            print("Error: Width of 'A' must be eqaul to Lenght of 'X'")
            return None

        elif (np.shape(A)[1] != np.shape(A)[0]):
            # handles non-square 'A' input matrix
            print("Error: 'A' must be square")
            return None
            
        else:
    #       # initializes output vector
            B = np.zeros((np.shape(A)[0],1))

            # pulls each row
            for i in range(0,np.shape(X)[0]):
                
                row = A[i][:]

                # scales row elememts by apropriate vector element
                for j in range(0,len(row)):
                    row[j] = row[j] * X[j]

                B[i] = np.sum(row)


            return B    

    # the more effecient way. Like to keep easiest way in mind 
    # if I need to use the method in the future
    def easyway(self,A,X):
        return A.dot(X)

