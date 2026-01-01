class RoleBuilder:
    ROLES = ["UNDEFINED", "DEVELOPER", "TEST_ENGINEER", "SR_DEVELOPER", "DESIGNER"]

    @staticmethod
    def get_role_description(role_id):
        if 1 <= role_id <= 4:
            return RoleBuilder.ROLES[role_id]
        return "UNDEFINED"
