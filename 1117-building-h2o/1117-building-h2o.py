from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.h_sem = Semaphore(2)   # allow 2 hydrogens
        self.o_sem = Semaphore(1)   # allow 1 oxygen
        self.barrier = Barrier(3)   # wait for 3 threads (HHO)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()
        self.barrier.wait()         # wait for full molecule
        releaseHydrogen()
        self.h_sem.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sem.acquire()
        self.barrier.wait()         # wait for full molecule
        releaseOxygen()
        self.o_sem.release()
