from typing import Callable
from functools import wraps
import time
import logging
import threading
import numpy as np

from pydantic import PositiveFloat, NonNegativeFloat, Field
from typing import Annotated 

StrictFraction: type = Annotated[float, Field(gt=0, lt=1)]

def periodic_call(
        fun: Callable = None,
        *,
        interval: PositiveFloat = 1,
        initial_delay: NonNegativeFloat = 0.01,
        loop_condition: Callable[[object, int], bool] = lambda r, n: True,
        sleep_fraction: StrictFraction = 0.8, 
        sleep_overhead: NonNegativeFloat = 20.0e-6,
        threaded: bool = False
):
    """
Periodically calls a function using semi-precise timing witout saturating
processor. 

Optional keyword arguments:
    * interval [float, s]
        Interval to call periodically the fonction. 
    * initial_delay [float, s]
        Initial delay before the first function call
    * loop_condition [function]: 
        A function that takes the result of the function (can be None) and 
        the number of calls made and returns a boolean value. By default, 
        loop forever.  
    * sleep_fraction [float]
        Once the function has finished its periodic call sleep for a 
        fraction of the remaining time to avoid saturating the processor.
    * sleep_overhead [float, s]
        Overheads associated with the sleep loop.  Depends on CPU speed
        and load, YMMV.

Example use:

    from obstechutils.precise_timing import periodic_call

    @periodic_call(
        interval=30, initial_delay=1,
        loop_condition: lambda res, n: n <= 10
    )
    def f():
        ... 

    if __name__ == "__main__":
        # operation to be repeated every 30s exactly 10 times at times 
        #    t = time.time() + 1 + 30 * n
        # with an offset and variance of tens of microseconds depending 
        # on machine and CPU load
        f()                          

"""
    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kwargs):

            fname = f.__name__
            logger = logging.getLogger('obstechutils')
            logger.info(f'{fname} periodic call every {interval:.4f} s')
          
            n = 0
            t0 = time.time()
            t_target = t0 + initial_delay 

            while True:

                while (remaining := t_target - time.time()) >= sleep_overhead:
                    time.sleep(remaining * sleep_fraction)

                res = f(*args,**kwargs)
                n += 1
                logger.debug(f'{fname} call #{n} dt={-remaining*1e6:.3f} μs')

                if not loop_condition(res, n):
                    break
                t_target = t0 + initial_delay + n * interval 

        if not threaded:
            return wrapper
           
        @wraps(wrapper) 
        def threaded_wrapper(*args, **kwargs):
            t = threading.Thread(
                    target=wrapper, args=args, kwargs=kwargs,
                    daemon=True
            )
            t.start()

        return threaded_wrapper

    if fun:
        return decorator(fun)
    
    return decorator
