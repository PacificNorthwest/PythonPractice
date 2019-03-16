from profile import Profile
from pstats import Stats
from time import sleep

def computation(x, y):
    for i in range(999999):
        i *= i
        

profiler = Profile()
profiler.runcall(computation, 324534, 223)
stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
print('Done')