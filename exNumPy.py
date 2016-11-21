import numpy as np

# 2d array
# np.array([(2, 3, 4), (5, 6, 7)])
# By default floating point is used.
# Can assign int to be generated:
# np.ones((5, 4), dtype=np.int8)


def test_run():
    print np.empty(5)
    print np.ones((5, 4), dtype=np.int8)
    print np.random.rand(5, 4)
    # Simple numbers from a Gaussian (normal) distribution
    # "standard normal" (mean = 50, standard deviation = 10),
    # mean means "around 50"
    print np.random.normal(50, 10, size=(2, 3))
    print np.random.randint(0, 10, size=5)


if __name__ == "__main__":
    test_run()