class Player:
    VERSION = "1.0 Black Widow"

    def betRequest(self, game_state):
        us = game_state["players"][game_state["in_action"]]
        hold = game_state["current_buy_in"] - us["bet"]
        my_cards = us["hole_cards"] + game_state["community_cards"]
        for card in my_cards:
            if card["rank"] in "2 3 4 5 6 7 8 9":
                return hold
        return hold + game_state["minimum_raise"] + 10

    def showdown(self, game_state):
        pass

