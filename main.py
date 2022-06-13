def on_gesture_shake():
    global Icono
    Icono = 0
    if Icono == 0:
        basic.show_icon(IconNames.CHESSBOARD)
    if Icono == 1:
        basic.show_icon(IconNames.MEH)
    if Icono == 2:
        basic.show_icon(IconNames.HEART)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Icono = 0
basic.show_string("Hola mundo ")
basic.show_icon(IconNames.HEART)
basic.show_number(10)
basic.pause(100)
basic.show_number(9)
basic.pause(100)
basic.show_number(8)
basic.pause(100)
basic.show_number(7)
basic.pause(100)
basic.show_number(6)
basic.pause(100)
basic.show_number(5)
basic.pause(100)
basic.show_number(4)
basic.pause(100)
basic.show_number(3)
basic.pause(100)
basic.show_number(2)
basic.pause(100)
basic.show_number(1)
basic.pause(100)
basic.show_number(0)

def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.ANGRY)
    if input.button_is_pressed(Button.B):
        basic.show_icon(IconNames.SAD)
basic.forever(on_forever)
