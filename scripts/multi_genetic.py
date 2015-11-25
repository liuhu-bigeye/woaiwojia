from multiprocessing import Pool
import os

def genetic_one(index):
  if index%2 == 0:
        sys_str='python genetic_price.py 2000 0.6 0.6 500 2>&1 > .liuqcprice.out%04d &'%index
  else:
        sys_str='python genetic_period.py 2000 0.6 0.6 500 2>&1 > .liuqcperiod.out%04d &'%index
  os.system(sys_str)

if __name__ == '__main__':
    pool = Pool(processes=10)
    num = 10
    result = pool.map(genetic_one, range(num))
    print 'before close'
    pool.close()
    print 'before join'
    pool.join()
    print 'before exit'
