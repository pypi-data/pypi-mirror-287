class Slot(object):
    def __init__(self, content: str, quantity: int):
        self.content = content
        self.quantity = quantity


class Equipment(object):
    def __init__(
        self,
        weapon_slot: str = None,
        shield_slot: str = None,
        helmet_slot: str = None,
        body_armor_slot: str = None,
        leg_armor_slot: str = None,
        boots_slot: str = None,
        ring1_slot: str = None,
        ring2_slot: str = None,
        amulet_slot: str = None,
        artifact1_slot: str = None,
        artifact2_slot: str = None,
        artifact3_slot: str = None,
        consumable1_slot: str = None,
        consumable1_slot_quantity: int = 0,
        consumable2_slot: str = None,
        consumable2_slot_quantity: int = 0,
    ):
        self.weapon_slot = Slot(weapon_slot, 1)
        self.shield_slot = Slot(shield_slot, 1)
        self.helmet_slot = Slot(helmet_slot, 1)
        self.body_armor_slot = Slot(body_armor_slot, 1)
        self.leg_armor_slot = Slot(leg_armor_slot, 1)
        self.boots_slot = Slot(boots_slot, 1)
        self.ring_slots = [Slot(ring1_slot, 1), Slot(ring2_slot, 1)]
        self.amulet_slot = Slot(amulet_slot, 1)
        self.artifact_slots = [
            Slot(artifact1_slot, 1),
            Slot(artifact2_slot, 1),
            Slot(artifact3_slot, 1),
        ]
        self.consumable_slots = [
            Slot(consumable1_slot, consumable1_slot_quantity),
            Slot(consumable2_slot, consumable2_slot_quantity),
        ]


class Inventory(object):
    def __init__(self, data: list, inventory_max_items: int = 20):
        self.slots = [None for _ in range(inventory_max_items)]
        for slot_data in data:
            self.slots[slot_data["slot"]] = Slot(
                slot_data["code"], slot_data["quantity"]
            )
        self.max_items = inventory_max_items
