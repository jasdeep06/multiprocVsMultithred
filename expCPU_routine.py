

def check_factors(numbers,inp,factors):
    for number in numbers:
        if inp % number == 0:
            factors.append(number)

def check_factors_multiprocess(numbers,inp,factors_queue):
    for number in numbers:
        if inp % number == 0:
            factors_queue.put(number)


def check_factors_increased_load(numbers,inp,factors):
    for i in range(10):
        for number in numbers:
            if inp % number == 0:
                factors.append(number)

def check_factors_multiprocess_increased_load(numbers,inp,factors_queue):
    for i in range(10):
        for number in numbers:
            if inp % number == 0:
                factors_queue.put(number)


def check_factors_without_cache(numbers,inp,factors):
    for number in numbers:
        if inp % number == 0:
            continue


def check_factors_multiprocess_without_cache(numbers, inp, factors_queue):
    for number in numbers:
        if inp % number == 0:
            continue


def check_factors_without_cache_increased_load(numbers,inp,factors):
    for i in range(10):
        for number in numbers:
            if inp % number == 0:
                continue


def check_factors_multiprocess_without_cache_increased_load(numbers, inp, factors_queue):
    for i in range(10):
        for number in numbers:
            if inp % number == 0:
                continue
