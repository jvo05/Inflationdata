def main(x, y):
    from matplotlib import pyplot as plt

    plt.rcParams["figure.figsize"] = [10.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    
    default_x_ticks = range(len(x))
    plt.plot(default_x_ticks, y)
    plt.xticks(default_x_ticks, x)

    plt.xlabel("Jahr")
    plt.ylabel("CPI / Consumer Price Index")

    plt.show()