from loader import dp
from .group import IsGroup
from .admin import IsAdmin
from .forbidden_messages import IsForbiddenMessage
from .notify import IsNotifyUser
from .edit import IsEditCommand


if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsForbiddenMessage)
    dp.filters_factory.bind(IsNotifyUser)
    dp.filters_factory.bind(IsEditCommand)
