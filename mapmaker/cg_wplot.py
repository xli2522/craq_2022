#bog-standard Conjugate Gradient solver, as you would copy from wikipedia
#Note that we don't actually care what A, b, etc. look like, as long as
#the various operators (@,+/-,multiplication by a scalar) are supported.

from matplotlib import pyplot as plt

def cg(x0,b,A,niter=35,plot=False,pause_len=0.5):
    #get the everything set up
    x=x0.copy()
    r=b-A@x
    p=r.copy()
    rr=r@r

    
    #iterate to solve the matrix equation
    for i in range(niter):
        Ap=A@p  #this step is matrix times vector, and in most problems will dominate your run time.
        pAp=p@Ap
        alpha=rr/pAp
        
        x=x+alpha*p
        if plot:
            plt.clf()
            plt.imshow(x.maps[0].map)
            plt.show()
            plt.pause(pause_len)
        r=r-alpha*Ap

        rr_new=r@r
        beta=rr_new/rr
        p=r+beta*p
        rr=rr_new
        print('residual is on step ',i,' is ',rr)
    return x
