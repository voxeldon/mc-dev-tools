import re

blocks = [
        "minecraft:acacia_button",
        "minecraft:acacia_door",
        "minecraft:acacia_fence_gate",
        "minecraft:acacia_pressure_plate",
        "minecraft:acacia_stairs",
        "minecraft:acacia_standing_sign",
        "minecraft:acacia_trapdoor",
        "minecraft:acacia_wall_sign",
        "minecraft:activator_rail",
        "minecraft:amethyst_block",
        "minecraft:amethyst_cluster",
        "minecraft:ancient_debris",
        "minecraft:andesite_stairs",
        "minecraft:anvil",
        "minecraft:azalea_leaves_flowered",
        "minecraft:azalea_leaves",
        "minecraft:azalea",
        "minecraft:bamboo_sapling",
        "minecraft:bamboo",
        "minecraft:barrel",
        "minecraft:barrier",
        "minecraft:basalt",
        "minecraft:beacon",
        "minecraft:bed",
        "minecraft:bedrock",
        "minecraft:bee_nest",
        "minecraft:beehive",
        "minecraft:beetroot",
        "minecraft:bell",
        "minecraft:big_dripleaf",
        "minecraft:birch_button",
        "minecraft:birch_door",
        "minecraft:birch_fence_gate",
        "minecraft:birch_pressure_plate",
        "minecraft:birch_stairs",
        "minecraft:birch_standing_sign",
        "minecraft:birch_trapdoor",
        "minecraft:birch_wall_sign",
        "minecraft:black_candle_cake",
        "minecraft:black_candle",
        "minecraft:black_glazed_terracotta",
        "minecraft:blackstone_double_slab",
        "minecraft:blackstone_slab",
        "minecraft:blackstone_stairs",
        "minecraft:blackstone_wall",
        "minecraft:blackstone",
        "minecraft:blast_furnace",
        "minecraft:blue_candle_cake",
        "minecraft:blue_candle",
        "minecraft:blue_glazed_terracotta",
        "minecraft:blue_ice",
        "minecraft:bone_block",
        "minecraft:bookshelf",
        "minecraft:brewing_stand",
        "minecraft:brick_block",
        "minecraft:brick_stairs",
        "minecraft:brown_candle_cake",
        "minecraft:brown_candle",
        "minecraft:brown_glazed_terracotta",
        "minecraft:brown_mushroom_block",
        "minecraft:brown_mushroom",
        "minecraft:bubble_column",
        "minecraft:budding_amethyst",
        "minecraft:cactus",
        "minecraft:cake",
        "minecraft:calcite",
        "minecraft:campfire",
        "minecraft:candle_cake",
        "minecraft:candle",
        "minecraft:carpet",
        "minecraft:carrots",
        "minecraft:cartography_table",
        "minecraft:carved_pumpkin",
        "minecraft:cauldron",
        "minecraft:cave_vines_body_with_berries",
        "minecraft:cave_vines_head_with_berries",
        "minecraft:cave_vines",
        "minecraft:chain_command_block",
        "minecraft:chain",
        "minecraft:chest",
        "minecraft:chiseled_deepslate",
        "minecraft:chiseled_nether_bricks",
        "minecraft:chiseled_polished_blackstone",
        "minecraft:chorus_flower",
        "minecraft:chorus_plant",
        "minecraft:clay",
        "minecraft:coal_block",
        "minecraft:coal_ore",
        "minecraft:cobbled_deepslate_double_slab",
        "minecraft:cobbled_deepslate_slab",
        "minecraft:cobbled_deepslate_stairs",
        "minecraft:cobbled_deepslate_wall",
        "minecraft:cobbled_deepslate",
        "minecraft:cobblestone_wall",
        "minecraft:cobblestone",
        "minecraft:cocoa",
        "minecraft:command_block",
        "minecraft:composter",
        "minecraft:concrete_powder",
        "minecraft:concrete",
        "minecraft:conduit",
        "minecraft:copper_block",
        "minecraft:copper_ore",
        "minecraft:coral_block",
        "minecraft:coral_fan_dead",
        "minecraft:coral_fan_hang",
        "minecraft:coral_fan_hang2",
        "minecraft:coral_fan_hang3",
        "minecraft:coral_fan",
        "minecraft:coral",
        "minecraft:cracked_deepslate_bricks",
        "minecraft:cracked_deepslate_tiles",
        "minecraft:cracked_nether_bricks",
        "minecraft:cracked_polished_blackstone_bricks",
        "minecraft:crafting_table",
        "minecraft:crimson_button",
        "minecraft:crimson_door",
        "minecraft:crimson_double_slab",
        "minecraft:crimson_fence_gate",
        "minecraft:crimson_fence",
        "minecraft:crimson_fungus",
        "minecraft:crimson_hyphae",
        "minecraft:crimson_nylium",
        "minecraft:crimson_planks",
        "minecraft:crimson_pressure_plate",
        "minecraft:crimson_roots",
        "minecraft:crimson_slab",
        "minecraft:crimson_stairs",
        "minecraft:crimson_standing_sign",
        "minecraft:crimson_stem",
        "minecraft:crimson_trapdoor",
        "minecraft:crimson_wall_sign",
        "minecraft:crying_obsidian",
        "minecraft:cut_copper_slab",
        "minecraft:cut_copper_stairs",
        "minecraft:cut_copper",
        "minecraft:cyan_candle_cake",
        "minecraft:cyan_candle",
        "minecraft:cyan_glazed_terracotta",
        "minecraft:dark_oak_button",
        "minecraft:dark_oak_door",
        "minecraft:dark_oak_fence_gate",
        "minecraft:dark_oak_pressure_plate",
        "minecraft:dark_oak_stairs",
        "minecraft:dark_oak_trapdoor",
        "minecraft:dark_prismarine_stairs",
        "minecraft:darkoak_standing_sign",
        "minecraft:darkoak_wall_sign",
        "minecraft:daylight_detector_inverted",
        "minecraft:daylight_detector",
        "minecraft:deadbush",
        "minecraft:deepslate_brick_double_slab",
        "minecraft:deepslate_brick_slab",
        "minecraft:deepslate_brick_stairs",
        "minecraft:deepslate_brick_wall",
        "minecraft:deepslate_bricks",
        "minecraft:deepslate_coal_ore",
        "minecraft:deepslate_copper_ore",
        "minecraft:deepslate_diamond_ore",
        "minecraft:deepslate_emerald_ore",
        "minecraft:deepslate_gold_ore",
        "minecraft:deepslate_iron_ore",
        "minecraft:deepslate_lapis_ore",
        "minecraft:deepslate_redstone_ore",
        "minecraft:deepslate_tile_double_slab",
        "minecraft:deepslate_tile_slab",
        "minecraft:deepslate_tile_stairs",
        "minecraft:deepslate_tile_wall",
        "minecraft:deepslate_tiles",
        "minecraft:deepslate",
        "minecraft:detector_rail",
        "minecraft:diamond_block",
        "minecraft:diamond_ore",
        "minecraft:diorite_stairs",
        "minecraft:dirt_with_roots",
        "minecraft:dirt",
        "minecraft:dispenser",
        "minecraft:double_cut_copper_slab",
        "minecraft:double_plant",
        "minecraft:double_stone_block_slab",
        "minecraft:double_stone_block_slab2",
        "minecraft:double_stone_block_slab3",
        "minecraft:double_stone_block_slab4",
        "minecraft:double_wooden_slab",
        "minecraft:dragon_egg",
        "minecraft:dried_kelp_block",
        "minecraft:dripstone_block",
        "minecraft:dropper",
        "minecraft:emerald_block",
        "minecraft:emerald_ore",
        "minecraft:enchanting_table",
        "minecraft:end_brick_stairs",
        "minecraft:end_bricks",
        "minecraft:end_portal_frame",
        "minecraft:end_portal",
        "minecraft:end_rod",
        "minecraft:end_stone",
        "minecraft:ender_chest",
        "minecraft:exposed_copper",
        "minecraft:exposed_cut_copper_slab",
        "minecraft:exposed_cut_copper_stairs",
        "minecraft:exposed_cut_copper",
        "minecraft:exposed_double_cut_copper_slab",
        "minecraft:farmland",
        "minecraft:fence_gate",
        "minecraft:fence",
        "minecraft:fire",
        "minecraft:fletching_table",
        "minecraft:flower_pot",
        "minecraft:flowering_azalea",
        "minecraft:flowing_lava",
        "minecraft:flowing_water",
        "minecraft:frame",
        "minecraft:frog_spawn",
        "minecraft:frosted_ice",
        "minecraft:furnace",
        "minecraft:gilded_blackstone",
        "minecraft:glass_pane",
        "minecraft:glass",
        "minecraft:glow_frame",
        "minecraft:glow_lichen",
        "minecraft:glowstone",
        "minecraft:gold_block",
        "minecraft:gold_ore",
        "minecraft:golden_rail",
        "minecraft:granite_stairs",
        "minecraft:grass_path",
        "minecraft:grass",
        "minecraft:gravel",
        "minecraft:gray_candle_cake",
        "minecraft:gray_candle",
        "minecraft:gray_glazed_terracotta",
        "minecraft:green_candle_cake",
        "minecraft:green_candle",
        "minecraft:green_glazed_terracotta",
        "minecraft:grindstone",
        "minecraft:hanging_roots",
        "minecraft:hardened_clay",
        "minecraft:hay_block",
        "minecraft:heavy_weighted_pressure_plate",
        "minecraft:honey_block",
        "minecraft:honeycomb_block",
        "minecraft:hopper",
        "minecraft:ice",
        "minecraft:infested_deepslate",
        "minecraft:iron_bars",
        "minecraft:iron_block",
        "minecraft:iron_door",
        "minecraft:iron_ore",
        "minecraft:iron_trapdoor",
        "minecraft:jukebox",
        "minecraft:jungle_button",
        "minecraft:jungle_door",
        "minecraft:jungle_fence_gate",
        "minecraft:jungle_pressure_plate",
        "minecraft:jungle_stairs",
        "minecraft:jungle_standing_sign",
        "minecraft:jungle_trapdoor",
        "minecraft:jungle_wall_sign",
        "minecraft:kelp",
        "minecraft:ladder",
        "minecraft:lantern",
        "minecraft:lapis_block",
        "minecraft:lapis_ore",
        "minecraft:large_amethyst_bud",
        "minecraft:lava_cauldron",
        "minecraft:lava",
        "minecraft:leaves",
        "minecraft:leaves2",
        "minecraft:lectern",
        "minecraft:lever",
        "minecraft:light_block",
        "minecraft:light_blue_candle_cake",
        "minecraft:light_blue_candle",
        "minecraft:light_blue_glazed_terracotta",
        "minecraft:light_gray_candle_cake",
        "minecraft:light_gray_candle",
        "minecraft:light_weighted_pressure_plate",
        "minecraft:lightning_rod",
        "minecraft:lime_candle_cake",
        "minecraft:lime_candle",
        "minecraft:lime_glazed_terracotta",
        "minecraft:lit_blast_furnace",
        "minecraft:lit_deepslate_redstone_ore",
        "minecraft:lit_furnace",
        "minecraft:lit_pumpkin",
        "minecraft:lit_redstone_lamp",
        "minecraft:lit_redstone_ore",
        "minecraft:lit_smoker",
        "minecraft:lodestone",
        "minecraft:log",
        "minecraft:log2",
        "minecraft:loom",
        "minecraft:magenta_candle_cake",
        "minecraft:magenta_candle",
        "minecraft:magenta_glazed_terracotta",
        "minecraft:magma",
        "minecraft:mangrove_button",
        "minecraft:mangrove_door",
        "minecraft:mangrove_double_slab",
        "minecraft:mangrove_fence_gate",
        "minecraft:mangrove_fence",
        "minecraft:mangrove_leaves",
        "minecraft:mangrove_log",
        "minecraft:mangrove_planks",
        "minecraft:mangrove_pressure_plate",
        "minecraft:mangrove_propagule",
        "minecraft:mangrove_roots",
        "minecraft:mangrove_slab",
        "minecraft:mangrove_stairs",
        "minecraft:mangrove_standing_sign",
        "minecraft:mangrove_trapdoor",
        "minecraft:mangrove_wall_sign",
        "minecraft:mangrove_wood",
        "minecraft:medium_amethyst_bud",
        "minecraft:melon_block",
        "minecraft:melon_stem",
        "minecraft:mob_spawner",
        "minecraft:monster_egg",
        "minecraft:moss_block",
        "minecraft:moss_carpet",
        "minecraft:mossy_cobblestone_stairs",
        "minecraft:mossy_cobblestone",
        "minecraft:mossy_stone_brick_stairs",
        "minecraft:mud_brick_double_slab",
        "minecraft:mud_brick_slab",
        "minecraft:mud_brick_stairs",
        "minecraft:mud_brick_wall",
        "minecraft:mud_bricks",
        "minecraft:mud",
        "minecraft:muddy_mangrove_roots",
        "minecraft:mycelium",
        "minecraft:nether_brick_fence",
        "minecraft:nether_brick_stairs",
        "minecraft:nether_brick",
        "minecraft:nether_gold_ore",
        "minecraft:nether_sprouts",
        "minecraft:nether_wart_block",
        "minecraft:nether_wart",
        "minecraft:netherite_block",
        "minecraft:netherrack",
        "minecraft:normal_stone_stairs",
        "minecraft:noteblock",
        "minecraft:oak_stairs",
        "minecraft:observer",
        "minecraft:obsidian",
        "minecraft:ochre_froglight",
        "minecraft:orange_candle_cake",
        "minecraft:orange_candle",
        "minecraft:orange_glazed_terracotta",
        "minecraft:oxidized_copper",
        "minecraft:oxidized_cut_copper_slab",
        "minecraft:oxidized_cut_copper_stairs",
        "minecraft:oxidized_cut_copper",
        "minecraft:oxidized_double_cut_copper_slab",
        "minecraft:packed_ice",
        "minecraft:packed_mud",
        "minecraft:pearlescent_froglight",
        "minecraft:pink_candle_cake",
        "minecraft:pink_candle",
        "minecraft:pink_glazed_terracotta",
        "minecraft:piston_arm_collision",
        "minecraft:piston",
        "minecraft:planks",
        "minecraft:podzol",
        "minecraft:pointed_dripstone",
        "minecraft:polished_andesite_stairs",
        "minecraft:polished_basalt",
        "minecraft:polished_blackstone_brick_double_slab",
        "minecraft:polished_blackstone_brick_slab",
        "minecraft:polished_blackstone_brick_stairs",
        "minecraft:polished_blackstone_brick_wall",
        "minecraft:polished_blackstone_bricks",
        "minecraft:polished_blackstone_button",
        "minecraft:polished_blackstone_double_slab",
        "minecraft:polished_blackstone_pressure_plate",
        "minecraft:polished_blackstone_slab",
        "minecraft:polished_blackstone_stairs",
        "minecraft:polished_blackstone_wall",
        "minecraft:polished_blackstone",
        "minecraft:polished_deepslate_double_slab",
        "minecraft:polished_deepslate_slab",
        "minecraft:polished_deepslate_stairs",
        "minecraft:polished_deepslate_wall",
        "minecraft:polished_deepslate",
        "minecraft:polished_diorite_stairs",
        "minecraft:polished_granite_stairs",
        "minecraft:portal",
        "minecraft:potatoes",
        "minecraft:powder_snow",
        "minecraft:powered_comparator",
        "minecraft:powered_repeater",
        "minecraft:prismarine_bricks_stairs",
        "minecraft:prismarine_stairs",
        "minecraft:prismarine",
        "minecraft:pumpkin_stem",
        "minecraft:pumpkin",
        "minecraft:purple_candle_cake",
        "minecraft:purple_candle",
        "minecraft:purple_glazed_terracotta",
        "minecraft:purpur_block",
        "minecraft:purpur_stairs",
        "minecraft:quartz_block",
        "minecraft:quartz_bricks",
        "minecraft:quartz_ore",
        "minecraft:quartz_stairs",
        "minecraft:rail",
        "minecraft:raw_copper_block",
        "minecraft:raw_gold_block",
        "minecraft:raw_iron_block",
        "minecraft:red_candle_cake",
        "minecraft:red_candle",
        "minecraft:red_flower",
        "minecraft:red_glazed_terracotta",
        "minecraft:red_mushroom_block",
        "minecraft:red_mushroom",
        "minecraft:red_nether_brick_stairs",
        "minecraft:red_nether_brick",
        "minecraft:red_sandstone_stairs",
        "minecraft:red_sandstone",
        "minecraft:redstone_block",
        "minecraft:redstone_lamp",
        "minecraft:redstone_ore",
        "minecraft:redstone_torch",
        "minecraft:redstone_wire",
        "minecraft:reeds",
        "minecraft:reinforced_deepslate",
        "minecraft:repeating_command_block",
        "minecraft:respawn_anchor",
        "minecraft:sand",
        "minecraft:sandstone_stairs",
        "minecraft:sandstone",
        "minecraft:sapling",
        "minecraft:scaffolding",
        "minecraft:sculk_catalyst",
        "minecraft:sculk_sensor",
        "minecraft:sculk_shrieker",
        "minecraft:sculk_vein",
        "minecraft:sculk",
        "minecraft:sea_lantern",
        "minecraft:sea_pickle",
        "minecraft:seagrass",
        "minecraft:shroomlight",
        "minecraft:shulker_box",
        "minecraft:silver_glazed_terracotta",
        "minecraft:skull",
        "minecraft:slime",
        "minecraft:small_amethyst_bud",
        "minecraft:small_dripleaf_block",
        "minecraft:smithing_table",
        "minecraft:smoker",
        "minecraft:smooth_basalt",
        "minecraft:smooth_quartz_stairs",
        "minecraft:smooth_red_sandstone_stairs",
        "minecraft:smooth_sandstone_stairs",
        "minecraft:smooth_stone",
        "minecraft:snow_layer",
        "minecraft:snow",
        "minecraft:soul_campfire",
        "minecraft:soul_fire",
        "minecraft:soul_lantern",
        "minecraft:soul_sand",
        "minecraft:soul_soil",
        "minecraft:soul_torch",
        "minecraft:sponge",
        "minecraft:spore_blossom",
        "minecraft:spruce_button",
        "minecraft:spruce_door",
        "minecraft:spruce_fence_gate",
        "minecraft:spruce_pressure_plate",
        "minecraft:spruce_stairs",
        "minecraft:spruce_standing_sign",
        "minecraft:spruce_trapdoor",
        "minecraft:spruce_wall_sign",
        "minecraft:stained_glass_pane",
        "minecraft:stained_glass",
        "minecraft:stained_hardened_clay",
        "minecraft:standing_banner",
        "minecraft:standing_sign",
        "minecraft:sticky_piston_arm_collision",
        "minecraft:sticky_piston",
        "minecraft:stone_block_slab",
        "minecraft:stone_block_slab2",
        "minecraft:stone_block_slab3",
        "minecraft:stone_block_slab4",
        "minecraft:stone_brick_stairs",
        "minecraft:stone_button",
        "minecraft:stone_pressure_plate",
        "minecraft:stone_stairs",
        "minecraft:stone",
        "minecraft:stonebrick",
        "minecraft:stonecutter_block",
        "minecraft:stripped_acacia_log",
        "minecraft:stripped_birch_log",
        "minecraft:stripped_crimson_hyphae",
        "minecraft:stripped_crimson_stem",
        "minecraft:stripped_dark_oak_log",
        "minecraft:stripped_jungle_log",
        "minecraft:stripped_mangrove_log",
        "minecraft:stripped_mangrove_wood",
        "minecraft:stripped_oak_log",
        "minecraft:stripped_spruce_log",
        "minecraft:stripped_warped_hyphae",
        "minecraft:stripped_warped_stem",
        "minecraft:structure_block",
        "minecraft:structure_void",
        "minecraft:sweet_berry_bush",
        "minecraft:tallgrass",
        "minecraft:target",
        "minecraft:tinted_glass",
        "minecraft:tnt",
        "minecraft:torch",
        "minecraft:trapdoor",
        "minecraft:trapped_chest",
        "minecraft:trip_wire",
        "minecraft:tripwire_hook",
        "minecraft:tuff",
        "minecraft:turtle_egg",
        "minecraft:twisting_vines",
        "minecraft:undyed_shulker_box",
        "minecraft:unlit_redstone_torch",
        "minecraft:unpowered_comparator",
        "minecraft:unpowered_repeater",
        "minecraft:verdant_froglight",
        "minecraft:vine",
        "minecraft:wall_banner",
        "minecraft:wall_sign",
        "minecraft:warped_button",
        "minecraft:warped_door",
        "minecraft:warped_double_slab",
        "minecraft:warped_fence_gate",
        "minecraft:warped_fence",
        "minecraft:warped_fungus",
        "minecraft:warped_hyphae",
        "minecraft:warped_nylium",
        "minecraft:warped_planks",
        "minecraft:warped_pressure_plate",
        "minecraft:warped_roots",
        "minecraft:warped_slab",
        "minecraft:warped_stairs",
        "minecraft:warped_standing_sign",
        "minecraft:warped_stem",
        "minecraft:warped_trapdoor",
        "minecraft:warped_wall_sign",
        "minecraft:warped_wart_block",
        "minecraft:water",
        "minecraft:waterlily",
        "minecraft:waxed_copper",
        "minecraft:waxed_cut_copper_slab",
        "minecraft:waxed_cut_copper_stairs",
        "minecraft:waxed_cut_copper",
        "minecraft:waxed_double_cut_copper_slab",
        "minecraft:waxed_exposed_copper",
        "minecraft:waxed_exposed_cut_copper_slab",
        "minecraft:waxed_exposed_cut_copper_stairs",
        "minecraft:waxed_exposed_cut_copper",
        "minecraft:waxed_exposed_double_cut_copper_slab",
        "minecraft:waxed_oxidized_copper",
        "minecraft:waxed_oxidized_cut_copper_slab",
        "minecraft:waxed_oxidized_cut_copper_stairs",
        "minecraft:waxed_oxidized_cut_copper",
        "minecraft:waxed_oxidized_double_cut_copper_slab",
        "minecraft:waxed_weathered_copper",
        "minecraft:waxed_weathered_cut_copper_slab",
        "minecraft:waxed_weathered_cut_copper_stairs",
        "minecraft:waxed_weathered_cut_copper",
        "minecraft:waxed_weathered_double_cut_copper_slab",
        "minecraft:weathered_copper",
        "minecraft:weathered_cut_copper_slab",
        "minecraft:weathered_cut_copper_stairs",
        "minecraft:weathered_cut_copper",
        "minecraft:weathered_double_cut_copper_slab",
        "minecraft:web",
        "minecraft:weeping_vines",
        "minecraft:wheat",
        "minecraft:white_candle_cake",
        "minecraft:white_candle",
        "minecraft:white_glazed_terracotta",
        "minecraft:wither_rose",
        "minecraft:wood",
        "minecraft:wooden_button",
        "minecraft:wooden_door",
        "minecraft:wooden_pressure_plate",
        "minecraft:wooden_slab",
        "minecraft:wool",
        "minecraft:yellow_candle_cake",
        "minecraft:yellow_candle",
        "minecraft:yellow_flower",
        "minecraft:yellow_glazed_terracotta"
]
while True:
    raw_input = input("Enter Command: ")

    if "$exit" in raw_input:
        break

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