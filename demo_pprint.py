if __name__ == '__main__':
    import time
    import sys
    import numpy as np
    from stackprinter import format


    def bump():
        print('creating crazy data structures.')
        boing = {k:np.ones((100,100)) for k in range(int(2e4))}
        print('.')
        somelist = [1,2,3,boing, boing, 4,5,6,7,8,9] * int(1e5)
        print('done.')

        somedict = {'various': 'excellent',
                             123: 'things',
                             'in': np.ones((42,23)),
                             'a list': somelist}
        sometuple = (1,2, somedict, np.ones((32,64)), boing)
        somedict['recursion'] = somedict
        raise Exception()


    try:
        bump()
    except:
        stuff = sys.exc_info()
        scopidoped = 'gotcha'
        tic = time.perf_counter()

        msg = format(stuff, style='color', show_vals='all', reverse=False, truncate_vals=250, suppressed_paths=["site-packages"])

        took = time.perf_counter() - tic
        print(msg)
        print('took %.1fms' % (took * 1000))
