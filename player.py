class Player:

    VERSION = "1.1 Bruce Banner"


    def betRequest(self, game_state):
        us = game_state["players"][game_state["in_action"]]
        hold = game_state["current_buy_in"] - us["bet"]
        my_cards = us["hole_cards"] + game_state["community_cards"]
        if self.check_for_pairs(my_cards):
            return hold + game_state["minimum_raise"] + 100
        for card in my_cards:
            if card["rank"] in "2 3 4 5 6 7 8 9":
                return hold
        return hold + game_state["minimum_raise"] + 10

    def showdown(self, game_state):
        pass



    def check_for_pairs(self, my_cards):
        card_ranks = []
        seen = set()
        uniq = []
        for card in my_cards:
            card_ranks.append(card["rank"])
        for x in card_ranks:
            if x not in seen:
                uniq.append(x)
                seen.add(x)
            else:
                return True








    def check_flush(self, game_state):
        flush = []
        us = game_state["players"][game_state["in_action"]]
        my_cards = us["hole_cards"] + game_state["community_cards"]
        for card in my_cards:
            flush.append(card['suit'])
        if len(set(flush)) == 1:
            return True
        return False
