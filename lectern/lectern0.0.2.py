import re

blocks = ['grass', 'stone', 'dirt', 'cobblestone','brick','planks','wool']
while True:
    raw_input = input("Enter Command: ")

    if "$help" in raw_input:
        print("Modifiers:")
        print("$print namespace: Specifies that the output should be written to a namespace.mcfunction file")
        print("--------------------------------------------------------------------------------------------")
        print("$loop (#): Specifies the number of times the command should be repeated.")
        print("--------------------------------------------------------------------------------------------")
        print("$delay[namespace](#): Specifies the delay for the execution of the command, in terms of a score name and its value.")
        print("--------------------------------------------------------------------------------------------")
        print("$[var_name]=[var_value][modifier]: Specifies a variable definition and its value. The modifier can be either + or -,")
        print("indicating if the value should increment or decrement each loop.")
        print("--------------------------------------------------------------------------------------------")
        print("$blocks: Specifies that the commands should be repeated for each block in the blocks list.")
        continue

    if "$print" in raw_input:
        my_func = raw_input.split()[1]
        output_to_file = True
        raw_input = raw_input.replace(f"$print {my_func}", "")
    else:
        my_func = "myfunction"
        output_to_file = False

    num_loops_match = re.search(r"\$loop\s*(\d+)", raw_input)
    num_loops = int(num_loops_match.group(1)) if num_loops_match else 1
    text = re.sub(r"\$loop\s*\d+", "", raw_input)
    
    delay_match = re.search(r"\$delay\s+(\w+)\s+(\d+)", text)
    delay_name = delay_match.group(1) if delay_match else None
    delay_value = int(delay_match.group(2)) if delay_match else 0
    text = re.sub(r"\$delay\s+(\w+)\s+(\d+)", "", text)

    var_defs = re.findall(r"\$(\w+)=(\d+)([\+|-]+)", text)
    for i in range(num_loops):
        for var_def in var_defs:
            var_name, var_value, var_modifier = var_def
            if var_modifier == "+":
                value = int(var_value) + i
            elif var_modifier == "-":
                value = int(var_value) - i
            try:
                exec(f"{var_name} = {value}")
            except NameError:
                exec(f"{var_name} = {value}")

        if "$blocks" in text:
            blocks_text = re.findall(r"\$blocks(.*?);", text)
            if not blocks_text:
                continue
            blocks_text = blocks_text[0]
            blocks_to_use = []
            blocks_to_exclude = []
            if "all" in blocks_text:
                blocks_to_use = blocks
            elif "!" in blocks_text:
                blocks_to_exclude = [block.strip() for block in blocks_text.split("!")[1].split()]
                blocks_to_use = [block for block in blocks if block not in blocks_to_exclude]
            else:
                blocks_to_use = [block.strip() for block in blocks_text.split()]
            for block in blocks_to_use:
                text_with_vars = text.replace("$blocks" + blocks_text + ";", block)
                if delay_name:
                    delay_text = f"execute as @a if score {delay_name} delay matches {i * delay_value} run "
                else:
                    delay_text = ""
                print(delay_text + text_with_vars.strip())
                if output_to_file:
                    with open(f"{my_func}.mcfunction", "a") as f:
                        f.write(delay_text + text_with_vars.strip() + "\n")

        else:
            text_with_vars = re.sub(r"\$(\w+)=(\d+)([\+|-]+)", lambda match: str(eval(match.group(1))), text)
            if delay_name:
                delay_text = f"execute as @a if score {delay_name} delay matches {i * delay_value} run "
            else:
                delay_text = ""
            print(delay_text + text_with_vars.strip())
            if output_to_file:
                with open(f"{my_func}.mcfunction", "a") as f:
                    f.write(delay_text + text_with_vars.strip() + "\n")
