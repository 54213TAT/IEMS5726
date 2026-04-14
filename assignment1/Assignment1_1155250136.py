# 1155250136 Cheng Haotian
import numpy as np
import pandas as pd
from scipy.stats import chisquare, wilcoxon, ttest_rel

# Problem 2
def problem_2(df):
    row_mean = row_sd = column_sample_mean = column_ss = 0

    row_mean = df.mean(axis=1)
    row_sd = df.std(axis=1, ddof=1)
    column_sample_mean = df.mean(axis=0)
    column_ss = df.std(axis=0, ddof=1) / np.sqrt(df.shape[0])

    return row_mean, row_sd, column_sample_mean, column_ss

# Problem 3
def problem_3(list_of_observation):
    p = chi2 = 0
    #special_die = [1, 1, 2, 3, 4, 4]
    sum_results = {2:4, 3:4, 4:5, 5:10, 6:5, 7:4, 8:4}
    theoretical_prob = [sum_results[i]/36 for i in range(2,9)]

    obs_counts = [list_of_observation.count(i) for i in range(2,9)]
    exp_counts = [theoretical_prob[i-2]*len(list_of_observation) for i in range(2,9)]

    chi2, p = chisquare(obs_counts, exp_counts)

    return p, chi2

# Problem 4
def problem_4(df):
    pairt = w = 0

    column1 = df.iloc[:,0]
    column2 = df.iloc[:,1]

    _, pairt = ttest_rel(column1, column2)
    _, w = wilcoxon(column1, column2)

    return pairt, w


if __name__ == "__main__":
    # Testing: Problem 2
    df = pd.read_csv('problem2.csv', sep=',', header=None)
    print(problem_2(df))


    # Testing: Problem 3
    observation = [3,5,3,6,7,8,3,5,5,2,4,4,5,2,8,7,5,5,5,3]
    p, chi2 = problem_3(observation)
    print("p-value :", p)
    print("chi-square :", chi2)
    
    
    # Testing: Problem 4
    df = pd.read_csv('problem4.csv', sep=',', header=None)
    pairt, w = problem_4(df)
    print("p-value from paired sample T-test: ", pairt)
    print("p-value from wilcoxon signed-ranked test with T-statistics: ", w)

