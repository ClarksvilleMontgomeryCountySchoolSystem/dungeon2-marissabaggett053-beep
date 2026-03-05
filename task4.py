good = r"""  @\_______/@
        @|XXXXXXXX |
       @ |X||    X |
      @  |X||    X |
     @   |XXXXXXXX |
    @    |X||    X |             V
   @     |X||   .X |
  @      |X||.  .X |                      V
 @      |%XXXXXXXX%||
@       |X||  . . X||
        |X||   .. X||                               @     @
        |X||  .   X||.                              ||====%
        |X|| .    X|| .                             ||    %
        |X||.     X||   .                           ||====%
       |XXXXXXXXXXXX||     .                        ||    %
       |XXXXXXXXXXXX||         .                 .  ||====% .
       |XX|        X||                .        .    ||    %  .
       |XX|        X||                   .          ||====%   .
       |XX|        X||              .          .    ||    %     .
       |XX|======= X||============================+ || .. %  ........
===== /            X||                              ||    %
                   X||           /)                 ||    %
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
bad = r""" _            _
 / \          / \
 |~|          |~|
#"'"|'"'"'"'"|"'"|
#   |  _.._  |   |
#   |.'    `.|   |
#   |        |   |
#   |.   /~~/~~/~~/
#   | './  /  /  /
#   |  /--/--/--/|
#   | /  /  /  / |
#   |/--/--/--/  |
#   |========#   | lbm"""
drawbridge_raised = True
if not drawbridge_raised:
    outcome = "Thunder: YES! I'm home free."
    print(good)
else:
    outcome = "Doom: How am I ever supposed to get out of here?!"
    print(bad)
print(outcome)