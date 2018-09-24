class Player:

    VERSION = "1.2.3 Bruce Banner"


    def betRequest(self, game_state):
        us = game_state["players"][game_state["in_action"]]
        hold = game_state["current_buy_in"] - us["bet"]
        my_cards = us["hole_cards"] + game_state["community_cards"]
        if self.check_for_pairs(my_cards):
            return hold + game_state["minimum_raise"] + us["stack"]/4
        for card in us["hole_cards"]:
            if card["rank"] in "J Q K A":
                return hold + game_state["minimum_raise"] + us["stack"]/10
        return hold

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
        if len(game_state['community_cards']) == 3:
            if len(set(flush)) == 1:
                return True
        else:
            if flush.count('spades') == 5 or flush.count('clubs') == 5 or flush.count('diamonds') == 5 or flush.count('hearts') == 5:
                    return True
        return False
