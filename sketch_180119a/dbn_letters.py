









"""
s18019 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

This code was generated by sketch_to_generate_dbn_letters_py.py

Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing        
"""
dbn_letter = {}  # Dict of functions

# A
def dbn_letterA(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+7))
    line((h),(v+7),(h+3),(v+10))
    line((h+3),(v+10),(h+10),(v+3))
    line((h+10),(v+3),(h+10),v)
    line(h,(v+3),(h+10),(v+3))
    popMatrix()
dbn_letter['A'] = dbn_letterA
dbn_letter[1] = dbn_letterA

# B
def dbn_letterB(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+10))
    line(h,(v+10),(h+5),(v+10))
    line((h+5),(v+10),(h+8),(v+7))
    line(h,(v+6),(h+7),(v+6))
    line((h+7),(v+6),(h+10),(v+3))
    line((h+10),(v+3),(h+10),(v+1))
    line(h,v,(h+9),v)
    popMatrix()
dbn_letter['B'] = dbn_letterB
dbn_letter[2] = dbn_letterB

# C
def dbn_letterC(h, v):
    pushMatrix()
    scale(1, -1)
    line((h+4),v,(h+10),v)
    line((h+4),v,h,(v+4))
    line(h,(v+4),h,(v+9))
    line((h+1),(v+10),(h+9),(v+10))
    popMatrix()
dbn_letter['C'] = dbn_letterC
dbn_letter[3] = dbn_letterC

# D
def dbn_letterD(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+10))
    line(h,v,(h+8),v)
    line((h+8),v,(h+10),(v+2))
    line((h+10),(v+2),(h+10),(v+6))
    line((h+10),(v+6),(h+6),(v+10))
    line((h+6),(v+10),h,(v+10))
    popMatrix()
dbn_letter['D'] = dbn_letterD
dbn_letter[4] = dbn_letterD

# E
def dbn_letterE(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,(v+3),h,(v+10))
    line(h,(v+3),(h+3),v)
    line((h+3),v,(h+10),v)
    line(h,(v+6),(h+9),(v+6))
    line(h,(v+10),(h+9),(v+10))
    popMatrix()
dbn_letter['E'] = dbn_letterE
dbn_letter[5] = dbn_letterE

# F
def dbn_letterF(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+10))
    line(h,(v+6),(h+8),(v+6))
    line(h,(v+10),(h+10),(v+10))
    popMatrix()
dbn_letter['F'] = dbn_letterF
dbn_letter[6] = dbn_letterF

# G
def dbn_letterG(h, v):
    pushMatrix()
    scale(1, -1)
    line((h+4),v,(h+9),v)
    line((h+4),v,h,(v+4))
    line(h,(v+4),h,(v+9))
    line((h+1),(v+10),(h+9),(v+10))
    line((h+10),(v+1),(h+10),(v+5))
    line((h+10),(v+5),(h+6),(v+5))
    popMatrix()
dbn_letter['G'] = dbn_letterG
dbn_letter[7] = dbn_letterG

# H
def dbn_letterH(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+10))
    line(h,(v+4),(h+10),(v+4))
    line((h+10),v,(h+10),(v+10))
    popMatrix()
dbn_letter['H'] = dbn_letterH
dbn_letter[8] = dbn_letterH

# I
def dbn_letterI(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,(h+10),v)
    line((h+5),v,(h+5),(v+10))
    line(h,(v+10),(h+9),(v+10))
    popMatrix()
dbn_letter['I'] = dbn_letterI
dbn_letter[9] = dbn_letterI

# J
def dbn_letterJ(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,(v+3),(h+3),v)
    line((h+3),v,(h+9),v)
    line((h+10),(v+1),(h+10),(v+10))
    popMatrix()
dbn_letter['J'] = dbn_letterJ
dbn_letter[10] = dbn_letterJ

# K
def dbn_letterK(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+10))
    line(h,(v+1),(h+9),(v+10))
    line((h+5),(v+5),(h+10),v)
    popMatrix()
dbn_letter['K'] = dbn_letterK
dbn_letter[11] = dbn_letterK

# L
def dbn_letterL(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+10))
    line(h,v,(h+10),v)
    popMatrix()
dbn_letter['L'] = dbn_letterL
dbn_letter[12] = dbn_letterL

# M
def dbn_letterM(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+10))
    #line(h,(v+10),(h+2),(v+10))
    line((h+1),(v+10),(h+5),(v+6))
    line((h+5),(v+6),(h+9),(v+10))
    line((h+10),(v+10),(h+10),v)
    popMatrix()
dbn_letter['M'] = dbn_letterM
dbn_letter[13] = dbn_letterM

# N
def dbn_letterN(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+10))
    line(h,(v+10),(h+3),(v+10))
    line((h+3),(v+10),(h+10),(v+3))
    line((h+10),(v+10),(h+10),v)
    popMatrix()
dbn_letter['N'] = dbn_letterN
dbn_letter[14] = dbn_letterN

# O
def dbn_letterO(h, v):
    pushMatrix()
    scale(1, -1)
    line((h+4),v,(h+9),v)
    line((h+4),v,h,(v+4))
    line(h,(v+4),h,(v+9))
    line((h+1),(v+10),(h+7),(v+10))
    line((h+7),(v+10),(h+10),(v+7))
    line((h+10),(v+7),(h+10),(v+1))
    popMatrix()
dbn_letter['O'] = dbn_letterO
dbn_letter[15] = dbn_letterO

# P
def dbn_letterP(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+10))
    line(h,(v+10),(h+7),(v+10))
    line((h+7),(v+10),(h+10),(v+7))
    line((h+10),(v+6),(h+8),(v+4))
    line(h,(v+4),(h+8),(v+4))
    popMatrix()
dbn_letter['P'] = dbn_letterP
dbn_letter[16] = dbn_letterP

# Q
def dbn_letterQ(h, v):
    pushMatrix()
    scale(1, -1)
    line((h+4),v,(h+8),v)
    line((h+4),v,h,(v+4))
    line(h,(v+4),h,(v+9))
    line((h+1),(v+10),(h+7),(v+10))
    line((h+7),(v+10),(h+10),(v+7))
    line((h+10),(v+7),(h+10),(v+2))
    line((h+6),(v+4),(h+10),v)
    popMatrix()
dbn_letter['Q'] = dbn_letterQ
dbn_letter[17] = dbn_letterQ

# R
def dbn_letterR(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,h,(v+10))
    line(h,(v+10),(h+7),(v+10))
    line((h+7),(v+10),(h+10),(v+7))
    line((h+10),(v+6),(h+8),(v+4))
    line(h,(v+4),(h+8),(v+4))
    line((h+6),(v+4),(h+10),v)
    popMatrix()
dbn_letter['R'] = dbn_letterR
dbn_letter[18] = dbn_letterR

# S
def dbn_letterS(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,(v+2),(h+2),v)
    line((h+2),v,(h+9),v)
    line((h+10),(v+1),(h+10),(v+4))
    line((h+9),(v+5),(h+2),(v+5))
    line((h+2),(v+5),h,(v+7))
    line(h,(v+7),h,(v+9))
    line((h+1),(v+10),(h+9),(v+10))
    line((h+9),(v+10),(h+10),(v+9))
    popMatrix()
dbn_letter['S'] = dbn_letterS
dbn_letter[19] = dbn_letterS

# T
def dbn_letterT(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,(v+10),(h+10),(v+10))
    line((h+5),(v+10),(h+5),v)
    popMatrix()
dbn_letter['T'] = dbn_letterT
dbn_letter[20] = dbn_letterT

# U
def dbn_letterU(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,(v+10),h,(v+3))
    line(h,(v+3),(h+3),v)
    line((h+3),v,(h+9),v)
    line((h+10),(v+1),(h+10),(v+10))
    popMatrix()
dbn_letter['U'] = dbn_letterU
dbn_letter[21] = dbn_letterU

# V
def dbn_letterV(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,(v+10),h,(v+5))
    line(h,(v+5),(h+5),v)
    line((h+5),v,(h+10),(v+5))
    line((h+10),(v+5),(h+10),(v+10))
    popMatrix()
dbn_letter['V'] = dbn_letterV
dbn_letter[22] = dbn_letterV

# W
def dbn_letterW(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,(v+10),h,(v+3))
    line(h,(v+3),(h+3),v)
    line((h+3),v,(h+6),(v+3))
    line((h+6),(v+3),(h+9),v)
    line((h+10),(v+1),(h+10),(v+10))
    popMatrix()
dbn_letter['W'] = dbn_letterW
dbn_letter[23] = dbn_letterW

# X
def dbn_letterX(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,(v+10),h,(v+9))
    line(h,(v+9),(h+4),(v+5))
    line((h+4),(v+5),(h+6),(v+5))
    line((h+6),(v+5),(h+10),(v+9))
    line((h+10),(v+9),(h+10),(v+10))
    line(h,v,h,(v+1))
    line(h,(v+1),(h+4),(v+5))
    line((h+6),(v+5),(h+10),(v+1))
    line((h+10),(v+1),(h+10),v)
    popMatrix()
dbn_letter['X'] = dbn_letterX
dbn_letter[24] = dbn_letterX

# X
def dbn_letterX(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,v,(h+10),(v+10))
    line(h,(v+10),(h+10),v)
    popMatrix()
dbn_letter['X'] = dbn_letterX
dbn_letter[24] = dbn_letterX

# Y
def dbn_letterY(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,(v+10),h,(v+7))
    line(h,(v+7),(h+3),(v+4))
    line((h+3),(v+4),(h+10),(v+4))
    line((h+10),(v+10),(h+10),(v+1))
    line((h+9),v,(h+2),v)
    line((h+2),v,h,(v+2))
    popMatrix()
dbn_letter['Y'] = dbn_letterY
dbn_letter[25] = dbn_letterY

# Z
def dbn_letterZ(h, v):
    pushMatrix()
    scale(1, -1)
    line(h,(v+10),(h+10),(v+10))
    line((h+10),(v+10),h,v)
    line(h,v,(h+10),v)
    popMatrix()
dbn_letter['Z'] = dbn_letterZ
dbn_letter[26] = dbn_letterZ

