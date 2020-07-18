
def translator():
  translation = ""
  phrase = input("Put your sentence or word in english here: ")

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
      " ": " | ",
      "1": "•---- ",
      "2": "••--- ",
      "3": "•••-- ",
      "4": "••••- ",
      '5': "••••• ",
      '6': "-•••• ",
      '7': "--••• ",
      '8': "---•• ",
      '9': "----• ",
      "0": "----- ",
      ".": ".",
      ":": ":",
      "+": "•-•-• ",
      "=": "-•••- ",
      "/": "-••-• "
    }[phrase]
    translation += word_translation
  print(translation)


def run_function():
    print('Space between letters is denoted by " " and space between words is denoted by "|" also, "." is denoted by "." itself')
    for rerun in range(1000):
        translator()


run_function()
