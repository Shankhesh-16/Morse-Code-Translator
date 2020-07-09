
def translator(phrase):
  translation = ""
  
  for phrase in phrase.upper():
    word_translation = {
    "A": "•- ",
    "B": "-••• ",
    "C": "-•-• ",
    "D": "-•• ",
    "E": "• ",
    "F": "••-• ",
    "G": "--• ",
    "H": "•••• ",
    "I": "•• ",
    "J": "•--- ",
    "K": "-•- ",
    "L": "•-•• ",
    "M": "-- ",
    "N": "-• ",
    "O": "--- ",
    "P": "•--• ",
    "Q": "--•- ",
    "R": "•-• ",
    "S": "••• ",
    "T": "- ",
    "U": "••- ",
    "V": "•••- ",
    "W": "•-- ",
    "X": "-••- ",
    "Y": "-•-- ",
    "Z": "--•• ",
    " ": " / "
    }[phrase]
    translation += word_translation
  print(translation)

translator("Suggestions are welcome")