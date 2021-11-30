import os, sys

tempText=r"Genesis 1:1	In the beginning God created the heaven and the earth. Genesis 1:2	And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. Genesis 1:3	And God said, Let there be light: and there was light. Genesis 1:4	And God saw the light, that it was good: and God divided the light from the darkness. Genesis 1:5	And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day. Genesis 1:6	And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters. Genesis 1:7	And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so. Genesis 1:8	And God called the firmament Heaven. And the evening and the morning were the second day. Genesis 1:9	And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear: and it was so. Genesis 1:10	And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good. Genesis 1:11	And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth: and it was so. Genesis 1:12	And the earth brought forth grass, and herb yielding seed after his kind, and the tree yielding fruit, whose seed was in itself, after his kind: and God saw that it was good. Genesis 1:13	And the evening and the morning were the third day. Genesis 1:14	And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years: Genesis 1:15	And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so. Genesis 1:16	And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also. Genesis 1:17	And God set them in the firmament of the heaven to give light upon the earth,"

def sort_bible(bibletext):
	letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	out_letters=dict()
	for letter in bibletext:
	    if letter in letters:
	        out_letters[letter.lower()].append(letter)
	return out_letters.values.join()

print(sort_bible(tempText))

# bib=open(r"D:\Temp\bible.txt", "r")
# bib_sort=open(r"D:\Temp\bible_sorted.txt", "w")

