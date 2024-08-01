import datetime
from .skins import Skin
from .skills import Skill
from .elemental_powers import ElementalPower
from .positions import Position
from .possesions import Equipment, Inventory
from ..client import Client


class Character(object):
    def __init__(self, client: Client, name: str):
        self._client = client
        self.name = name
        self.update_from_server()
        self.cooldown_expiration = None

    def update_from_server(self):
        data = self._client.get_character_data(self.name)
        self.update_from_data(data)

    def update_from_data(self, data: dict):
        self.skin = data["skin"]
        self.level = data["level"]
        self.xp = data["xp"]
        self.max_xp = data["max_xp"]
        self.total_xp = data["total_xp"]
        self.gold = data["gold"]
        self.speed = data["speed"]
        mining_skill = Skill(
            "mining", data["mining_level"], data["mining_xp"], data["mining_max_xp"]
        )
        woodcutting_skill = Skill(
            "woodcutting",
            data["woodcutting_level"],
            data["woodcutting_xp"],
            data["woodcutting_max_xp"],
        )
        fishing_skill = Skill(
            "fishing", data["fishing_level"], data["fishing_xp"], data["fishing_max_xp"]
        )
        weaponcrafting_skill = Skill(
            "weaponcrafting",
            data["weaponcrafting_level"],
            data["weaponcrafting_xp"],
            data["weaponcrafting_max_xp"],
        )
        gearcrafting_skill = Skill(
            "gearcrafting",
            data["gearcrafting_level"],
            data["gearcrafting_xp"],
            data["gearcrafting_max_xp"],
        )
        jewelrycrafting_skill = Skill(
            "jewelrycrafting",
            data["jewelrycrafting_level"],
            data["jewelrycrafting_xp"],
            data["jewelrycrafting_max_xp"],
        )
        cooking_skill = Skill(
            "cooking", data["cooking_level"], data["cooking_xp"], data["cooking_max_xp"]
        )
        self.skills = {
            "mining": mining_skill,
            "woodcutting": woodcutting_skill,
            "fishing": fishing_skill,
            "weaponcrafting": weaponcrafting_skill,
            "gearcrafting": gearcrafting_skill,
            "jewelrycrafting": jewelrycrafting_skill,
            "cooking": cooking_skill,
        }
        self.hp = data["hp"]
        self.haste = data["haste"]
        self.critical_strike = data["critical_strike"]
        self.stamina = data["stamina"]
        fire_power = ElementalPower(
            "fire", data["attack_fire"], data["dmg_fire"], data["res_fire"]
        )
        earth_power = ElementalPower(
            "earth", data["attack_earth"], data["dmg_earth"], data["res_earth"]
        )
        water_power = ElementalPower(
            "water", data["attack_water"], data["dmg_water"], data["res_water"]
        )
        air_power = ElementalPower(
            "air", data["attack_air"], data["dmg_air"], data["res_air"]
        )
        self.elemental_powers = {
            "fire": fire_power,
            "earth": earth_power,
            "water": water_power,
            "air": air_power,
        }
        self.position = Position(data["x"], data["y"])
        self.cooldown = data["cooldown"]
        self.cooldown_expiration = data["cooldown_expiration"]
        self.equipment = Equipment(
            data["weapon_slot"],
            data["shield_slot"],
            data["helmet_slot"],
            data["body_armor_slot"],
            data["leg_armor_slot"],
            data["boots_slot"],
            data["ring1_slot"],
            data["ring2_slot"],
            data["amulet_slot"],
            data["artifact1_slot"],
            data["artifact2_slot"],
            data["artifact3_slot"],
            data["consumable1_slot"],
            data["consumable1_slot_quantity"],
            data["consumable2_slot"],
            data["consumable2_slot_quantity"],
        )
        self.inventory_max_items = data["inventory_max_items"]
        self.inventory = Inventory(data["inventory"], self.inventory_max_items)

    def move(self, position: Position = None, x: int = None, y: int = None):
        if position is not None:
            x = position.x
            y = position.y
        elif x is None or y is None:
            raise ValueError("Either position or x and y must be provided.")
        data = self._client.move_character(self.name, x, y)
        self.update_from_data(data["character"])
        self.cooldown_expiration = datetime.datetime.now() + datetime.timedelta(
            seconds=data["cooldown"]["remainingSeconds"]
        )

    def __str__(self):
        return f"<Character: {self.name} @ {self.position} - Level {self.level} - {self.hp} HP - {self.gold} gold>"
