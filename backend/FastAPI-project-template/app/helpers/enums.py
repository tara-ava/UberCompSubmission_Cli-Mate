import enum


class UserRole(enum.Enum):
    ADMIN_ROLE = 'administrators'
    USER_ROLE = 'users'
    GUEST_ROLE = 'guests'

class PartnerRole(enum.Enum):
    RC = 'recycler'
    RW = 'reward'

class WasteType(enum.Enum):
    PLASTIC = 'plastic'
    PAPER = 'paper'
    GLASS = 'glass'
    METAL1 = 'metal1'
    METAL2 = 'metal2'
    METAL3 = 'metal3'

