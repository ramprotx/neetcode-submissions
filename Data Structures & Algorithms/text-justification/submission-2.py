class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []                      # finished lines
        line, length = [], 0          # line = words on the current line
                                      # length = total letters on the line (spaces NOT counted)
        i = 0                         # index of the next word to place

        while i < len(words):
            # Does words[i] fit on this line?
            # letters so far + new word + minimum spaces needed
            # len(line) = number of gaps once the new word is added (1 space per gap minimum)
            if length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])            # it fits: add it
                length += len(words[i])          # count only its letters
                i += 1                           # move to the next word
            else:
                # ---- Line is full: spread spaces and save it ----
                # (i is NOT advanced, so words[i] starts the next line)

                extra_space = maxWidth - length  # total spaces to add to this line

                gaps = max(1, len(line) - 1)     # gaps between words; one word -> 1 "gap" after it,
                                                 # so a single word gets all spaces on its right (left-justified)
                                                 # max(1, ...) also avoids dividing by zero

                space = extra_space // gaps      # spaces EVERY gap gets
                remainder = extra_space % gaps   # leftover spaces, handed out one each to the LEFTMOST gaps

                for j in range(gaps):            # for each gap (attached after word j)
                    line[j] += " " * space       # add the even share
                    if remainder:                # extra spaces still left?
                        line[j] += " "           # left gaps get one more (the problem's rule)
                        remainder -= 1

                res.append("".join(line))        # words already carry their spaces, so join with ""
                line, length = [], 0             # start a fresh line

        # ---- Last line: left-justified ----
        last_line = " ".join(line)               # exactly one space between words
        trail_space = maxWidth - len(last_line)  # pad the end with spaces up to maxWidth
        res.append(last_line + " " * trail_space)
        return res