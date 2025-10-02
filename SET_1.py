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


def random_cards():
    card_1 = [0, 0, 0, 0]
    card_2 = [0, 0, 0, 0]
    while card_1 == card_2:
        for i in range(4):
            card_1[i] = random.randint(0, 2)
            card_2[i] = random.randint(0, 2)
    return card_1, card_2


def print_card(karta):
    print("Card:")
    print(f"- color: {colors[karta[0]]}")
    print(f"- shape: {shape[karta[1]]}")
    print(f"- number: {number[karta[2]]}")
    print(f"- shading: {shading[karta[3]]}")
    print()


def find_set(card_1, card_2):
    card_3 = [0, 0, 0, 0]
    for i in range(4):
        card_3[i] = (3 - card_1[i] - card_2[i]) % 3
    return card_3


def show_images(cards):
    f, axarr = plt.subplots(1, 3)
    image_datas = [0, 0, 0]
    for i in range(3):
        image_datas[i] = ("img//" + str(colors[cards[i][0]])
                          + str(shape[cards[i][1]]) + str(shading[cards[i][3]])
                          + str(number[cards[i][2]]) + ".png")
        axarr[i].imshow(mpimg.imread(image_datas[i]))
        axarr[i].axis("off")
    plt.show()


def main():
    #random.seed(123)
    card_1, card_2 = random_cards()
    print("Two random cards:")
    print_card(card_1)
    print_card(card_2)
    card_3 = find_set(card_1, card_2)
    print("Card that creates a SET:")
    print_card(card_3)
    cards = [card_1, card_2, card_3]
    show_images(cards)


if __name__ == "__main__":
    main()
