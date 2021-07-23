from multiprocessing import Process

def one(): import Video
def two(): import ServoPan

Process.daemon=True

Process(target=one).start()
Process(target=two).start()