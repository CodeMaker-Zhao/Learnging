import random
import math
import numpy as np
import matplotlib.pyplot as plt

class PSO:
    def __init__(self,times,size,num_min,num_max):
        self.times = times #迭代次数
        self.popu_size = size #种群数量
        self.var_nums = len(num_min) #变量个数
        self.bound = [num_min,num_max] #变量的边界

        self.popu_x = np.zeros((self.popu_size, self.var_nums)) #存储每个粒子的位置
        self.popu_v = np.zeros((self.popu_size, self.var_nums)) #存储每个粒子的速度
        self.p_best = np.zeros((self.popu_size,self.var_nums)) #存储粒子自身最优值的位置
        self.g_best = np.zeros((1,self.var_nums)) #存储整体最优值

        temp = 0
        for i in range(self.popu_size):
            for j in range(self.var_nums):
                self.popu_x[i][j] = random.uniform(self.bound[0][j],self.bound[1][j])
                self.popu_v[i][j] = random.uniform(0,1)
            self.p_best[i] = self.popu_x[i]
            fit = self.fitness(self.p_best[i])
            if fit > temp:
                self.g_best = self.p_best[i]
                temp = fit

    def fitness(self, inp_var):
        x1 = inp_var[0]
        x2 = inp_var[1]
        y = math.sin(x2)*np.pi*x1**3 - math.cos(x1)*x2**4
        return y
    
    def update(self, popu_size):
        c1 = 2
        c2 = 2
        w = 0.4
        for i in range(popu_size):
            #更新速度
            self.popu_v[i] = w*self.popu_v[i] + c1*random.uniform(0,1)*(self.p_best[i] - self.popu_x[i]) + c2*random.uniform(0,1)*(self.g_best - self.popu_x[i])
            #更新位置
            self.popu_x[i] = self.popu_x[i] + self.popu_v[i]
            #边界限制
            for j in range(self.var_nums):
                if self.popu_x[i][j] < self.bound[0][j]:
                    self.popu_x[i][j] = self.bound[0][j]
                if self.popu_x[i][j] > self.bound[1][j]:
                    self.popu_x[i][j] = self.bound[1][j]
            if self.fitness(self.popu_x[i]) > self.fitness(self.p_best[i]):
                self.p_best[i] = self.popu_x[i]
            if self.fitness(self.popu_x[i]) > self.fitness(self.g_best):
                self.g_best = self.popu_x[i].copy()

    def main(self):
        recordobj = []
        for gen in range(self.times):
            self.update(self.popu_size)
            recordobj.append(self.fitness(self.g_best))
            print('############ Generation {} ############'.format(str(gen + 1)))
            print('最好的位置：{0[0]:.2f}  {0[1]:.2f}'.format(self.g_best))
            print('最大的函数值：{:.2f}'.format(self.fitness(self.g_best)))
        print("---- End of (successful) Searching ----")

        plt.figure()
        plt.title("Figure1")
        plt.xlabel("iterators", size=14)
        plt.ylabel("fitness", size=14)
        t = [t for t in range(self.times)]
        plt.plot(t, recordobj, color='b', linewidth=2)
        plt.show()


if __name__ == '__main__':
    times = 100
    popsize = 100
    low = [1, 1]
    up = [30, 30]
    pso = PSO(times, popsize, low, up)
    pso.main()
