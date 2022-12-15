# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 01:05:17 2020

@author: nikla
"""
from itertools import count
import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', None)


class LizUnit:
    _ids = count(0)
    def __init__(self, number, name, type, unit_prize):
        self.number = number
        self.name = name
        self.type = type
        self.unit_prize = unit_prize
        self.cost = self.number*self.unit_prize
        self.id = next(self._ids)
        self.text = f"{self.number} {self.name}. "
        
    def Command_add_ons(self, cmd_add_on, cmd_prize):
        self.cost = self.cost + cmd_prize
        self.text = self.text + f"Command: {cmd_add_on}. "
    
    def Weapons_add_ons(self, wpn_add_on, wpn_prize):
        self.cost = self.cost + wpn_prize*self.number
        self.text = self.text + f"Weapons: {wpn_add_on}. "
        
    def Mount_add_ons(self, mount_add_on, mount_prize):
        self.cost = self.cost + mount_prize
        self.text = self.text + f"Mount: {mount_add_on}. "
        
    def MagicItems_add_ons(self, MagicItems_add_on, MagicItems_prize, Magic_effect):
        self.cost = self.cost + MagicItems_prize
        self.text = self.text + f"Magic Items: {MagicItems_add_on}, {Magic_effect}. "
        
    def BlessedSpawning_add_ons(self, BlessedSpawning_add_on, BS_prize, BS_effect):
        self.cost = self.cost + BS_prize*self.number
        self.text = self.text + f"Blessed Spawning: {BlessedSpawning_add_on}, {BS_effect}. "
        
    def SpecialEffect_add_ons(self, SpecialEffs_add_on, SpecialEffs_prize, Special_effect):
        self.cost = self.cost + SpecialEffs_prize
        self.text = self.text + f"Special Effect: {SpecialEffs_add_on}, {Special_effect}. "
        
    def print_unit(self):
        print(f"{self.number} {self.name}. Type '{self.type}'. Total points: {self.cost}.")
        try:
            print(f"Add ons: {self.cmd}")
        except:
            pass
        print(f"Instance id {self.id}")
        print(" ")
    
    def data(self):
        self.text = self.text + f"Cost: {self.cost}"
        return (self.number, self.name, self.type, self.cost, self.text)

def seperate_units(list_unit):
    lord_list = []
    hero_list = []
    core_list = []
    special_list = []
    rare_list = []
    lord_text_list = []
    hero_text_list = []
    core_text_list = []
    special_text_list = []
    rare_text_list = []
    index = 0
    while index < len(list_unit):
        if list_unit[index][2] == "Lord":
            lord_list.append(list_unit[index][3])
            lord_text_list.append(list_unit[index][4])
        elif list_unit[index][2] == "Hero":
            hero_list.append(list_unit[index][3])
            hero_text_list.append(list_unit[index][4])
        elif list_unit[index][2] == "Core":
            core_list.append(list_unit[index][3])
            core_text_list.append(list_unit[index][4])
        elif list_unit[index][2] == "Special":
            special_list.append(list_unit[index][3])
            special_text_list.append(list_unit[index][4])
        elif list_unit[index][2] == "Rare":
            rare_list.append(list_unit[index][3])
            rare_text_list.append(list_unit[index][4])
        index += 1
    print("________________________________ARMY LIST________________________________")
    print("__________________________________Lords__________________________________")
    [print(x) for x in lord_text_list]
    print(" ")
    print("__________________________________Heros__________________________________")
    [print(x) for x in hero_text_list]
    print(" ")
    print("__________________________________Core___________________________________")
    [print(x) for x in core_text_list]
    print(" ")
    print("_________________________________Special_________________________________")
    [print(x) for x in special_text_list]
    print(" ")
    print("__________________________________Rare___________________________________")
    [print(x) for x in rare_text_list]
    print(" ")
    Sums = [sum(lord_list), sum(hero_list), sum(core_list), sum(special_list), sum(rare_list)]
    return Sums

def check_army_points(Tot_points, sum_lists):
    Lord_points_max = Tot_points*0.25
    Hero_points_max = Tot_points*0.25
    LH_points_max = Tot_points*0.35
    Core_points_min = Tot_points*0.25
    Special_points_max = Tot_points*0.5
    Rare_points_max = Tot_points*0.25
    
    LH_spent = sum_lists[0] + sum_lists[1]
    
    Lord_check = Lord_points_max - sum_lists[0]
    Hero_check = Hero_points_max - sum_lists[1]
    LH_check = LH_points_max - LH_spent
    Core_check = Core_points_min - sum_lists[2]
    Special_check = Special_points_max - sum_lists[3]
    Rare_check = Rare_points_max - sum_lists[4]
    Points_left = Tot_points-sum(sum_lists)
    if Lord_check >= 0:
        L_str = 'You can add more points for Lords ^.^'
    else:
        L_str = 'Too many points for Lords! Scrab some! >_<'
    if Hero_check >= 0:
        H_str = 'You can add more points for Heros ^.^'
    else:
        H_str = 'Too many points for Heros! Scrab some! >_<'
    if LH_check >= 0:
        LH_str = 'You can add more points for L&Hs ^.^'
    else:
        LH_str = 'Too many points for L&Hs! Scrab some! >_<'
    if Core_check <= 0:
        Core_str = 'You have enough points for Core ^.^'
    else:
        Core_str = 'You need to add more Core points! >_<'
    if Special_check >= 0:
        Spec_str = 'You can add more points for Special ^.^'
    else:
        Spec_str = 'Too many points, Special! Scrab some! >_<'
    if Rare_check >= 0:
        Rare_str = 'You can add more points for Rare ^.^'
    else:
        Rare_str = 'Too many points for Rare! Scrab some! >_<'
    if Points_left >= 0:
        too_many_points_str = " "
    else:
        too_many_points_str = "         TOO MANY POINTS!!!"
    print(" ")
    print("_______________________________ARMY POINTS_______________________________")
    print(f"Points left: {Points_left}" + too_many_points_str)
    d = {'Type': ['Lords:','Heros:','L & H:','Core:','Special:','Rare:'],
         'Max/Min': [Lord_points_max, Hero_points_max, LH_points_max, Core_points_min, Special_points_max, Rare_points_max], 
         'Spent': [sum_lists[0], sum_lists[1], LH_spent, sum_lists[2], sum_lists[3], sum_lists[4]], 
         'Balance': [Lord_check, Hero_check, LH_check, Core_check, Special_check, Rare_check],
         'Status': [L_str,H_str,LH_str,Core_str,Spec_str,Rare_str]}
    df = pd.DataFrame(data=d).set_index('Type')
    print(df)
    

    
Total_points = 2000

oldblood = LizUnit(1, "Oldblood", 'Lord', 150)
oldblood.Mount_add_ons("Carnosaur", 175)
oldblood.SpecialEffect_add_ons("Loping Stride", 5, "+1 Movement")
oldblood.MagicItems_add_ons("Talisman of Preservation and Obsidian Blade", 45+25, "4+ Ward Save and Ignores Armour Saves")
oldblood.BlessedSpawning_add_ons("Blessed Mark of the Old Ones", 10, "Reroll 3 dices")

skinkChief = LizUnit(1, "Skink Chief", "Hero", 35)
skinkChief.SpecialEffect_add_ons("B.S.B.", 25, "Hold your Ground!")
skinkChief.Weapons_add_ons("Javelin + Shield", 6)

Tettoeko = LizUnit(1, "Tetto'eko", "Hero", 190)

skinkPriest = LizUnit(1, "Skink Priest", "Hero", 60)
skinkPriest.SpecialEffect_add_ons("Lvl Up!", 35, "Lvl 2 Mage")
skinkPriest.Mount_add_ons("Troglodon",150)
skinkPriest.MagicItems_add_ons("Armour of Destiny", 50, "Heavy armour and 4+ Ward save")

skinks1 = LizUnit(10, "Skink Skirmishers", "Core", 7)
skinks1.Weapons_add_ons("Javelin & Shields", 1)
skinks1.Command_add_ons("Patrol leader", 10)
skinks1.BlessedSpawning_add_ons("B.S. of Quetzl", 1, "Natural armour +1")

skinks2 = LizUnit(10, "Skink Skirmishers", "Core", 7)
skinks2.Weapons_add_ons("Javelin & Shields", 1)
skinks2.Command_add_ons("Patrol leader", 10)
skinks2.BlessedSpawning_add_ons("B.S. of Quetzl", 1, "Natural armour +1")

skinksCohort = LizUnit(24, "Skink cohort", "Core", 3)
skinksCohort.Weapons_add_ons("Javelin", 3)
skinksCohort.Command_add_ons("FC", 30)
skinksCohort.BlessedSpawning_add_ons("B.S. of Quetzl", 1, "Natural armour +1")

warriors = LizUnit(28, "Saurus Warriors", "Core", 11)
warriors.Command_add_ons("FC", 30)
warriors.Weapons_add_ons("Spears", 1)
warriors.BlessedSpawning_add_ons("B.S. of Quetzl", 1, "Natural armour +1")

coldOne = LizUnit(8, "Cold One Riders", "Special", 24)
coldOne.Command_add_ons("Musician",10)
coldOne.BlessedSpawning_add_ons("B.S. of Quetzl", 2, "Natural armour +1")

ripperdactyl = LizUnit(3, "Ripperdactyl Riders", "Special", 37)
ripperdactyl.BlessedSpawning_add_ons("B.S. of Quetzl", 2, "Natural armour +1")

templeGuards = LizUnit(15, "Temple Guard", "Special", 17)
templeGuards.Command_add_ons("FC",30)
templeGuards.BlessedSpawning_add_ons("B.S. of Quetzl", 1, "Natural armour +1")

salamander = LizUnit(1, "Salamander Hunting Pack", "Rare", 80)

razordon = LizUnit(1, "Razordon Hunting Pack", "Rare", 60)

bastiladon = LizUnit(1, "Bastiladon", "Rare", 210)
bastiladon.SpecialEffect_add_ons("Solar Engine",40,"+1 Initiative 6 inches and Laser")

kroxi = LizUnit(3, "Kroxigor", "Special", 43)
kroxi.Command_add_ons("Kroxigor Ancient",10)
kroxi.BlessedSpawning_add_ons("B.S. of Quetzl", 3, "Natural armour +1")

HornedOnes = LizUnit(5,'Horned One Riders','Special',19)
HornedOnes.Command_add_ons("Musician", 5)
HornedOnes.Weapons_add_ons("Javelins", 3)

stegadon = LizUnit(1, 'Ancient Stegadon', 'Rare', 220)
stegadon.SpecialEffect_add_ons("Unstoppable Stampede", 10, "Devastating Charge")


list_units = [skinkPriest.data(),
              oldblood.data(), stegadon.data(), bastiladon.data(),
              skinks1.data(), skinks2.data(), coldOne.data(),
              warriors.data()]
sum_lists = seperate_units(list_units)
check_army = check_army_points(Total_points, sum_lists)





