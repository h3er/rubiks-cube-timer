from timeit import default_timer as t
import keyboard as k
import numpy as np

allTimes, sortedTimes, avgTime, avgLast5, avgLast12, avgBest5, avgBest12, counter = [], [], 0, 0, 0, 0, 0, 0

while True:
    print('\n')
    print('press shift to start')
    k.wait('shift')
    start = t()
    k.wait('shift')
    end = t()
    timeTaken = round(end - start, 3)
    dec = input((f'{timeTaken}, would you like to keep this time? y/n: ')).lower().strip()
    if dec == 'y':
        counter += 1
        allTimes.append(timeTaken)
        sortedTimes.append(timeTaken)
        sortedTimes.sort()
        avgTime = round(np.average(allTimes), 3)
        print(f'average: {avgTime}')
        if counter >= 5:
            avgLast5 = round(np.average(allTimes[:-4]), 3)
            avgBest5 = round(np.average(sortedTimes[:5]), 3)
            print(f'average of last 5: {avgLast5}')
            print(f'average of best 5: {avgBest5}')
            if counter >= 12:
                avgLast12 = round(np.average(allTimes[:-11]), 3)
                avgBest12 = round(np.average(sortedTimes[:12]), 3)
                print(f'average of last 12: {avgLast12}')
                print(f'average of best 12: {avgBest12}')
    else:
        print('loser')
