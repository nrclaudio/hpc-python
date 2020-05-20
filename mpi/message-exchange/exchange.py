from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

my_rank = {'rank': rank}

if rank == 0:
    comm.send(my_rank, dest=1)
    msg = comm.recv(source=1)

elif rank == 1:
    comm.send(my_rank, dest=0)
    msg = comm.recv(source=0)
print("Rank %d received a message from rank %d." %
      (rank, msg['rank']))


n = 100000
my_array = np.full(n, rank, int)
buff = np.empty(n, int)

if rank == 0:
    comm.Send([my_array, n, MPI.INT], dest=1)
    comm.Recv([buff, n, MPI.INT], source=1)
elif rank == 1:
    comm.Recv([buff, n, MPI.INT], source=0)
    comm.Send([my_array, n, MPI.INT], dest=0)
print("I'm rank {} and have received an array with first element: {}".
      format(rank, buff[0]))
