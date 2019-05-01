import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def file_to_list():
    """reads lines from a file and builds a list using append."""
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
    fin = open('words.txt') #how to open file
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
    return a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = file_to_list()


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lengths = [len(a), len(b), len(c), len(d), len(e), len(f), len(g), len(h), len(i), len(j), len(k), len(l), len(m), len(n), len(o), len(p), len(q), len(r), len(s), len(t), len(u), len(v), len(w), len(x), len(y), len(z)]

print(lengths)
print(alphabet)

def graphing(lengths, alphabet):
    plt.figure
    plt.bar(alphabet, lengths)
    plt.show()

graphing(lengths, alphabet)
    
    
    
    
    