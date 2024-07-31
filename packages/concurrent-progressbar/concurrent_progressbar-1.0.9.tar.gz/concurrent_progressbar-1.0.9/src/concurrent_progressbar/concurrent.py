from multiprocessing import Process, Queue
import threading as th
from threading import Thread
from tqdm import tqdm
import time
import os


class _Concurrency(object):
    def __init__(self, num_workers, target: list, args: list, task_desc: list = None):
        super(_Concurrency, self).__init__()
        self._max_workers = min([len(a) for a in args])
        self._num_workers = num_workers if num_workers <= self._max_workers else self._max_workers
        self._target = target
        self._ntask = len(self._target)
        self._args = args
        self._task_desc = task_desc
        # self._colors = ['WHITE', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN']*5
        self._colors = ['WHITE']*self._ntask
        self._prog_bar = [tqdm(total=len(self._args[i]), dynamic_ncols=True, colour=self._colors[i], position=i, desc=f'Task {i}' if self._task_desc is None else self._task_desc[i]) for i in range(self._ntask)]
        self._queue = Queue()
        self._condition = th.Condition()

    def __str__(self):
        return f'No. of workers: {self._num_workers}\nNo. of tasks: {self._ntask}'
    
    def _status_update(self):
        while True:
            process_n = self._queue.get()
            if process_n == -1:
                break
            self._prog_bar[process_n].update()
            
    def _wait(self, _wait_queue, condition):
        while True:
            if len(_wait_queue) > 0:
                process = _wait_queue.pop()
                if process == -1:
                    try:
                        with condition:
                            condition.notify()
                    except: pass
                    break
                if process.is_active():
                    process.join()
            try:
                with condition:
                    condition.notify()
            except: pass
            
    def _task(self, i):
        condition = th.Condition()
        _wait_queue = []
        wait_t = Thread(target=self._wait, args=(_wait_queue, condition))
        wait_t.start()
        
        self._create_process_pool(i)
        _pool = self.__getattribute__(f'pool_{i}')

        for arg in self._args[i]:
            if len(_pool) < 1:
                self._create_process_pool(i)
                _pool = self.__getattribute__(f'pool_{i}')
            process = _pool.pop()
            process._args = arg
            process.start()
                
            if process.is_alive():
                _wait_queue.append(process)
                
            self._queue.put(int(i))
                
            try:
                while len(_wait_queue) >= self._num_workers:
                    with condition:
                        condition.wait()
            except KeyboardInterrupt as k:
                os._exit(0)
            except Exception as e:
                pass

        _wait_queue.append(-1)
        
        while len(_wait_queue) > 0:
            with condition:
                condition.wait()
    
    def run(self):
        t = Thread(target=self._status_update)
        t.start()
        
        p = [Process(target=self._task, args=(i,)) for i in range(self._ntask)]
        for _p in p:
            _p.start()
            
        for _p in p:
            _p.join()
        self._queue.put(-1)


class Multiprocessing(_Concurrency):
    def __init__(self, num_workers, target: list, args: list, task_desc: list = None):
        """Spawn the target method in different processes.

        Args:
            num_workers (_type_): Number of processes generated and executed parallel.
            target (list): The method to be executed.
            args (list): arguments for the targets
            task_desc (list, optional): _description_. Give name to the tasks.
        """
        super(Multiprocessing, self).__init__(
            num_workers=num_workers, target=target, args=args, task_desc=task_desc
        )
    
    def _create_process_pool(self, i):
        self.__setattr__(f'pool_{i}', [Process(target=self._target[i]) for _ in range(self._num_workers)])
            

class Multithreading(_Concurrency):
    def __init__(self, num_workers, target: list, args: list, task_desc: list = None):
        """Spawn the target method in different processes.

        Args:
            num_workers (_type_): Number of threads generated and executed parallel.
            target (list): The method to be executed.
            args (list): arguments for the targets
            task_desc (list, optional): _description_. Give name to the tasks.
        """
        super(Multithreading, self).__init__(
            num_workers=num_workers,
            target=target,
            args=args,
            task_desc=task_desc,
        )
    
    def _create_process_pool(self, i):
        self.__setattr__(f'pool_{i}', [Thread(target=self._target[i]) for _ in range(self._num_workers)])