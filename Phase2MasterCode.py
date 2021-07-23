from multiprocessing import Process

def one(): import Video
def two(): import Phase2Final

Process(target=one).start()
Process(target=two).start()