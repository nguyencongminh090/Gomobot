import pyautogui


def inits(distance, a1, a2, b1, b2):
    global diz
    global a, z, c, d
    diz = distance
    a, z, c, d = [int(a1), int(a2), int(b1), int(b2)]
    print('Config:', a, z, c, d)

def get_opening():
    pic = pyautogui.screenshot(region=(a, z, c + 20, d + 20))
    pic.save('Opening.png')
    lst = []
    lta = []
    coord_b = ''
    coord_w = ''
    for i in range(0, 15):
        for j in range(0, 15):
            r, g, b = pic.getpixel((round(i * diz), round(j * diz)))
            if r == 40 and g == 40 and b == 40:
                lst.append((round(i*diz) + a, round(j*diz) + z))
            elif r == 255:
                rbg = pic.getpixel((round(i*diz) + 7, round(j*diz) + 7))
                if rbg == (40, 40, 40):
                    coord_b = (round(i*diz) + a, round(j*diz) + z)
    for i in range(0, 15):
        for j in range(0, 15):
            r, g, b = pic.getpixel((round(i*diz), round(j*diz)))
            if r == 243 and g == 243 and b == 243:
                lta.append((round(i*diz) + a, round(j*diz) + z))
            elif r == 255:
                rbg = pic.getpixel((round(i*diz) + 7, round(j*diz) + 7))
                if rbg == (243, 243, 243):
                    coord_w = (round(i*diz) + a, round(j*diz) + z)
    if coord_b != '':
        lst.append(coord_b)
    if coord_w != '':
        lta.append(coord_w)
    return lst, lta


def opening():
    opens = get_opening()
    black = opens[0]
    white = opens[1]
    output = []

    for i in range(len(max(black, white)) * 2):
        try:
            output.append(black[i])
            output.append(white[i])
        except:
            break

    print('Output:', output)
    return output


def test():
    pic = pyautogui.screenshot(region=(a, z, c + 20, d + 20))
    pic.save('Opening.png')
    for i in range(0, 15):
        for j in range(0, 15):
            pyautogui.moveTo(round(i*diz) + a, round(j*diz) + z)
    pass