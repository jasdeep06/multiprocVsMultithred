import threading
import time
import multiprocessing
from utils import download_and_save_image,plot_bar_graph



def save_images(image_ids):
    for image_id in image_ids:
        download_and_save_image(image_id)

def get_thread_times(num_threads,image_ids):
    times = []
    for num_thread in num_threads:
        print("Running in {} threads".format(str(num_thread)))
        threads = []
        items_per_thread = len(image_ids)//num_thread
        for thread_count in range(num_thread):
            threads.append(threading.Thread(target=save_images,args=(image_ids[thread_count*items_per_thread:(thread_count+1)*items_per_thread],)))
        t_start = time.time()
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        t_end = time.time()

        times.append(round(t_end-t_start,4))
    return times


def get_multiprocess_times(num_processes,image_ids):
    times = []
    for num_process in num_processes:
        print("Running in {} processes".format(str(num_process)))
        processes = []
        items_per_thread = len(image_ids)//num_process
        for process_count in range(num_process):
            processes.append(multiprocessing.Process(target=save_images,args=(image_ids[process_count*items_per_thread:(process_count+1)*items_per_thread],)))
        t_start = time.time()
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        t_end = time.time()

        times.append(round(t_end-t_start,4))
    return times


if __name__ == "__main__":
    threads_processes  = [1,2,4,8]
    multithread_times = get_thread_times(threads_processes,list(range(64)))
    multiprocess_times = get_multiprocess_times(threads_processes,list(range(64)))
    plot_bar_graph([multithread_times,multiprocess_times],threads_processes,"time(s)",
                   "number of threads/processes","IO task","results\\io_task_comparision.png")

