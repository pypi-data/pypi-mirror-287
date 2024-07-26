from enum import Enum

class permission(Enum):
    MODIFY_CONTENT="content",
    MODIFY_TYPE="type",
    DELETE_DOMAIN="delete",
    VIEW_DETAILS="details"