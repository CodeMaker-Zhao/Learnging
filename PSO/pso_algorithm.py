import matplotlib.pyplot as plt
import numpy as np
import math
import random

class PSO:
    def __init__(self, iterations, popu_size, lows, highs):
        #设置迭代次数、种群数量、自变量、边界
        self.iterations = iterations
        self.popu_size = popu_size
        self.var_nums = len(lows)
        self.bound = [lows, highs]

        #设置个体位置、个体速度、个体最优位置、种群最优位置
        self.popu_x = np.zeros((self.popu_size, self.var_nums))
        self.popu_v = np.zeros((self.popu_size, self.var_nums))
        self.p_best = np.zeros((self.popu_size, self.var_nums))
        self.g_best = np.zeros((1,self.var_nums))

        temp = 0
        for i in range(self.popu_size):
            for j in range(self.var_nums):
                self.popu_x[i][j] = random.uniform(self.bound[0][j],self.bound[1][j])
                self.popu_v[i][j] = random.uniform(-1,1)
            self.p_best[i] = self.popu_x[i].copy()
            fit = self.fitness(self.popu_x[i])
            if fit>temp:
                self.g_best = self.popu_x[i].copy()
                temp = self.fitness(self.popu_x[i])
    
    def fitness(self,inp_var):
        x1 = inp_var[0]
        x2 = inp_var[1]
        y =(1+np.cos(12*(x1**2+x2**2)**0.5))/(.5*(x1**2+x2**2)+2)
        return y

    def update(self):
        w = 0.8
        c1 = 2
        c2 = 2
        for i in range(self.popu_size):
            self.popu_v[i] = w*self.popu_v[i] + c1*(self.p_best[i] - self.popu_x[i]) + c2*(self.g_best - self.popu_x[i])
            self.popu_x[i] = self.popu_x[i] + self.popu_v[i]
            for j in range(self.var_nums):
                self.popu_x[i][j] = self.bound[0][j] if self.popu_x[i][j] < self.bound[0][j] else self.popu_x[i][j]
                self.popu_x[i][j] = self.bound[1][j] if self.popu_x[i][j] > self.bound[1][j] else self.popu_x[i][j]
            self.p_best[i] = self.popu_x[i].copy() if self.fitness(self.popu_x[i]) > self.fitness(self.p_best[i]) else self.p_best[i]
            self.g_best = self.popu_x[i].copy() if self.fitness(self.popu_x[i]) > self.fitness(self.g_best) else self.g_best

    def main(self):
        recordobj = []
        for gen in range(self.iterations):
            self.update()
            recordobj.append(self.fitness(self.g_best))
            print('############ Generation {} ############'.format(str(gen + 1)))
            print('最好的位置：{0[0]:.2f}  {0[1]:.2f}'.format(self.g_best))
            print('最大的函数值：{:.2f}'.format(self.fitness(self.g_best)))
        print("---- End of (successful) Searching ----")
        plt.figure()
        plt.title("Figure1")
        plt.xlabel("iterators", size=14)
        plt.ylabel("fitness", size=14)
        t = [t for t in range(self.iterations)]
        plt.plot(t, recordobj, color='b', linewidth=2)
        plt.show()


if __name__ == '__main__':
    times = 500
    popsize = 100
    low = [-10, -10]
    up = [10, 10]
    pso = PSO(times, popsize, low, up)
    pso.main()
