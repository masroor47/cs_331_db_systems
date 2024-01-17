import random
import time 


def trial(searches, collection):
    tot_time = 0.0
    for s in searches:
        start_time = time.perf_counter()
        if s in collection:
            pass
        end_time = time.perf_counter()
        tot_time += end_time - start_time
    return tot_time / len(searches)

def get_searches(words, length):
    return [random.choice(words) for _ in range(length)]

if __name__ == '__main__':
    keywords = []
    list_ = ['SELECT', '(SELECT', 'SHOW', 'DESC']
    set_ = {'SELECT', '(SELECT', 'SHOW', 'DESC'}

    repetitions = 1000
    num_trials = 50
    list_time = 0.0
    set_time = 0.0

    for _ in range(num_trials):
        searches = get_searches(list_, repetitions)
        list_time += trial(searches, list_)
        set_time += trial(searches, set_)
        
    print(f"conducted {num_trials} trials with {repetitions} repetitions")
    print(f"avg list lookup time: {list_time / num_trials}")
    print(f"avg set lookup time: {set_time / num_trials}")