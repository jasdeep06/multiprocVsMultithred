import threading
import multiprocessing
import time
from expCPU_routine import check_factors,check_factors_increased_load,check_factors_multiprocess_without_cache,\
    check_factors_multiprocess_without_cache_increased_load,check_factors_without_cache_increased_load,\
    check_factors_multiprocess,check_factors_without_cache,check_factors_multiprocess_increased_load
from utils import plot_bar_graph,clear_queue


def get_threaded_time(num_threads,inp,factors,target_function):
    range_numbers = list(range(1,inp))
    times = []
    for num_thread in num_threads:
        factors.clear()
        print("Running in {} threads".format(str(num_thread)))
        threads = []
        items_per_thread = len(range_numbers)//num_thread
        for thread_count in range(num_thread):
            threads.append(threading.Thread(target=target_function,args=(range_numbers[thread_count*items_per_thread:(thread_count+1)*items_per_thread],inp,factors,)))
        t_start = time.time()
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        t_end = time.time()

        times.append(round(t_end-t_start,4))
    return times


def get_multiprocess_times(num_processes,inp,factors,target_function):
    times = []
    range_numbers = list(range(1,inp))
    for num_process in num_processes:
        clear_queue(factors)
        print("Running in {} processes".format(str(num_process)))
        processes = []
        items_per_process = len(range_numbers)//num_process
        for process_count in range(num_process):
            processes.append(multiprocessing.Process(target=target_function,args=(range_numbers[process_count*items_per_process:(process_count+1)*items_per_process],inp,factors,)))
        t_start = time.time()
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        t_end = time.time()

        times.append(round(t_end-t_start,4))
    return times

def select_target_function(profile_load_high,profile_cache):
    if profile_cache == True and profile_load_high == False:
        thread_target_function = check_factors
        multiprocessing_target_function = check_factors_multiprocess
        plot_title = "Cached Normal load"
        plot_file = "results\\cached_normal.png"
    elif profile_cache == False and profile_load_high == False:
        thread_target_function = check_factors_without_cache
        multiprocessing_target_function = check_factors_multiprocess_without_cache
        plot_title = "Not Cached Normal load"
        plot_file = "results\\not_cached_normal.png"
    elif profile_cache == True and profile_load_high == True:
        thread_target_function = check_factors_increased_load
        multiprocessing_target_function = check_factors_multiprocess_increased_load
        plot_title = "Cached High Load"
        plot_file = "results\\cached_high.png"
    elif profile_cache == False and profile_load_high == True:
        thread_target_function = check_factors_without_cache_increased_load
        multiprocessing_target_function = check_factors_multiprocess_without_cache_increased_load
        plot_title = "Not Cached High Load"
        plot_file = "results\\not_cached_high.png"

    return thread_target_function,multiprocessing_target_function,plot_title,plot_file



if __name__  == "__main__":
    inp = 25600000
    threads_processes = [1,2,4,8]
    factors = []

    # Case1 Normal load,Cached
    threading_target_function,multiprocessing_target_function,plot_title,plot_file = select_target_function(
        profile_load_high=False,profile_cache=True)
    threaded_times = get_threaded_time(threads_processes,inp,factors,threading_target_function)
    factors_queue = multiprocessing.Queue()
    multiprocessing_times = get_multiprocess_times(threads_processes,inp,factors_queue,multiprocessing_target_function)
    plot_bar_graph([threaded_times,multiprocessing_times],threads_processes,"time(s)","Number of threads/processes"
                   ,plot_title,plot_file)

    # Case2 High load,Cached
    threading_target_function,multiprocessing_target_function,plot_title,plot_file = select_target_function(
        profile_load_high=True,profile_cache=True)
    threaded_times = get_threaded_time(threads_processes,inp,factors,threading_target_function)
    factors_queue = multiprocessing.Queue()
    multiprocessing_times = get_multiprocess_times(threads_processes,inp,factors_queue,multiprocessing_target_function)
    plot_bar_graph([threaded_times,multiprocessing_times],threads_processes,"time(s)","Number of threads/processes",
                   plot_title,plot_file)

    # Case2 Normal load,Not Cached
    threading_target_function, multiprocessing_target_function, plot_title,plot_file = select_target_function(
        profile_load_high=False, profile_cache=False)
    threaded_times = get_threaded_time(threads_processes, inp, factors, threading_target_function)
    factors_queue = multiprocessing.Queue()
    multiprocessing_times = get_multiprocess_times(threads_processes, inp, factors_queue,
                                                   multiprocessing_target_function)
    plot_bar_graph([threaded_times, multiprocessing_times], threads_processes, "time(s)", "Number of threads/processes",
                   plot_title, plot_file)

    # Case2 High load,Not Cached
    threading_target_function, multiprocessing_target_function, plot_title,plot_file = select_target_function(
        profile_load_high=True, profile_cache=False)
    threaded_times = get_threaded_time(threads_processes, inp, factors, threading_target_function)
    factors_queue = multiprocessing.Queue()
    multiprocessing_times = get_multiprocess_times(threads_processes, inp, factors_queue,
                                                   multiprocessing_target_function)
    plot_bar_graph([threaded_times, multiprocessing_times], threads_processes, "time(s)", "Number of threads/processes",
                   plot_title, plot_file)

