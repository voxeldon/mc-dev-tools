# MC Dev Tools
**Simple scripts to assist with Minecraft Addon development.**

*These scripts are designed for Bedrock edition but may provide use in other cases.*

## Hueshifter
- Generates copies of textures with incremented hues.

---
## Actionbar
A script that generates complex actionbar title commands in Minecraft by taking user input. The script takes the id, scoreboard, and selector as inputs, converts the information into JSON format, and saves it as a file.

**Usage**
- Run the script in the terminal/command line
- Enter the id, board, and selector for the actionbar title
- The script will generate and save a JSON file with the actionbar title information
  
**Limitations**
- The number of characters in the id and selector is not specified.

---

## Book Gen

A script to generate a book in Minecraft by taking user input for the book's title, author name, and text. The script converts the text into pages and saves it as a JSON file.

**Usage**
- Run the script in the terminal/command line
- Enter the book title, author name, and text
- The script will generate a JSON file with the book's information

**Limitations**
- Book text must be less than 12800 characters
- Each page can have up to 256 characters

---

## Item Gen
A script that generates Minecraft item files by taking the id and item names from the user as input. The script creates language (.lang) files and JSON files for the items.

**Usage**
- Run the script in the terminal/command line
- Enter the id of the items (e.g. loadisk)
- Enter the item names separated by a space (e.g. apple orange banana)
- The script will generate the necessary files for the items
- Repeat the process if you want to generate files for more items

**Limitations**
- The script will only generate the files if they don't already exist.

---  

# Persona 
The script generates Minecraft skins by combining random parts from defined folders. The user inputs the number of skins to generate and the base name, and the script saves the final result as PNG files. 

**Usage**
- Run the script in the terminal/command line
- Enter the number of images you want to generate.
- Enter the name of the files you want to generate.
  
---

# Looper

This program is designed to generate Minecraft commands and write them to a file. The commands are based on a user-provided input string, which can contain variable definitions, looping, and other special syntax.

## Input format

The user provides an input string to the program, which can contain the following syntax:

- Variable definitions: Variables are defined using the syntax `$variable_name=value[+|-]`, where `value` is an integer and the optional `+` or `-` symbol specifies how the variable should be incremented or decremented during each iteration of a loop.
- Looping: Looping is specified using the syntax `$loop n`, where `n` is the number of times the commands should be repeated.
- Block expansion: Use $blocks syntax to repeat commands for each block in a predefined list. Select blocks with $blocks stone; or exclude with $blocks !stone;.
- Delays: Delays can be specified using the syntax `$delay score_name delay_value`, where `score_name` is the name of a fake player score and `delay_value` is the amount of time in ticks to wait before executing the commands.

## Output

The program outputs the generated commands to the console and, if specified, to a file. The filename is based on the `my_func` argument, which is specified using the special syntax `$print my_func`. The file extension is `.mcfunction`.

## Code overview

The code uses regular expressions (regex) to process the user-provided input string. It performs the following steps:

1. Parses the `$loop` and `$print` syntax.
2. Parses and evaluates the variable definitions.
3. Replaces `$blocks` with the names of blocks in the predefined list.
4. Replaces the `$delay` syntax with the appropriate `execute as @a if score ... delay matches ...` commands.
5. Writes the generated commands to the console and, if specified, to a file.

## Example usage

```py
$loop 5
$print my_func
$delay score_name 10
setblock ~$pos=1+ ~ ~ $blocks
```
### Explanation:
- $loop 5: This sets up a loop that will repeat the commands within it 5 times.
- $print my_func: This sets the filename for the output file to "my_func.mcfunction".
- $delay score_name 10: This sets a delay of 10 ticks using the score "score_name".
- $blocks This expands the $block variable which will be set in alphabetical order.

### Output 
```
setblock ~1 ~ ~ diamond_ore
execute as @a if score score_name matches 10 run setblock ~2 ~ ~ gold_ore
execute as @a if score score_name matches 10 run setblock ~3 ~ ~ iron_ore
execute as @a if score score_name matches 20 run setblock ~4 ~ ~ diamond_ore
execute as @a if score score_name matches 20 run setblock ~5 ~ ~ gold_ore
```