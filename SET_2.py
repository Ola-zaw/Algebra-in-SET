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


def check_set(cards):
    for i in range(4):
        if (cards[0][i] + cards[1][i] + cards[2][i]) % 3 != 0:
            return False
    return True


def random_cards():
    card_1 = [0, 0, 0, 0]
    card_2 = [0, 0, 0, 0]
    card_3 = [0, 0, 0, 0]
    cards = [card_1, card_2, card_3]
    while (card_1 == card_2) or (card_1 == card_3) or (card_2 == card_3) or check_set(cards):
        for i in range(4):
            card_1[i] = random.randint(0, 2)
            card_2[i] = random.randint(0, 2)
            card_3[i] = random.randint(0, 2)
    return cards


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
    f, axarr = plt.subplots(3, 3)
    for i in range(3):
        for j in range(3):
            image_datas = ("img//" + str(colors[cards[i][j][0]]) + str(shape[cards[i][j][1]])
                           + str(shading[cards[i][j][3]]) + str(number[cards[i][j][2]]) + ".png")
            axarr[i][j].imshow(mpimg.imread(image_datas))
            axarr[i][j].axis("off")
    plt.show()


def find_plane(cards):
    plane = [[0]*3 for i in range(3)]
    plane[0][0] = cards[0]
    plane[0][1] = cards[1]
    plane[0][2] = find_set(cards[0], cards[1])
    plane[1][0] = cards[2]
    plane[2][0] = find_set(cards[0], cards[2])
    plane[2][2] = find_set(cards[1], cards[2])
    plane[1][1] = find_set(cards[0], plane[2][2])
    plane[1][2] = find_set(cards[1], plane[2][0])
    plane[2][1] = find_set(cards[2], plane[0][2])
    return plane


def main():
    #random.seed(123)
    cards = random_cards()
    print("Three random cards:")
    print_card(cards[0])
    print_card(cards[1])
    print_card(cards[2])
    plane = find_plane(cards)
    print("Plane:")
    for i in range(3):
        for j in range(3):
            print_card(plane[i][j])
    show_images(plane)


if __name__ == "__main__":
    main()
