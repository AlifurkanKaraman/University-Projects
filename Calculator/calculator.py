from graphics import *

def multi1(integers, strings):
    try:
        sums_mul = integers * int(strings)
        inputText.setText(sums_mul)
        strings = str(sums_mul)
        return strings
    except ValueError:
        inputText.setText('0')
        strings = ''
        return strings

def addition1(integers, strings):
    try:
        sums_a = integers + int(strings)
        inputText.setText(sums_a)
        strings = str(sums_a)
        return strings
    except ValueError:
        inputText.setText('0')
        strings = ''
        return strings

def sub1(integers, strings):
    try:
        sums_s = integers - int(strings)
        inputText.setText(sums_s)
        strings = str(sums_s)
        return strings
    except ValueError:
        inputText.setText('0')
        strings = ''
        return strings

def division1(integers, strings):
    try:
        sums_d = integers / int(strings)
        if integers % int(strings) == 0:
            inputText.setText(int(sums_d))
        else:
            inputText.setText(sums_d)
        strings = str(sums_d)
        return strings
    except ZeroDivisionError:
        inputText.setText('0')
        strings = ''
        return strings
def exponention1(integers, strings):
    try:
        sums_e = (integers)**(int(strings))
        inputText.setText(sums_e)
        strings = str(sums_e)
        return strings
    except ValueError:
        inputText.setText('0')
        strings = ''
        return strings

def modulus1(integers, strings):
    try:
        sums_m = integers % int(strings)
        inputText.setText(sums_m)
        strings = str(sums_m)
        return strings
    except ZeroDivisionError:
        inputText.setText('0')
        strings = ''
        return  strings

win = GraphWin("Calculator", 600, 600)
Text(Point(300, 10), 'Calculator').draw(win)
rec1 = Rectangle(Point(0, 100), Point(150, 200)).draw(win)
Text(Point(75, 150), "AC").draw(win)
rec2 = Rectangle(Point(0, 100), Point(150, 300)).draw(win)
Text(Point(75, 250), "7").draw(win)
rec3 = Rectangle(Point(0, 100), Point(150, 400)).draw(win)
Text(Point(75, 350), "4").draw(win)
rec4 = Rectangle(Point(0, 100), Point(150, 500)).draw(win)
Text(Point(75, 450), "1").draw(win)
rec5 = Rectangle(Point(0, 100), Point(300, 200)).draw(win)
Text(Point(150, 550), "0").draw(win)
rec6 = Rectangle(Point(150, 100), Point(300, 200)).draw(win)
Text(Point(225, 150), "+/-").draw(win)
rec7 = Rectangle(Point(150, 100), Point(300, 300)).draw(win)
Text(Point(225, 250), "8").draw(win)
rec8 = Rectangle(Point(150, 100), Point(300, 400)).draw(win)
Text(Point(225, 350), "5").draw(win)
rec9 = Rectangle(Point(150, 100), Point(300, 500)).draw(win)
Text(Point(225, 450), "2").draw(win)
rec10 = Rectangle(Point(300, 100), Point(450, 200)).draw(win)
rec11 = Rectangle(Point(300, 100), Point(450, 300)).draw(win)
Text(Point(375, 150), "%").draw(win)
rec12 = Rectangle(Point(300, 100), Point(450, 400)).draw(win)
Text(Point(375, 250), "9").draw(win)
rec13 = Rectangle(Point(300, 100), Point(450, 500)).draw(win)
Text(Point(375, 350), "6").draw(win)
rec14 = Rectangle(Point(300, 100), Point(450, 600)).draw(win)
Text(Point(375, 450), "3").draw(win)
rec15 = Rectangle(Point(450, 100), Point(600, 200)).draw(win)
Text(Point(375, 550), "**").draw(win)
rec16 = Rectangle(Point(450, 100), Point(600, 300)).draw(win)
Text(Point(525, 150), "/").draw(win)
rec17 = Rectangle(Point(450, 100), Point(600, 400)).draw(win)
Text(Point(525, 250), "x").draw(win)
rec18 = Rectangle(Point(450, 100), Point(600, 500)).draw(win)
Text(Point(525, 350), "-").draw(win)
rec19 = Rectangle(Point(450, 100), Point(600, 600)).draw(win)
Text(Point(525, 450), "+").draw(win)
rec20 = Rectangle(Point(450, 100), Point(600, 700)).draw(win)
Text(Point(525, 550), "=").draw(win)
inputText = Entry(Point(300, 55), 20)
inputText.setText('0')
inputText.draw(win)
sums_m= 0
sums_e = 0
sums_d = 0
sums_mul = 0
sums_s = 0
sums_a = 0
integers = 0
strings = ''
modulus = False
division = False
multi = False
sub = False
addition = False
exponention = False
equal = False

while True:
    try:
        x = win.getMouse()
    except GraphicsError:
        win.close()
        break
    if x.x > 0 and x.x < 150 and x.y > 100 and x.y < 200:
        inputText.setText('0')
        strings = ''
        modulus = False
        division = False
        multi = False
        sub = False
        addition = False
        exponention = False
        equal = False
    elif x.x > 0 and x.x < 150 and x.y > 100 and x.y < 300:
        if equal:
            inputText.setText('0')
            equal = False
            strings = ''
        else:
            # inputText.setText('7')
            strings += '7'
            inputText.setText(strings)
    elif x.x > 0 and x.x < 150 and x.y > 100 and x.y < 400:
        if equal:
            inputText.setText('0')
            equal = False
            strings = ''
        else:
            inputText.setText('4')
            strings += '4'
            inputText.setText(strings)
    elif x.x > 0 and x.x < 150 and x.y > 100 and x.y < 500:
        if equal:
            inputText.setText('0')
            equal = False
            strings = ''
        else:
            inputText.setText('1')
            strings += '1'
            inputText.setText(strings)
    elif x.x > 150 and x.x < 300 and x.y > 100 and x.y < 200:

        if '-' in strings:
            strings = int(strings) * (-1)
            strings = str(strings)
            inputText.setText(strings)
            equal = False
            plus_minus = True
        else:
            if strings == '':
                inputText.setText('0')
            elif '-' in strings:
                inputText.setText('0')
                strings = ''
            else:
                strings = '-' + strings
                inputText.setText(str(strings))
                equal = False

        # inputText.setText('+/-')
    elif x.x > 150 and x.x < 300 and x.y > 100 and x.y < 300:
        if equal:
            inputText.setText('0')
            equal = False
            strings = ''
        else:
            inputText.setText('8')
            strings += '8'
            inputText.setText(strings)
    elif x.x > 150 and x.x < 300 and x.y > 100 and x.y < 400:
        if equal:
            inputText.setText('0')
            equal = False
            strings = ''
        else:
            inputText.setText('5')
            strings += '5'
            inputText.setText(strings)
    elif x.x > 150 and x.x < 300 and x.y > 100 and x.y < 500:
        if equal:
            inputText.setText('0')
            equal = False
            strings = ''
        else:
            inputText.setText(2)
            strings += '2'
            inputText.setText(strings)
    elif x.x > 0 and x.x < 300 and x.y > 100 and x.y < 600:
        if equal:
            inputText.setText('0')
            equal = False
            strings = ''
        else:
            inputText.setText('0')
            if strings == '0':
                inputText.setText('0')
                strings = ''
            else:
                strings += '0'
                inputText.setText(strings)
    elif x.x > 300 and x.x < 450 and x.y > 100 and x.y < 200:
        if modulus:
            strings = modulus1(integers, strings)
            modulus = False
        if exponention:
            strings = exponention1(integers, strings)
            exponention = False
        if division:
            strings = division1(integers, strings)
            division = False
        if multi:
            strings = multi1(integers, strings)
            multi = False
        if sub:
            strings = sub1(integers, strings)
            sub = False
        if addition:
            strings = addition1(integers, strings)
            addition = False

        if strings == '' and modulus == False:
            inputText.setText('0')
        else:
            try:
                if modulus == True:
                    inputText.setText('0')
                    strings = ''
                    modulus = False
                else:
                    inputText.setText(strings)
                    modulus = True
                    integers = int(strings)
                    equal = False
                    strings = ''
            except ValueError:
                inputText.setText('0')
                strings = ''
        # inputText.setText('%')
    elif x.x > 300 and x.x < 450 and x.y > 100 and x.y < 300:
        if equal:
            inputText.setText('0')
            equal = False
            strings = ''
        else:
            inputText.setText('9')
            strings += '9'
            inputText.setText(strings)
    elif x.x > 300 and x.x < 450 and x.y > 100 and x.y < 400:
        if equal:
            inputText.setText('0')
            equal = False
            strings = ''
        else:
            inputText.setText('6')
            strings += '6'
            inputText.setText(strings)
    elif x.x > 300 and x.x < 450 and x.y > 100 and x.y < 500:
        if equal:
            inputText.setText('0')
            equal = False
            strings = ''
        else:
            inputText.setText('3')
            strings += '3'
            inputText.setText(strings)
    elif x.x > 300 and x.x < 450 and x.y > 100 and x.y < 600:
        if modulus:
            strings = modulus1(integers, strings)
            modulus = False
        if exponention:
            strings = exponention1(integers, strings)
            exponention = False
        if division:
            strings = division1(integers, strings)
            division = False
        if multi:
            strings = multi1(integers, strings)
            multi = False
        if sub:
            strings = sub1(integers, strings)
            sub = False
        if addition:
            strings = addition1(integers, strings)
            addition = False

        if strings == '' and exponention == False:
            inputText.setText('0')
        else:
            try:
                if exponention == True:
                    inputText.setText('0')
                    strings = ''
                    exponention = False
                else:
                    inputText.setText(strings)
                    exponention = True
                    integers = int(strings)
                    equal = False
                    strings = ''
            except ValueError:
                inputText.setText('0')
                strings = ''
        # inputText.setText('**')
    elif x.x > 450 and x.x < 600 and x.y > 100 and x.y < 200:
        if modulus:
            strings = modulus1(integers, strings)
            modulus = False
        if exponention:
            strings = exponention1(integers, strings)
            exponention = False
        if division:
            strings = division1(integers, strings)
            division = False
        if multi:
            strings = multi1(integers, strings)
            multi = False
        if sub:
            strings = sub1(integers, strings)
            sub = False
        if addition:
            strings = addition1(integers, strings)
            addition = False

        if strings == '' and division == False:
            inputText.setText('0')
        else:
            try:
                if division == True:
                    inputText.setText('0')
                    strings = ''
                    division = False
                else:
                    inputText.setText(strings)
                    division = True
                    integers = int(strings)
                    equal = False
                    strings = ''
            except ValueError:
                inputText.setText('0')
                strings = ''
        # inputText.setText('/')
    elif x.x > 450 and x.x < 600 and x.y > 100 and x.y < 300:
        if modulus:
            strings = modulus1(integers, strings)
            modulus = False
        if exponention:
            strings = exponention1(integers, strings)
            exponention = False
        if division:
            strings = division1(integers, strings)
            division = False
        if multi:
            strings = multi1(integers, strings)
            multi = False
        if sub:
            strings = sub1(integers, strings)
            sub = False
        if addition:
            strings = addition1(integers, strings)
            addition = False

        if strings == '' and multi == False:
            inputText.setText('0')
        else:
            try:
                if multi == True:
                    inputText.setText('0')
                    strings = ''
                    multi = False
                else:
                    inputText.setText(strings)
                    multi = True
                    integers = int(strings)
                    equal = False
                    strings = ''
            except ValueError:
                inputText.setText('0')
                strings = ''

        # inputText.setText('x')
    elif x.x > 450 and x.x < 600 and x.y > 100 and x.y < 400:
        if modulus:
            strings = modulus1(integers, strings)
            modulus = False
        if exponention:
            strings = exponention1(integers, strings)
            exponention = False
        if division:
            strings = division1(integers, strings)
            division = False
        if multi:
            strings = multi1(integers, strings)
            multi = False
        if sub:
            strings = sub1(integers, strings)
            sub = False
        if addition:
            strings = addition1(integers, strings)
            addition = False

        if strings == '' and sub == False:
            inputText.setText('0')
        else:
            try:
                if sub == True:
                    inputText.setText('0')
                    strings = ''
                    sub = False
                else:
                    inputText.setText(strings)
                    sub = True
                    integers = int(strings)
                    equal = False
                    strings = ''
            except ValueError:
                inputText.setText('0')
                strings = ''
        # inputText.setText('-')
    elif x.x > 450 and x.x < 600 and x.y > 100 and x.y < 500:
        if modulus:
            strings = modulus1(integers, strings)
            modulus = False
        if exponention:
            strings = exponention1(integers, strings)
            exponention = False
        if division:
            strings = division1(integers, strings)
            division = False
        if multi:
            strings = multi1(integers, strings)
            multi = False
        if sub:
            strings = sub1(integers, strings)
            sub = False
        if addition:
            strings = addition1(integers, strings)
            addition = False

        if strings == '' and addition == False:
            inputText.setText('0')
        else:
            try:
                if addition == True:
                    inputText.setText('0')
                    strings = ''
                    addition = False
                else:
                    inputText.setText(strings)
                    addition = True
                    integers = int(strings)
                    equal = False
                    strings = ''
            except ValueError:
                inputText.setText('0')
                strings = ''
        # inputText.setText('+')
    elif x.x > 450 and x.x < 600 and x.y > 100 and x.y < 600:
        if strings == '':
            inputText.setText('0')
        if modulus:
            strings = modulus1(integers, strings)
            modulus = False
        if exponention:
            strings = exponention1(integers, strings)
            exponention = False
        if division:
            strings = division1(integers, strings)
            division = False
        if multi:
            strings = multi1(integers, strings)
            multi = False
        if sub:
            strings = sub1(integers, strings)
            sub = False
        if addition:
            strings = addition1(integers, strings)
            addition = False
        equal = True
        # inputText.setText('=')
