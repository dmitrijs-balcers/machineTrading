import numpy as np


# 2d array
# np.array([(2, 3, 4), (5, 6, 7)])
# By default floating point is used.
# Can assign int to be generated:
# np.ones((5, 4), dtype=np.int8)


def test_run():
    print "{{test_run}}"
    print np.empty(5)
    print np.ones((5, 4), dtype=np.int8)
    print np.random.rand(5, 4)
    # Simple numbers from a Gaussian (normal) distribution
    # "standard normal" (mean = 50, standard deviation = 10),
    # mean means "around 50"
    print np.random.normal(50, 10, size=(2, 3))
    print np.random.randint(0, 10, size=5)

    array_attributes(np.random.random((5, 4)))
    operations()
    performance()


def array_attributes(a):
    print "{{array_attributes}}"
    print a.shape
    print a.shape[0]
    print a.shape[1]
    print len(a.shape)
    print a.size


def operations():
    np.random.seed(693)  # Will give the same output every-time
    a = np.random.randint(0, 10, size=(5, 4))
    print "Array:\n", a
    print "Sum of all elements: ", a.sum()
    print "Sum of each column: \n", a.sum(axis=0)
    print "Sum of each row: \n", a.sum(axis=1)

    print "Minimum of each column: \n", a.min(axis=0)
    print "Minimum of each row: \n", a.min(axis=1)
    print "Mean of all elements:", a.mean()


if __name__ == "__main__":
    test_run()