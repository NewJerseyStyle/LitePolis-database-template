from typing import Dict, Any, List

from .Users import UserManager
from .Conversations import ConversationManager

class DatabaseActor(UserManager, ConversationManager):
    pass