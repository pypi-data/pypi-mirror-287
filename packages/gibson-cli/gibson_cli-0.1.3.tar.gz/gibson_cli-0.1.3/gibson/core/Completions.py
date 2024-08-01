import os


class Completions:
    def __init__(self):
        self.user_home = os.environ.get("HOME")
        self.gibson_config = ".gibsonai"

    def install(self):
        completions_location = f"$HOME/{self.gibson_config}/bash_completion"
        installation = f"""\n[ -s "{completions_location}" ] && \\. "{completions_location}" # Load gibson auto completion\n"""

        with open(f"{self.user_home}/.bashrc", "r+") as f:
            if completions_location not in f.read():
                f.write(installation)

        with open(f"{self.user_home}/.zshrc", "r+") as f:
            if completions_location not in f.read():
                f.write(installation)

        return self

    def write(self):
        try:
            file = os.path.dirname(__file__) + f"/../data/bash-completion.tmpl"
            with open(file, "r") as f:
                contents = f.read()
        except FileNotFoundError:
            return self

        completions = f"{self.user_home}/{self.gibson_config}/bash_completion"
        with open(completions, "w") as f:
            f.write(contents)

        return self
