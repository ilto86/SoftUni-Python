from project.blade_knight import BladeKnight
from project.dark_knight import DarkKnight
from project.dark_wizard import DarkWizard
from project.elf import Elf
from project.hero import Hero
from project.knight import Knight
from project.muse_elf import MuseElf
from project.soul_master import SoulMaster
from project.wizard import Wizard

hero = Hero("Hero", 4)
elf = Elf("Elf", 5)
muse_elf = MuseElf("Muse_Elf", 15)
wizard = Wizard("Wizard", 10)
dark_wizard = DarkWizard("Dark_Wizard", 20)
soul_master = SoulMaster("Soul_Master", 30)
knight = Knight("Knight", 20)
dark_knight = DarkKnight("Dark_Knight", 40)
blade_knight = BladeKnight("Blade_Knight", 60)



print("===" * 50)
print(f"First {hero.__class__.__bases__[0].__name__}")
print("===" * 50)
print(str(hero))
print(hero.username)
print(hero.level)
print("===" * 50)
print("===" * 50)
print("===" * 50)
print(f"Inheritance from --> class {elf.__class__.__bases__[0].__name__}")
print("===" * 50)
print(str(elf))
print(elf.username)
print(elf.level)
print("===" * 50)
print("===" * 50)
print("===" * 50)
print(f"Inheritance from --> class {muse_elf.__class__.__bases__[0].__name__}")
print("===" * 50)
print(str(muse_elf))
print(muse_elf.username)
print(muse_elf.level)
print("===" * 50)
print("===" * 50)
print("===" * 50)
print(f"Inheritance from --> class {wizard.__class__.__bases__[0].__name__}")
print("===" * 50)
print(str(wizard))
print(wizard.username)
print(wizard.level)
print("===" * 50)
print("===" * 50)
print("===" * 50)
print(f"Inheritance from --> class {dark_wizard.__class__.__bases__[0].__name__}")
print("===" * 50)
print(str(dark_wizard))
print(dark_wizard.username)
print(dark_wizard.level)
print("===" * 50)
print("===" * 50)
print("===" * 50)
print(f"Inheritance from --> class {soul_master.__class__.__bases__[0].__name__}")
print("===" * 50)
print(str(soul_master))
print(soul_master.username)
print(soul_master.level)
print("===" * 50)
print("===" * 50)
print("===" * 50)
print(f"Inheritance from --> class {knight.__class__.__bases__[0].__name__}")
print("===" * 50)
print(str(knight))
print(knight.username)
print(knight.level)
print("===" * 50)
print("===" * 50)
print("===" * 50)
print(f"Inheritance from --> class {dark_knight.__class__.__bases__[0].__name__}")
print("===" * 50)
print(str(dark_knight))
print(dark_knight.username)
print(dark_knight.level)
print("===" * 50)
print("===" * 50)
print("===" * 50)
print(f"Inheritance from --> class {blade_knight.__class__.__bases__[0].__name__}")
print("===" * 50)
print(str(blade_knight))
print(blade_knight.username)
print(blade_knight.level)
print("===" * 50)





'''Exception Output 
H
4
H of type Hero has level 4
E of type Elf has level 4
Hero
E
4  
'''