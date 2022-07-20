from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(BaseWorker):
    def work(self):
        print("I'm working!")


class SuperWorker(BaseWorker):
    def work(self):
        print("I work very hard!!")


class LazyWorker(BaseWorker):
    def work(self):
        print("I am lazy worker!!!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), '`worker` must be of type {}'.format(BaseWorker)
        # is same
        # if not isinstance(worker, BaseWorker):
        #     raise AssertionError(f"worker` must be of type {BaseWorker}")
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
super_worker = SuperWorker()
lazy_worker = LazyWorker()
manager = Manager()

try:
    manager.set_worker(worker)
    manager.manage()
    manager.set_worker(super_worker)
    manager.manage()
    manager.set_worker(lazy_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")