def plotAccuracy(train, test):
    import matplotlib as plt

    minplot = min(min(train), min(test))

    plt.plot(train)
    plt.plot(test)
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.ylim(minplot, 1.0)
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.savefig('/accuracy.png')  # change later to use Files
    plt.show()

def plotLoss(train, test):
    import matplotlib as plt

    plt.plot(train)
    plt.plot(test)
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.ylim(10**-1.5, 10**3)
    plt.yscale('log')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.savefig('data/loss.png')  # Change later to Files
    plt.show()