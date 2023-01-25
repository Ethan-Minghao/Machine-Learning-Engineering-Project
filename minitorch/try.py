import minitorch

if __name__ == "__main__":
    a = [
        [
            [-100.00, -0.00, -1.10, 100.00],
            [-0.00, -0.00, 0.33, -0.00],
            [5.27, -0.00, 100.00, 100.00],
        ],
        [
            [0.00, -0.00, 51.81, 0.00],
            [-45.13, 1.00, 0.00, -100.00],
            [-0.00, 1.50, 0.00, -0.00],
        ],
    ]
    print(minitorch.tensor(a))
    print(minitorch.tensor(a).shape)
    print(minitorch.max(minitorch.tensor(a), 0))
    print(max(minitorch.tensor(a)[i, 0, 0] for i in range(2)))
    b = [1, 2, 3, 4, 5]
    print(max(b[i] for i in range(3)))
