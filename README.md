## Agent Orange: Pseudo-Fuzz Defoliator


### About:
tl;dr Uniform Fuzz Distribution

In Anki 2.1, a constrain was put in to the scheduler to prevent the next interval from getting smaller than the previous interval after fuzz. This applies to both V1 and V2. The constrain is applied AFTER randomization. This changes the statistics so that smaller intervals have a higher probability of being chosen. The result is 100% organic ease hell.

For the test below, each test is ran in a loop 10k times. The probability of hitting the lower intervals for young/fresh cards are 20-60% higher than the upper intervals. For V2, at intervals below 5, it results in 100% organic defuzz. While other intervals are skewed much worst than V1.

This addon ensures a uniform distribution so that all given intervals have the same probability of being chosen.


### Probability Distribution Test:

```
### V1 #############

>>> test_distribution_probability(ivl=1,ef=1300,grade=2)
2: 50.80%
3: 49.20%

>>> test_distribution_probability(ivl=2,ef=1300,grade=2)
3: 66.17%
4: 33.83%

>>> test_distribution_probability(ivl=5,ef=1300,grade=2)
6: 66.17%
7: 33.83%

>>> test_distribution_probability(ivl=6,ef=1300,grade=2)
7: 59.40%
8: 20.23%
9: 20.37%

>>> test_distribution_probability(ivl=9,ef=1300,grade=2)
10: 59.16%
12: 20.36%
11: 20.48%

>>> test_distribution_probability(ivl=14,ef=1300,grade=2)
15: 39.25%
16: 20.10%
17: 20.36%
18: 20.29%


>>> test_distribution_probability(ivl=1,ef=1300,grade=3)
3: 32.72%
2: 33.93%
4: 33.35%

>>> test_distribution_probability(ivl=5,ef=1300,grade=3)
6: 39.30%
7: 20.05%
8: 20.30%
9: 20.35%

>>> test_distribution_probability(ivl=9,ef=1300,grade=3)
10: 40.06%
11: 19.66%
12: 19.62%
13: 20.66%


### V2 #############
>>> test_distribution_probability(ivl=5,ef=1300,grade=2)
6: 66.42%
7: 33.58%

>>> test_distribution_probability(ivl=5,ef=1300,grade=3)
7: 67.09%
8: 32.91%

>>> test_distribution_probability(ivl=9,ef=1300,grade=2)
10: 59.77%
11: 20.45%
12: 19.78%

>>> test_distribution_probability(ivl=9,ef=1300,grade=3)
11: 35.97%
12: 27.98%
13: 36.05%

>>> test_distribution_probability(ivl=9,ef=1300,grade=3)
11: 36.98%
12: 27.58%
13: 35.44%

>>> test_distribution_probability(ivl=12,ef=1300,grade=3)
14: 15.89%
15: 20.06%
16: 27.92%
17: 36.13%

>>> test_distribution_probability(ivl=12,ef=1300,grade=3)
14: 15.71%
15: 19.95%
16: 27.86%
17: 36.48%

>>> test_distribution_probability(ivl=12,ef=1300,grade=2)
13: 39.85%
14: 20.42%
15: 19.93%
16: 19.80%


########################################

### 2.0 or with this addon #############

>>> test_distribution_probability(ivl=5,ef=1300,grade=2)
5: 33.00%
6: 33.00%
7: 33.00%

>>> test_distribution_probability(ivl=9,ef=1300,grade=2)
8: 20.00%
9: 20.00%
10: 19.00%
11: 20.00%
12: 20.00%

>>> test_distribution_probability(ivl=15,ef=1300,grade=2)
16: 20.00%
17: 19.00%
18: 19.00%
19: 20.00%
20: 19.00%

>>> test_distribution_probability(ivl=3,ef=2500,grade=2)
3: 32.00%
4: 33.00%
5: 33.00%

>>> test_distribution_probability(ivl=5,ef=1300,grade=2)
5: 32.00%
6: 33.00%
7: 33.00%

>>> test_distribution_probability(ivl=3,ef=2500,grade=3)
5: 19.00%
6: 20.00%
7: 19.00%
8: 19.00%
9: 20.00%

>>> test_distribution_probability(ivl=5,ef=2500,grade=3)
10: 19.00%
11: 19.00%
12: 20.00%
13: 19.00%
14: 20.00%

```

### Future development:
This project maybe merged with DeFuzz in a future date. For now, I will leave it separated as the bulky documentation maybe confusing to new users.
