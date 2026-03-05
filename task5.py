good = r"""                   ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
            ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::
           |;:;K`__,...;=\_____,=``           %%%&     %#,---
           |;::::::::::::|       `'.________+-------\   ``
          /8M%;:::;;:::::|                  |        `-------"""
bad = r"""  _,aaaaaaaaaaaaaaaaaaa,_                _,aaaaaaaaaaaaaaaaaaa,_
  ,P"                     "Y,            ,P"                     "Y,
 d'    ,aaaaaaaaaaaaaaa,    `b          d'    ,aaaaaaaaaaaaaaa,    `b
d'   ,d"            ,aaabaaaa8aaaaaaaaaa8aaaadaaa,            "b,   `b
I    I  ,adba,      I                            I      ,adba,  I    I
Y,   `Y,I    I      `aaaaaaaaaaaaaaaaaaaaaaaaaaaa'      I    I,P'   ,P
 Y,   `bI    Iaaaaaaaaad'   ,P          Y,   `baaaaaaaaaI    Id'   ,P
  `b,   I    I            ,d'            `b,            I    I   ,d'
    `baaI    Iaaaaaaaaaaad'                `baaaaaaaaaaaI    Iaad'
        I    I                                          I    I
        I    I                                          I    I
        I    I                                          I    I
    _,aaI    Iaaaaaaaaaaa,_                _,aaaaaaaaaaaI    Iaa,_
  ,P"   I    I            "Y,            ,P"            I    I   "Y,
 d'    ,I    Iaaaaaaaaa,    `b          d'    ,aaaaaaaaaI    I,    `b
d'   ,d"I    I         "b,   `b        d'   ,d"         I    I"b,   `b
I    I  `"YP"'   ,adba,  I    I        I    I  ,adba,   `"YP"'  I    I
Y,   `Y,         I    I,P'   ,P        Y,   `Y,I    I         ,P'   ,P
 Y,   `baaaaaaaaaI    Id'   ,P          Y,   `bI    Iaaaaaaaaad'   ,P
  `b,            I    I   ,d'            `b,   I    I            ,d'
    `baaaaaaaaaaaI    Iaad'                `baaI    Iaaaaaaaaaaad'
                 I    I        Normand         I    I
                 I    I                        I    I
                 I    I        Veilleux        I    I
    _,aaaaaaaaaaaI    Iaa,_                _,aaI    Iaaaaaaaaaaa,_
  ,P"            I    I   "Y,            ,P"   I    I            "Y,
 d'    ,aaaaaaaaaI    I,    `b          d'    ,I    Iaaaaaaaaa,    `b
d'   ,d"         I    I"b,   `b        d'   ,d"I    I         "b,   `b
I    I  ,adba,   `"YP"'  I    I        I    I  `"YP"'   ,adba,  I    I
Y,   `Y,I    I         ,P'   ,P        Y,   `Y,         I    I,P'   ,P
 Y,   `bI    Iaaaaaaaaad'   ,P          Y,   `baaaaaaaaaI    Id'   ,P
  `b,   I    I            ,d'            `b,            I    I   ,d'
    `baaI    Iaaaaaaaaaaad'                `baaaaaaaaaaaI    Iaad'
        I    I                                          I    I
        I    I                                          I    I
        I    I                                          I    I
    _,aaI    Iaaaaaaaaaaa,_                _,aaaaaaaaaaaI    Iaa,_
  ,P"   I    I            "Y,            ,P"            I    I   "Y,
 d'    ,I    Iaaaaaaaaa,    `b          d'    ,aaaaaaaaaI    I,    `b
d'   ,d"I    I      ,aaabaaaa8aaaaaaaaaa8aaaadaaa,      I    I"b,   `b
I    I  `"YP"'      I                            I      `"YP"'  I    I
Y,   `Y,            `aaaaaaaaaaaaaaaaaaaaaaaaaaaa'            ,P'   ,P
 Y,   `baaaaaaaaaaaaaaad'   ,P          Y,   `baaaaaaaaaaaaaaad'   ,P
  `b,                     ,d'            `b,                     ,d'
    `baaaaaaaaaaaaaaaaaaad'                `baaaaaaaaaaaaaaaaaaad'
"""
escaped = False
if escaped:
    outcome = "Legend: YIPPEEEEEEE! Take that Dungeon."
    print(good)
else:
    outcome = "Doom: NOooOoOoOOoOoo!! Why meeeeee?"
    print(bad)
print(outcome)