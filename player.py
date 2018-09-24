class Player:
    VERSION = "1.0 Black Widow"

    def betRequest(self, game_state):
        us = game_state["players"][game_state["in_action"]]
        hold = game_state["current_buy_in"] - us["bet"]
        my_cards = us["hole_cards"] + game_state["community_cards"]

        for card in my_cards:
            if card["rank"] in "J Q K A":
                return hold
        return hold + game_state["minimum_raise"] + 10

    def showdown(self, game_state):
        pass

    def check_drill(self, my_cards):
        seen = set()
        uniq = []
        for x in my_cards:
            if x not in seen:
                uniq.append(x)
                seen.add(x)
                if uniq - seen == 3:
                    return True
        return False
