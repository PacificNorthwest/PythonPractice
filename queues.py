from queue import Queue
from threading import Thread
from time import sleep

class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                else:
                    yield item
            finally:
                self.task_done()

    def __len__(self):
        return self.qsize()

class Worker(Thread):
    def __init__(self, in_queue, out_queue, func):
        super().__init__()
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.func = func

    def run(self):
        for item in self.in_queue:
            print('Processing item')
            result = self.func(item)
            self.out_queue.put(result)

class Img:
    def __init__(self, width, height, *, id = None):
        self.width = width
        self.height = height
        self.id = id


def download_image(index):
    print(f'Downloading image #{index}')
    sleep(0.1)
    return Img(600, 600, id=index)

def downscale_image(img):
    print(f'Processing image with Id {img.id}')
    sleep(0.1)
    img.width /= 2
    img.height /=2
    return img

def upload_image(img):
    print(f'Uploading image with Id {img.id}')
    sleep(0.1)
    return img

download_queue = ClosableQueue()
processing_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()

threads = [
    Worker(download_queue, processing_queue, download_image),
    Worker(processing_queue, upload_queue, downscale_image),
    Worker(upload_queue, done_queue, upload_image)
]

for thread in threads:
    thread.start()

for id in range(100):
    download_queue.put(id)
    
download_queue.close()
download_queue.join()
processing_queue.close()
processing_queue.join()
upload_queue.close()
upload_queue.join()

print()
print(f'Processing done! Totally processed {len(done_queue)} items')




