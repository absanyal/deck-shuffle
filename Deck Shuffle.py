# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 02:43:29 2016

@author: AB Sanyal
"""
import random

def shuffle(a):
    p = a[:]
    b = []
    while (len(p) > 0):
        k = random.choice(p)
        b.append(k)
        p.remove(k)
    return b

def full_deck():
    deck = []
    for suit in ["Spade ", "Heart ", "Diamond ", "Club "]:
        card = suit + "A"
        deck.append(card)
        i = 2
        while (i <= 10):
            card = suit + str(i)
            deck.append(card)
            i += 1
        for royal in ["J", "Q", "K"]:
            card = suit + royal
            deck.append(card)
    return deck

def show_seq(seq, separator):
    i = 0
    p = ""
    while (i < len(seq)):
        p += str(seq[i])
        if (i < len(seq) - 1):
            p += str(separator)
        i += 1
    return p

new_deck = full_deck()
print("\nOrdered deck:")
print(show_seq(new_deck, ", "))
print("\nShuffled deck:")
print(show_seq(shuffle(new_deck), ", "))

#Small git test