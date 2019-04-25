from microbit import *
import radio

radio.on()
while True:
    if button_a.was_pressed():
        sleep(100)
        if button_b.was_pressed():
            radio.send("end")
            display.show(Image.TARGET)
            sleep(750)
            display.clear()
        else:
            radio.send("dot")
            display.show(Image('00000:00000:00900:00000:00000'))
            sleep(750)
            display.clear()
    elif button_b.was_pressed():
        sleep(100)
        if button_a.was_pressed():
            radio.send("end")
            display.show(Image.TARGET)
            sleep(750)
            display.clear()
        else:
            radio.send("dash")
            display.show(Image('00000:00000:09990:00000:00000'))
            sleep(750)
            display.clear()
