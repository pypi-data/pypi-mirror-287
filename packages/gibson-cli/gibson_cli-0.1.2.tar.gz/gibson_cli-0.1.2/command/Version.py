from conf.Version import Version as VersionConf
from .BaseCommand import BaseCommand


class Version(BaseCommand):
    def execute(self):
        self.conversation.type(VersionConf.num)
        return True
