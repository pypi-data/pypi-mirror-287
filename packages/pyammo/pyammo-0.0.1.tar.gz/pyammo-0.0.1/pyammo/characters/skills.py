class Skill(object):
    def __init__(self, skill: str, level: int, xp: int, max_xp: int):
        self.skill = skill
        self.level = level
        self.xp = xp
        self.max_xp = max_xp
