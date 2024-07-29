# Maya Numerals
Maya Numerals is a package that converts numbers written in Western digits into Maya numerical glyphs (represented in Unicode). Simply input a number to the package and get a list of the Maya glyphs that comprise that number in ascending order. For more information on Maya numerical writing, please consult the background section below.
     

<p align="center">
<img src="https://raw.githubusercontent.com/ian-nai/maya_numerals/main/maya_readme_image.png" height="200" width="240">
</p>

## Installation and Usage
Install using pip:
```
pip3 install maya_numerals
```

Maya Numerals takes a single integer as an argument. You can use the package on an integer with the following syntax:

```
from maya_numerals import mn

mn.convert(39)
# returns ['ᴮ9', 'ᴮ1']
```

## Font
The Maya numeral Unicode characters are supported by [this font](https://www.babelstone.co.uk/Fonts/Mayan.html) from BabelStone, which is licensed under the SIL Open Font License 1.1. Per BabelStone:

>...you are free to use it for personal or commercial purposes, and to redistribute it by itself or as part of a free or commercial software package, just as long as you do not sell the font on its own. The license also allows you to modify the font in any way you like, as long as the modified font does not use "BabelStone" in its name. Please read the license for details.

## Background
Maya numerals use a vigesimal (base-20) positional numeral system to represent numbers. From Wikipedia:
> For example, thirteen is written as three dots in a horizontal row above two horizontal bars; sometimes it is also written as three vertical dots to the left of two vertical bars. With these three symbols, each of the twenty vigesimal digits could be written.
>
>Numbers after 19 were written vertically in powers of twenty. 

For more information, consult the [full Wikipedia article](https://en.wikipedia.org/wiki/Maya_numerals).