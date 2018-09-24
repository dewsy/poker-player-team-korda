
class Player:
    VERSION = "1.0 Black Widow"

    def betRequest(self, game_state):
        my_cards = []
        for i in game_state["players"]:
            if i["name"] == "team Korda":
                my_cards.append(i["hole_cards"])
        my_cards.append(game_state["community_cards"])
        for card in my_cards:
            for card2 in my_cards:
                if card["rank"] == card2["rank"]:
                    return 1000
        return 10

    def showdown(self, game_state):
        pass

