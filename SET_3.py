import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

colors = {
    0: "green",
    1: "red",
    2: "purple"
}
number = {
    0: 1,
    1: 2,
    2: 3
}
shape = {
    0: "squiggle",
    1: "diamond",
    2: "oval"
}
shading = {
    0: "filled",
    1: "empty",
    2: "shaded"
}


def generate_cards():
    cards = [[0]*9 for i in range(9)]
    i = 0
    j = 0
    for color in range(3):
        for shape in range(3):
            for number in range(3):
                for shade in range(3):
                    card = [color,shape,number,shade]
                    cards[i][j] = card
                    i += 1
            i = 0
            j += 1
    return cards


def show_images(cards):
    f, axarr = plt.subplots(9, 9)
    for i in range(9):
        for j in range(9):
            image_datas = ("img//" + str(colors[cards[i][j][0]]) + str(shape[cards[i][j][1]])
                           + str(shading[cards[i][j][3]]) + str(number[cards[i][j][2]]) + ".png")
            axarr[i][j].imshow(mpimg.imread(image_datas))
            axarr[i][j].axis("off")
    plt.show()


def main():
    #random.seed(123)
    cards = generate_cards()
    show_images(cards)


if __name__ == "__main__":
    main()
