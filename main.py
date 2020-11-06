import pygame
import random
import re

pygame.init()
icon = pygame.image.load("Dependencies/hangman.png")
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hangman")
pygame.display.set_icon(icon)


words_txt = open("Dependencies/nouns.txt", "r")
words = words_txt.readlines()
words_txt.close()

mine = pygame.font.Font('Dependencies/big.ttf', 35)
smaller = pygame.font.Font('Dependencies/big.ttf', 30)
go_font = pygame.font.Font('Dependencies/big.ttf', 80)
vowel_font = pygame.font.Font('Dependencies/big.ttf', 40)
pa = pygame.font.Font('Dependencies/big.ttf', 50)
row1 = [['Q', [0, 0, 0], False], ['W', [0, 0, 0], False], ['E', [0, 0, 0], False], ['R', [0, 0, 0], False],
        ['T', [0, 0, 0], False], ['Y', [0, 0, 0], False], ['U', [0, 0, 0], False], ['I', [0, 0, 0], False],
        ['O', [0, 0, 0], False], ['P', [0, 0, 0], False]]
row2 = [['A', [0, 0, 0], False], ['S', [0, 0, 0], False], ['D', [0, 0, 0], False], ['F', [0, 0, 0], False],
        ['G', [0, 0, 0], False], ['H', [0, 0, 0], False], ['J', [0, 0, 0], False], ['K', [0, 0, 0], False],
        ['L', [0, 0, 0], False]]
row3 = [['Z', [0, 0, 0], False], ['X', [0, 0, 0], False], ['C', [0, 0, 0], False], ['V', [0, 0, 0], False],
        ['B', [0, 0, 0], False], ['N', [0, 0, 0], False], ['M', [0, 0, 0], False]]


guesses = 0
correct = 0
word = words[random.randint(1, 599)]
ans_w = ""
for u in word:
    if u.isalpha():
        ans_w += u
num_of_vowels = 0
for l in word:
    if l in "aeiouAEIOU":
        num_of_vowels += 1
print(word)

start = (800 - (len(word) * 20))//2


def word_guess():
    for s in range(start, 800-start-20, 20):
        pygame.draw.line(screen, (0, 0, 0), (s+8, 400), (s + 20, 400), 4)


def show_ch(to_show):
    for n in range(3):
        if to_show[1][n]:
            ch = smaller.render(to_show[0], True, (0, 0, 0))
            screen.blit(ch, (to_show[1][n], 370))


def guess(c):
    global guesses, correct
    c[0] = c[0].lower()
    wo = word.lower()
    res = wo.find(c[0])
    if res == -1:
        guesses += 1
    else:
        se = word.lower()
        matches = [m.start() for m in re.finditer(c[0], se)]
        j = 0
        for match in matches:
            correct += 1
            pos = start + 20 * match
            pos += 8
            if c[0] == 'i':
                pos += 3
            elif c[0] == 'f' or c[0] == 'e' or c[0] == 'l':
                pos += 2
            elif c[0] == 'w':
                pos -= 2
            elif c[0] == 't':
                pos += 1
            c[1][j] = pos
            j += 1
        show_ch(c)


def game_over():
    txt = go_font.render("Game Over", True, (0, 0, 0))
    ans = pa.render("Word was " + ans_w, True, (0, 0, 0))
    play = pa.render("Press enter to play again!", True, (0, 0, 0))
    screen.blit(txt, (250, 100))
    screen.blit(ans, (250, 200))
    screen.blit(play, (190, 300))


def win():
    txt = go_font.render("You Win!", True, (0, 0, 0))
    play = pa.render("Press enter to play again!", True, (0, 0, 0))
    screen.blit(txt, (250, 200))
    screen.blit(play, (190, 300))


def vowel_display():
    vow = vowel_font.render("Vowels: " + str(num_of_vowels), True, (0, 0, 0))
    screen.blit(vow, (80, 150))


steps = []
for i in range(7):
    name = "Dependencies/base" + str(i) + ".png"
    steps.append(pygame.image.load(name))
hint = False
winn = False
go = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (winn or go):
            correct = 0
            winn = False
            go = False
            hint = False
            guesses = 0
            word = words[random.randint(0, 49)]
            ans_w = ""
            for u in word:
                if u.isalpha():
                    ans_w += u
            num_of_vowels = 0
            for l in word:
                if l in "aeiouAEIOU":
                    num_of_vowels += 1
            start = (800 - (len(word) * 20)) // 2
            print(word)
            row1 = [['Q', [0, 0, 0], False], ['W', [0, 0, 0], False], ['E', [0, 0, 0], False], ['R', [0, 0, 0], False],
                    ['T', [0, 0, 0], False], ['Y', [0, 0, 0], False], ['U', [0, 0, 0], False], ['I', [0, 0, 0], False],
                    ['O', [0, 0, 0], False], ['P', [0, 0, 0], False]]
            row2 = [['A', [0, 0, 0], False], ['S', [0, 0, 0], False], ['D', [0, 0, 0], False], ['F', [0, 0, 0], False],
                    ['G', [0, 0, 0], False], ['H', [0, 0, 0], False], ['J', [0, 0, 0], False], ['K', [0, 0, 0], False],
                    ['L', [0, 0, 0], False]]
            row3 = [['Z', [0, 0, 0], False], ['X', [0, 0, 0], False], ['C', [0, 0, 0], False], ['V', [0, 0, 0], False],
                    ['B', [0, 0, 0], False], ['N', [0, 0, 0], False], ['M', [0, 0, 0], False]]

    screen.fill((255, 255, 255))
    screen.blit(steps[guesses], (0, 0))

    if guesses == 6:
        go = True
        game_over()
    elif correct == len(word)-1:
        win()
        winn = True
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    word_guess()
    if hint:
        vowel_display()
    else:
        hi = vowel_font.render("HINT", True, (0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (80, 150, 75, 45))
        if 82 + 71 > mouse[0] > 82 and 152 + 42 > mouse[1] > 152:
            pygame.draw.rect(screen, (0, 205, 255), (82, 152, 71, 42))
            if click[0] and not go:
                hint = True
        else:
            pygame.draw.rect(screen, (255, 255, 255), (82, 152, 71, 42))
        screen.blit(hi, (90, 151))

    x = 0
    for i in range(175, 625, 45):
        tr = mine.render(row1[x][0], True, (0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (i, 440, 45, 45))
        if row1[x][2]:
            pygame.draw.rect(screen, (87, 87, 87), (i + 2, 442, 42, 42))
            show_ch(row1[x])
        else:
            if i + 45 > mouse[0] > i and 442 + 45 > mouse[1] > 442:
                pygame.draw.rect(screen, (0, 205, 255), (i + 2, 442, 42, 42))
                if click[0] and not go and not winn:
                    row1[x][2] = True
                    guess(row1[x])
            else:
                pygame.draw.rect(screen, (255, 255, 255), (i+2, 442, 42, 42))
        screen.blit(tr, (i+16, 443))
        x += 1

    x = 0
    for i in range(190, 595, 45):
        tr = mine.render(row2[x][0], True, (0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (i, 488, 45, 45))
        if row2[x][2]:
            pygame.draw.rect(screen, (87, 87, 87), (i + 2, 490, 42, 42))
            show_ch(row2[x])
        else:
            if i + 45 > mouse[0] > i and 490 + 45 > mouse[1] > 490:
                pygame.draw.rect(screen, (0, 205, 255), (i + 2, 490, 42, 42))
                if click[0] and not go and not winn:
                    row2[x][2] = True
                    guess(row2[x])
            else:
                pygame.draw.rect(screen, (255, 255, 255), (i + 2, 490, 42, 42))
        screen.blit(tr, (i + 17, 493))
        x += 1

    x = 0
    for i in range(215, 530, 45):
        tr = mine.render(row3[x][0], True, (0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (i, 536, 45, 45))
        if row3[x][2]:
            pygame.draw.rect(screen, (87, 87, 87), (i + 2, 538, 42, 42))
            show_ch(row3[x])
        else:
            if i + 45 > mouse[0] > i and 538 + 45 > mouse[1] > 538:
                pygame.draw.rect(screen, (0, 205, 255), (i + 2, 538, 42, 42))
                if click[0] and not go and not winn:
                    row3[x][2] = True
                    guess(row3[x])
            else:
                pygame.draw.rect(screen, (255, 255, 255), (i + 2, 538, 42, 42))
        screen.blit(tr, (i + 17, 538))
        x += 1
    pygame.display.update()
