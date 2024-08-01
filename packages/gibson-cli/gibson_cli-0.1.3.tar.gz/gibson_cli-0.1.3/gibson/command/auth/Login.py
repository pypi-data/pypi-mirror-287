from gibson.api.Cli import Cli
from gibson.command.BaseCommand import BaseCommand


class Login(BaseCommand):
    def execute(self):
        cli = Cli(self.configuration)
        access_token, refresh_token = cli.login()

        if access_token is None or refresh_token is None:
            self.conversation.newline()
            self.conversation.type(
                "Login failed, please try again with `gibson auth login`."
            )
        else:
            self.configuration.set_auth_tokens(access_token, refresh_token)
            self.conversation.type(f"Welcome! You are now logged in.")

        self.conversation.newline()
