from microbit import *
import radio


# set letters equal to images
A = Image('00900:09090:09990:90009:90009')
B = Image('09940:09090:09940:09090:09940')
C = Image('09990:09050:09000:09050:09990')
D = Image('09950:09090:09090:09090:09950')
E = Image('09990:09000:09900:09000:09990')
F = Image('09990:09000:09950:09000:09000')
G = Image('07990:09000:09690:09090:07990')
H = Image('09009:09009:09999:09009:09009')
I = Image('09990:00900:00900:00900:09990')
J = Image('00090:00090:00090:09090:05950')
K = Image('09009:09090:09900:09090:09009')
L = Image('09000:09000:09000:09000:09990')
M = Image('90009:99099:90909:90009:90009')
N = Image('90009:99009:90909:90099:90009')
O = Image('05950:09090:09090:09090:05950')
P = Image('09950:09090:09500:09000:09000')
Q = Image('09900:90090:90590:90090:09909')
R = Image('99950:90090:99950:90900:90090')
S = Image('09990:90000:09950:00090:99950')
T = Image('09990:00900:00900:00900:00900')
U = Image('09009:09009:09009:09009:04994')
V = Image('90009:90009:90009:09090:00900')
W = Image('90009:90009:90909:99099:90009')
X = Image('90009:09090:00900:09090:90009')
Y = Image('90009:09090:00900:00900:00900')
Z = Image('09999:00090:00900:09000:99990')




letter_string = ""

alphabet = {".-" : A, "-..." : B, "-.-." : C, "-.." : D, "." : E, "..-." : F, "--." : G, "...." : H,
            ".." : I, ".---" : J, "-.-" : K, ".-.." : L, "--" : M, "-." : N, "---" : O, ".--." : P,
            "--.-" : Q, ".-." : R, "..." : S, "-" : T, "..-" : U, "...-" : V, ".--" : W, "-..-" : X, "-.--" : Y, "--.." : Z}

radio.on()

def display_letter(letter_string):
    while True:
        r = radio.receive()
        #when a and b pressed, look up in dictionary and display letter
        if r == "end":
            #look up in dictionary the string
            #display that dictionary entry
            if letter_string in alphabet.keys():
                display.show(alphabet[str(letter_string)])
                sleep(1500)
                display.clear()
                letter_string = ""
            else:
                display.show(Image.SAD)
                sleep(1500)
                display.clear()
                letter_string = ""
        elif r == "dot":
            display.show(Image('00000:00000:00900:00000:00000'))
            sleep(750)
            display.clear()
            letter_string  = letter_string + "."
            #add "." to letter_string
        elif r == 'dash':
            display.show(Image('00000:00000:09990:00000:00000')) #be a dash
            sleep(750)
            display.clear()
            letter_string  = letter_string + "-"
            #add "-" to letter_string
    print(letter_string)


display_letter(letter_string)