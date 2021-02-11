# Press the green button in the gutter to run the script.
from math import log2

import treeNode
import fpGrowth

import time

start_time = time.time()


# take bac names from bacttaxa of marine and animal
def bacteria_names():
    file = open("bactTaxa_Habitat.txt", "r")
    Marine_Bac_Names = open("Marine_Bac_Names.txt", "w")
    Animal_Bac_Names = open("Animal_Bac_Names.txt", "w")
    lines = file.readlines()
    for line in lines:
        split_line = line.split(";")
        if len(split_line) == 11:
            if split_line[10] == "Animal\n":
                Animal_Bac_Names.write(split_line[1])
                Animal_Bac_Names.write("\n")
            elif split_line[10] == "Marine Environment\n":
                name = split_line[1]
                Marine_Bac_Names.write(name)
                Marine_Bac_Names.write("\n")


# take all words of animal\marine bac from cog_word_bac
# read all names and put the words in file
# build dict{bac_name, {words_list, lable}}
# animal = lable 1 , marine = lable 0
def write_words(function_cogs_list):
    dict = {}
    Marine_Bac_Names = open("Marine_Bac_Names.txt", "r")
    Animal_Bac_Names = open("Animal_Bac_Names.txt", "r")
    cog_word_bac_animal = open("cog_word_bac_animal.txt", "w")
    cog_word_bac_marine = open("cog_word_bac_marine.txt", "w")
    cog_words_bac = open("cog_words_bac.txt", "r")

    lines_cog_word_bac = cog_words_bac.readlines()
    lines_animal_names = Animal_Bac_Names.readlines()

    # count how many marine bac and how many animal bac
    marine_counter = 0
    animal_counter = 0

    # take names from bac_names
    for i in range(0, len(lines_animal_names)):
        lines_animal_names[i] = lines_animal_names[i][:-1]
    lines_marine_names = Marine_Bac_Names.readlines()
    for i in range(0, len(lines_marine_names)):
        lines_marine_names[i] = lines_marine_names[i][:-1]
    # pass all cog_bac_name and take words of animal and marine
    for line in lines_cog_word_bac:
        split_line = line.split("#")
        bac_name = split_line[3]
        if bac_name in lines_animal_names:
            animal_word_list = (split_line[4]).split("\t")
            animal_word_list.pop(0)
            # if this bac has been writen in dict before - we add the word to the list if not excist already
            if bac_name in dict.keys():
                for item in animal_word_list:
                    if item != "X" and item != "\n":
                        if item not in dict[bac_name][0]:
                            if item in function_cogs_list:
                                dict[bac_name][0].append(item)
                                cog_word_bac_animal.write(item)
                                cog_word_bac_animal.write(", ")
                            # translate cog to letter
                            # for key, value in info_dict.items():
                            # if item in value:
                            # letter = key
                            # cog_word_bac_animal_letter.write(letter)
                            # cog_word_bac_animal_letter.write(", ")
            # new transaction
            else:
                is_transaction_empty = 0
                for item in animal_word_list:
                    if item != "X" and item != "\n":
                        if item in function_cogs_list:
                            if is_transaction_empty == 0:
                                animal_counter += 1
                                dict[bac_name] = {}
                                dict[bac_name][0] = []
                                dict[bac_name][1] = 1
                                cog_word_bac_animal.write("\n")
                                is_transaction_empty = 1
                            dict[bac_name][0].append(item)
                            cog_word_bac_animal.write(item)
                            cog_word_bac_animal.write(", ")
                            # for key, value in info_dict.items():
                            # if item in value:
                            # letter = key
                            # cog_word_bac_animal_letter.write(letter)
                            # cog_word_bac_animal_letter.write(", ")

        if bac_name in lines_marine_names:
            marine_word_list = (split_line[4]).split("\t")
            marine_word_list.pop(0)
            if bac_name in dict.keys():
                for item in marine_word_list:
                    if item != "X" and item != "\n":
                        if item not in dict[bac_name][0]:
                            if item in function_cogs_list:
                                dict[bac_name][0].append(item)
                                cog_word_bac_marine.write(item)
                                cog_word_bac_marine.write(", ")
                            # for key, value in info_dict.items():
                            # if item in value:
                            # letter = key
                            # cog_word_bac_marine_letter.write(letter)
                            # cog_word_bac_marine_letter.write(", ")
            else:
                is_transaction_empty = 0
                # cog_word_bac_marine_letter.write("\n")
                for item in marine_word_list:
                    if item != "X" and item != "\n":
                        if item in function_cogs_list:
                            if is_transaction_empty == 0:
                                marine_counter += 1
                                dict[bac_name] = {}
                                dict[bac_name][0] = []
                                dict[bac_name][1] = 0
                                cog_word_bac_marine.write("\n")
                                is_transaction_empty = 1
                            dict[bac_name][0].append(item)
                            cog_word_bac_marine.write(item)
                            cog_word_bac_marine.write(", ")
                            # for key, value in info_dict.items():
                            # if item in value:
                            # letter = key
                            # cog_word_bac_marine_letter.write(letter)
                            # cog_word_bac_marine_letter.write(", ")

    Marine_Bac_Names.close()
    Animal_Bac_Names.close()
    cog_word_bac_animal.close()
    cog_word_bac_marine.close()
    # cog_word_bac_marine_letter.close()
    # cog_word_bac_animal_letter.close()
    cog_words_bac.close()

    return dict, animal_counter, marine_counter


def filter_dict(to_remove_list, dict):
    filtered_dict = dict.copy()
    for value in filtered_dict.values():
        for cog in value[0]:
            if cog in to_remove_list:
                value[0].remove(cog)
    return filtered_dict


# claculate entropy given 2 class
def entropy(class0, class1):
    if class0 == 0 or class1 == 0:
        return 0
    return -(class0 * log2(class0) + class1 * log2(class1))


# gain = s_entropy - (8/20 * s1_entropy + 12/20 * s2_entropy)
# claculate IG from frequent itemset
# return IG, class_0, class_1
def calcul_IG(freq_item_set, dict, class1, class0, total_entropy):
    data_size = class0 + class1
    s1_class0 = 0
    s1_class1 = 0
    s2_class0 = 0
    s2_class1 = 0
    for v in dict.values():
        v_set = set(v[0])
        if freq_item_set.issubset(v_set):
            if v[1] == 1:
                s1_class1 += 1
            else:
                s1_class0 += 1
        else:
            if v[1] == 1:
                s2_class1 += 1
            else:
                s2_class0 += 1

    # if itemset is very discriminative - s1_entropy = 0
    if s1_class0 + s1_class1 == 0:
        s1_class0_0 = 0
        s1_class1_1 = 0
    else:
        s1_class0_0 = s1_class0 / (s1_class0 + s1_class1)
        s1_class1_1 = s1_class1 / (s1_class1 + s1_class0)
    if s2_class1 + s2_class0 == 0:
        s2_class0_0 = 0
        s2_class1_1 = 0
    else:
        s2_class0_0 = s2_class0 / (s2_class1 + s2_class0)
        s2_class1_1 = s2_class1 / (s2_class1 + s2_class0)
    s1_entropy = (entropy(s1_class0_0, s1_class1_1))
    s2_entropy = (entropy(s2_class0_0, s2_class1_1))
    gain = total_entropy - (
            ((s1_class0 + s1_class1) / data_size) * s1_entropy + ((s2_class0 + s2_class1) / data_size) * s2_entropy)
    return gain, s1_class1, s1_class0


# given an itemset, delete transaction that contain this itemset
def remove_item_from_dict(dict, myitem):
    # if v_set.issubset(myitem):
    for k, v in dict.copy().items():
        v_set = set(v[0])
        print("V_SET:")
        print(v_set)
        if myitem.issubset(v_set):
            del dict[k]

# build dict {letter, [cogs_list]}, check what cogs belong to which letter in COG_INFO_TABLE
def build_info_dict():
    file = open("COG_INFO_TABLE.txt", "r")
    dict_info = {}
    for line in file.readlines():
        lines = line.split(";")
        cog_num = lines[0][3:]
        if lines[1] in dict_info.keys():
            dict_info[lines[1]].append(cog_num)
        else:
            new_list = [cog_num]
            dict_info[lines[1]] = new_list
    file.close()
    return dict_info


# return list of all cogs that under the category
def build_category_list(category):
    file = open("COG_INFO_TABLE.txt", "r")
    category_cogs_list = []
    for line in file.readlines():
        lines = line.split(";")
        cog_num = lines[0][3:]
        for i in range(3,len(lines)-1):
            if lines[i] == category:
                category_cogs_list.append(cog_num)
    file.close()
    return category_cogs_list


# return dict{letter, num_of_appereance}
# how many time a letter from info_table (letter = process in the bacteria such as metabolism)
# appear in specific lable
# example : how many time J appears in animal bacterias
def lable_info(info_dict, lable):
    info_lable = {}
    if lable == 1:
        file = open("cog_word_bac_animal.txt", "r")
    else:
        file = open("cog_word_bac_marine.txt", "r")

    for line in file.readlines():
        lines = line.split(", ")
        for word in lines:
            for key, value in info_dict.items():
                if word in value:
                    letter = key
                    if letter in info_lable.keys():
                        info_lable[letter] += 1
                    else:
                        info_lable[letter] = 1
    file.close()
    return info_lable


# sort dict
def sort_dict(dict1):
    sorted_values = sorted(dict1.values())  # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in dict1.keys():
            if dict1[k] == i:
                sorted_dict[k] = dict1[k]
                break
    return sorted_dict


# turns list to set e.g take all items that appears more then once
def turn_list_to_set(lable):
    if lable == 0:
        file = open("cog_word_bac_marine_letter.txt", "r")
        print("----marine letters----")
    else:
        file = open("cog_word_bac_animal_letter.txt", "r")
        print("----animal letters----")
    list_trans = []
    lines = file.readlines()
    for line in lines:
        trans_cog_list = []
        trans = line.split(", ")
        for cog in trans:
            if cog not in trans_cog_list:
                trans_cog_list.append(cog)
        list_trans.append(trans_cog_list)

    print(list_trans)


# filter the transactions and take out all cogs that appears in al transactions
def cog_word_bac_filtered(label, to_remove_list):
    if label == 0:
        file = open("cog_word_bac_marine.txt", "r")
        filtered_file = open("cog_word_bac_marine_filtered.txt", "w")
    else:
        file = open("cog_word_bac_animal.txt", "r")
        filtered_file = open("cog_word_bac_animal_filtered.txt", "w")
    lines = file.readlines()
    del lines[0]
    for line in lines:
        cog_list = line.split(", ")
        for cog in cog_list:
            if cog not in to_remove_list and cog != "\n":
                filtered_file.write(cog)
                filtered_file.write(", ")
        filtered_file.write("\n")
    file.close()
    filtered_file.close()


if __name__ == '__main__':

    # takes all bacterias names from bactTaxa_Habitant that are animal or marine
    bacteria_names()
    category = "Lipid transport and metabolism"
    # list of all cogs that belong to catagory
    function_cogs_list = build_category_list(category)

    # dict = {bac_name, {words_list, lable}}
    dict, animal_counter, marine_counter = write_words(function_cogs_list)

    min_sup = 100
    output = open("output.txt", "w")
    simpDat = fpGrowth.loadSimpDat(dict)
    initSet = fpGrowth.createInitSet(simpDat)
    myFPtree, myHeaderTab = fpGrowth.createTree(initSet, min_sup)
    if not myHeaderTab:
        print("header table empty")
        print("--- %s seconds ---" % (time.time() - start_time))
        exit(1)
    freqItems = []
    fpGrowth.mineTree(myFPtree, myHeaderTab, min_sup, set([]), freqItems)

    class0 = marine_counter / (marine_counter + animal_counter)
    class1 = animal_counter / (marine_counter + animal_counter)
    Hc = entropy(class0, class1)
    dict_IG_freq = {}

    # claculate IG to all the frequent itemsets, returns also how many time each freq_itemset appears in lable 1 and 0
    for item_set in freqItems:
        ig, lable1_count, lable0_count = calcul_IG(item_set, dict, animal_counter, marine_counter, Hc)
        dict_IG_freq[frozenset(item_set)] = [ig, lable0_count, lable1_count]

    # sort all freq_itemsets by IG
    sorted_freqItemSet_by_ig = sorted(dict_IG_freq.items(), key=lambda item: item[1][0])

    # write the 10 itemsets with the best IG to "output.txt"
    for i in range(0, 10):
        if len(sorted_freqItemSet_by_ig)!= 0 :
            most_dist_trans = sorted_freqItemSet_by_ig.pop()
            max_ig_freq_itemset = list(most_dist_trans[0])
            max_ig = most_dist_trans[1][0]
            max_lable0 = most_dist_trans[1][1]
            max_lable1 = most_dist_trans[1][2]
            num_of_genome = max_lable1 + max_lable0
            output_string = "itemset: " + str(max_ig_freq_itemset) + ", IG: " + str(
                max_ig) + ", Num genomes contain : " + str(num_of_genome) + ", Animal : " + str(
                max_lable1) + ", Marine : " + str(max_lable0) + "\n"
            output.write(output_string)

    print("--- %s seconds ---" % (time.time() - start_time))
