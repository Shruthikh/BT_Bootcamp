# NEW in Lab-11:
# Role description logic isolated in RoleBuilder
class RoleBuilder:
    @staticmethod
    def get_role_description(role):
        if role is None:
            return "UNDEFINED"
        return role.name
