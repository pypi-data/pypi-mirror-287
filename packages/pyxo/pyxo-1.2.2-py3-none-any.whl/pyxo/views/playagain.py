from pyxo.views.view import View


class PlayAgain(View):
    def print(self) -> str | None:
        return input("\n\ndo you want to play again (yes,no)")
