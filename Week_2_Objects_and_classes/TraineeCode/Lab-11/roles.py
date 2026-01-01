from enum import Enum

# NEW in Lab-11:
# Roles converted from constants to Enum for type safety
class Roles(Enum):
    DEVELOPER = 1
    TEST_ENGINEER = 2
    SR_DEVELOPER = 3
    DESIGNER = 4
