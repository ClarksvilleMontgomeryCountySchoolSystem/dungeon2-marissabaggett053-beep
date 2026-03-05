good = r"""  .--.
              /.-. '----------.
              \'-' .--"--""-"-'
           jgs '--'
"""
bad = r"""           .-""-.
           / .--. \
          / /    \ \
          | |    | |
          | |.-""-.|
         ///`.::::.`\
        ||| ::/  \:: ;
        ||; ::\__/:: ;
         \\\ '::::' /
     jgs  `=':-..-'`"""
has_key = True
if has_key:
    outcome = "Click: Well, lets see what's beyond this door."
    print(good)
else:
    outcome = "Doom: What do I do now?"
    print(bad)
print(outcome)