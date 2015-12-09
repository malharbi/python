# used tkinter with pictuer and audio
# by Motaz AlHarbi in 12/3/15
  

import tkinter
from tkinter import *
import os

def buttonPressed( event ):
	print( "Listening to the audio ...for 4 minute" )
	os.system("afplay /Users/MAC/Desktop/MSCS-UNH/python/02-irish-cat.mp3")


base = tkinter.Tk()
base.title("The Demon Cat")
base.geometry("610x600+80+100")

frame1 = tkinter.Frame(base)
frame1.pack()
gif1 = PhotoImage(file = 'cat.gif')
canvas = tkinter.Canvas(frame1, height=315, width=610)
canvas.create_image(0, 0, image = gif1, anchor = NW)
canvas.pack()
canvas.bind( "<Button-1>", buttonPressed )

frame2 = tkinter.Frame(base)
frame2.pack()
lable= Label(frame2, text="click on the photo", fg="red")
lable.pack(side = TOP)

frame3 = Frame(base)
frame3.pack()
S = Scrollbar(frame3)
T = Text(frame3)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """There was a woman in Connemara – the wife of a fisherman. As he had always good luck, she had plenty of fish at all times stored away in the house ready for market. But, to her great annoyance, she found that a great cat used to come in at night and devour all the best and finest fish. So she kept a big stick by her, and determined to watch.

One day, as she and a woman were spinning together, the house suddenly became quite dark and the door was burst open as if by the blast of the tempest, when in walked a huge black cat, who went straight up to the fire, then turned round and growled at them.

“Why, surely this is the devil,” said a young girl, who was by, sorting fish.

“I’ll teach you how to call me names,” said the cat, and jumping at her, he scratched her arm till the blood came. “There, now,” he said, “you will be more civil another time when a gentleman comes to see you.” And with that he walked over to the door and shut it close, to prevent any of them going out, for the poor young girl, while crying loudly from fright and pain, had made a desperate rush to get away.

Just then a man was going by, and hearing the cries, he pushed open the door and tried to get in, but the cat stood on the threshold and would let no one pass. On this the man attacked him with his stick, and gave him a sound blow. The cat, however, was more than a match in the fight, for it flew at him and tore his face and hands so badly that the man at last took to his heels and ran away as fast as he could.

“Now, it’s time for my dinner,” said the cat, going up to examine the fish that was laid out on the tables. “I hope the fish is good today. Now, don’t disturb me, nor make a fuss. I can help myself.” With that he jumped up, and began to devour all the best fish, while he growled at the woman.

“Away, out of this, you wicked beast!” she cried, giving it a blow with the tongs that would have broken its back only it was a devil. “Out of this, no fish you have today.”

But the cat only grinned at her, and went on tearing and spoiling and devouring the fish, evidently not a bit the worse for the blow. On this, both the women attacked it with sticks, and struck hard blows enough to kill it, on which the cat glared at them, and spit fire. Then, making a leap, it tore their heads and arms till the blood came, and the frightened women rushed shrieking from the house.

But presently the mistress returned, carrying with her a bottle of holy water. And, looking in, she saw the cat still devouring the fish, and not minding. So she crept over quietly and threw holy water on it without a word. No sooner was this done than a dense black smoke filled the place, through which nothing was seen but the two red eyes of the cat, burning like coals of fire. Then the smoke gradually cleared away, and she saw the body of the creature burning slowly till it became shrivelled and black like a cinder, and finally disappeared. And from that time the fish remained untouched and safe from harm, for the power of the evil one was broken, and the demon cat was seen no more."""
T.insert(END, quote)

base.mainloop()
