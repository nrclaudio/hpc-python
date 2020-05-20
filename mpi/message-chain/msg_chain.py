from mpi4py import MPI
import numpy as np
from sys import stdout

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
ntasks = comm.Get_size()


myarray = np.full(10, myid, int)
mybuff = np.empty(10, int)

if myid < ntasks - 1 and myid >= 1:
    comm.Send(myarray, dest=myid + 1)
    print("I'm rank {} and I'm sending {}".
          format(myid, len(myarray)))
    comm.Recv(mybuff, source=myid - 1)
    print("I'm rank {} and I've received an array with"
          " first element {}". format(myid, mybuff[0]))
elif myid < ntasks - 1 and myid < 1:
    comm.Send(myarray, dest=myid + 1)
    print("I'm rank {} and I'm sending {}".
          format(myid, len(myarray)))


# Wait for the first batch to finish #
stdout.flush()
comm.barrier()

if myid == 0:
    print("")
    print("Sendrecv (in the middle of the chain):")


if myid < ntasks - 1 and myid >= 1:
    comm.Sendrecv(myarray, dest=myid + 1, source=myid - 1, recvbuf=mybuff)
    print("I'm rank {} and I'm sending {}".
          format(myid, len(myarray)))
    print("I'm rank {} and I've received an array with"
          " first element {}". format(myid, mybuff[0]))
elif myid < ntasks - 1 and myid < 1:
    comm.Send(myarray, dest=myid + 1)
    print("I'm rank {} and I'm sending {}".
          format(myid, len(myarray)))
