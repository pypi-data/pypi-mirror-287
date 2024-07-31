from zentra_api.cli.constants.enums import AddItem, DefaultFolderOptions

from pydantic import BaseModel


class CreateItem(BaseModel):
    """"""

    item: AddItem
    folder: DefaultFolderOptions
