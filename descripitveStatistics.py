import matplotlib.pyplot as plt
import numpy as np

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def file_to_list():
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    j = []
    k = []
    l = []
    m = []
    n = []
    o = []
    p = []
    q = []
    r = []
    s = []
    t = []
    u = []
    v = []
    w = []
    x = []
    y = []
    z = []
    fin = open('AliceInWonderland.txt') #how to open file
    for line in fin:
        word = line[:len(line)-1]
        for letter in word:
            if letter == "a": 
                a.append(word)
            elif letter == "b":
                b.append(word)
            elif letter == "c":
                c.append(word)
            elif letter == "d":
                d.append(word)
            elif letter == "e":
                e.append(word)
            elif letter == "f":
                f.append(word)
            elif letter == "g":
                g.append(word)
            elif letter == "h":
                h.append(word)
            elif letter == "i":
                i.append(word)
            elif letter == "j":
                j.append(word)
            elif letter == "k":
                k.append(word)
            elif letter == "l":
                l.append(word)
            elif letter == "m":
                m.append(word)
            elif letter == "n":
                n.append(word)
            elif letter == "o":
                o.append(word)
            elif letter == "p":
                p.append(word)
            elif letter == "q":
                q.append(word)
            elif letter == "r":
                r.append(word)
            elif letter == "s":
                s.append(word)
            elif letter == "t":
                t.append(word)
            elif letter == "u":
                u.append(word)
            elif letter == "v":
                v.append(word)
            elif letter == "w":
                w.append(word)
            elif letter == "x":
                x.append(word)
            elif letter == "y":
                y.append(word)
            elif letter == "z":
                z.append(word)
    fin.close()
    lengths = [len(a), len(b), len(c), len(d), len(e), len(f), len(g), len(h), len(i), len(j), len(k), len(l), len(m), len(n), len(o), len(p), len(q), len(r), len(s), len(t), len(u), len(v), len(w), len(x), len(y), len(z)]
    return lengths


def graphing(lengths, alphabet):
    plt.figure
    plt.bar(alphabet, lengths, color = ['darkred', 'firebrick', 'indianred', 'lightcoral', 'coral','darkorange', 'orange', 'gold', 'yellow', 'greenyellow', 'palegreen', 'lime', 'limegreen', 'mediumspringgreen', 'cyan', 'deepskyblue', 'dodgerblue', 'royalblue', 'blue', 'darkblue', 'darkslateblue', 'rebeccapurple', 'darkorchid', 'fuchsia', 'orchid', 'pink'])
    plt.show()
    
def finding_stats(lengths, alphabet):
    least_used = np.argmin(lengths) 
    most_used = np.argmax(lengths)
    print("least used: " + str(alphabet[least_used]))
    print("most used: " + str(alphabet[most_used])+ "\n")
    
    print("one symbol letters: E, T")
    print("frequency of one symbol letters: " + str((lengths[4] + lengths[19])/2) + "\n")
    
    print("two symbol letters: A, I, M, N")
    print("frequency of two symbol letters: " + str((lengths[12] + lengths[13] + lengths[0] + lengths[8])/4)+ "\n")
    
    print("three symbol letters: D, G, K, O, R, S, U, W")
    print("frequency of three symbol letters: " + str((lengths[14] + lengths[6] + lengths[10] + lengths[3] + lengths[22] + lengths[17] + lengths[20] + lengths[18])/8)+ "\n")
    
    print("four symbol letters: Q, Z, Y, C, X, B, J, P, L, F, V, H")
    print("frequency of four symbol letters: " + str((lengths[16] + lengths[25] + lengths[24] + lengths[2] + lengths[23] + lengths[1] + lengths[9] + lengths[15] + lengths[11] + lengths[5] + lengths[21] + lengths[7])/12))


lengths = file_to_list()
graphing(lengths, alphabet) 
finding_stats(lengths, alphabet)