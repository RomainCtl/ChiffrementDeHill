# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from enum import Enum, unique

@unique
class alphabet(Enum):
    A=0
    B=1
    C=2
    D=3
    E=4
    F=5
    G=6
    H=7
    I=8
    J=9
    K=10
    L=11
    M=12
    N=13
    O=14
    P=15
    Q=16
    R=17
    S=18
    T=19
    U=20
    V=21
    W=22
    X=23
    Y=24
    Z=25

#print(alphabet['A'].value)

TOT_FREQ = 10000
class freqApp(Enum):
    ES=305
    LE=246
    EN=242
    DE=215
    RE=209
    NT=197
    ON=164
    ER=163
    TE=163
    SE=155
    ET=143
    QU=134
    NE=127
    OU=118
    AI=117
    EM=113
    IT=112
    ME=104
    IS=103
    LA=101
    EC=100
    TI=98
    CE=98
    ED=96
    IE=94
    RA=92
    IN=90
    EU=89
    UR=88
    CO=87
    AR=86
    TR=86
    UE=85
    TA=85
    EP=82
    ND=80
    NS=79
    PA=78
    US=76
    SA=75
    SS=73
    AN=30
    
