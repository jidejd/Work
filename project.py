import gooeypie as gp


def Equalsbutton(event):
    Display.text = eval(Display.text)


def Clearbutton(event):
    Display.clear()


def Additionbutton(event):
    Display.text = Display.text + "+"


def Subtractbutton(event):
    Display.text = Display.text + "-"


def Dividebutton(event):
    Display.text = Display.text + "/"


def Multiplybutton(event):
    Display.text = Display.text + "*"


def Number0(event):
    Display.text = Display.text + '0'


def Number1(event):
    Display.text = Display.text + '1'


def Number2(event):
    Display.text = Display.text + '2'


def Number3(event):
    Display.text = Display.text + '3'


def Number4(event):
    Display.text = Display.text + '4'


def Number5(event):
    Display.text = Display.text + '5'


def Number6(event):
    Display.text = Display.text + '6'


def Number7(event):
    Display.text = Display.text + '7'


def Number8(event):
    Display.text = Display.text + '8'


def Number9(event):
    Display.text = Display.text + '9'


app = gp.GooeyPieApp('Calc')
app.width = 300

Clear = gp.Button(app, 'C', Clearbutton)
Display = gp.Input(app)

Addition = gp.Button(app, '+', Additionbutton)
Subtraction = gp.Button(app, '--', Subtractbutton)
Division = gp.Button(app, '/', Dividebutton)
Multiplication = gp.Button(app, 'X', Multiplybutton)

Number0 = gp.Button(app, '0', Number0)
Number1 = gp.Button(app, '1', Number1)
Number2 = gp.Button(app, '2', Number2)
Number3 = gp.Button(app, '3', Number3)
Number4 = gp.Button(app, '4', Number4)
Number5 = gp.Button(app, '5', Number5)
Number6 = gp.Button(app, '6', Number6)
Number7 = gp.Button(app, '7', Number7)
Number8 = gp.Button(app, '8', Number8)
Number9 = gp.Button(app, '9', Number9)

Equals = gp.Button(app, '=', Equalsbutton)

app.set_grid(6, 4)
app.add(Display, 1, 1)
app.add(Clear, 6, 1, align='center')

app.add(Addition, 3, 4, align='center')
app.add(Subtraction, 4, 4, align='center')
app.add(Division, 5, 4, align='center')
app.add(Multiplication, 6, 4, align='center')
app.add(Equals, 6, 3, align='center')

app.add(Number0, 6, 2, align='center')
app.add(Number1, 5, 1, align='center')
app.add(Number2, 5, 2, align='center')
app.add(Number3, 5, 3, align='center')
app.add(Number4, 4, 1, align='center')
app.add(Number5, 4, 2, align='center')
app.add(Number6, 4, 3, align='center')
app.add(Number7, 3, 1, align='center')
app.add(Number8, 3, 2, align='center')
app.add(Number9, 3, 3, align='center')

app.run()