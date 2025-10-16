from string import Template


class ValidatedTemplate(Template):
    def __init__(self, template: str):
        super().__init__(template)
        self._validate()

    def _validate(self) -> None:
        if self.is_valid():
            return

        invalids = [
            matched
            for matched in self.pattern.finditer(self.template)
            if matched.group("invalid")
        ]
        error_msgs = []
        for matched in invalids:
            try:
                self._invalid(matched)
            except ValueError as e:
                error_msgs.append(str(e))
        raise ValueError("\n".join(error_msgs))
