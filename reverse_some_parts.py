'''
You have a text that some of the words in reverse order.
The text also contains some words in the correct order, and they are wrapped in parenthesis.
Write a function fixes all of the words and,
remove the parenthesis that is used for marking the correct words.

Your function should return the same text defined in the constant CORRECT_ANSWER
'''


INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca A reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) .gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. A pioneer of " \
                 "commercial fiction and American magazines, he was one of the first American authors to become an " \
                 "international celebrity and earn a large fortune from writing."

def fix_text(mystr):
    mystr=mystr.split()
    liste=[]
    for i in mystr:
        if (i[0]+ i[-1])=="()":
            liste.append(i[1:-1])
        else:
            liste.append(i[::-1])
    mystr=" ".join(liste)
    return mystr

if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")