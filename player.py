class Player:

    VERSION = "1.6 Back Panther"


    def betRequest(self, game_state):
        us = game_state["players"][game_state["in_action"]]
        hold = game_state["current_buy_in"] - us["bet"]
        my_cards = us["hole_cards"] + game_state["community_cards"]
        if self.check_flush(game_state):
            return hold + game_state['minimum_raise'] + us["stack"]
        if self.check_for_line(my_cards):
            return hold + game_state["minimum_raise"] + us["stack"] / 2
        if self.check_drill(my_cards):
            return us["stack"] / 3
        if self.check_for_pairs(my_cards):
            return hold + game_state["minimum_raise"] + us["stack"]/4
        if self.check_for_players_in(game_state) == False or self.check_for_high_card(us) == False:
            return 0
        if self.check_for_high_card(game_state, us):
                return hold + game_state["minimum_raise"] + us["stack"]/7
        return hold

    def showdown(self, game_state):
        pass

    def check_for_high_card(self, game_state, us):
        for card in us["hole_cards"]:
            if card["rank"] in "K A":
                return True

        for card2 in us["hole_cards"]:
            if card2["rank"] in "J Q K A":
                statuses = []
                for player in game_state["players"]:
                    if player["status"] == "out":
                        statuses.append("w")
                if len(statuses) >= 3:
                    return True
        return False


    def check_for_players_in(self, game_state):
        statuses = []
        for player in game_state["players"]:
            if player["status"] == "out":
                statuses.append("w")
        if len(statuses) == 4:
            return True
        else:
            return False



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

    def check_drill(self, my_cards):
        card_ranks = []
        for card in my_cards:
            card_ranks.append(card["rank"])
        if len(card_ranks) - len(set(card_ranks)) == 3:
            return True

    def check_for_line(self, my_cards):
        ranks = []
        line = 0
        for cards in my_cards:
            try:
                ranks.append(int(cards["rank"]))
            except ValueError:
                if cards["rank"] == "J":
                    ranks.append(10)
                elif cards["rank"] == "Q":
                    ranks.append(11)
                elif cards["rank"] == "K":
                    ranks.append(12)
                elif cards["rank"] == "A":
                    ranks.append(13)

        ranks.sort()

        for i in range(len(ranks) - 1):
            if (ranks[i + 1] - ranks[i]) == 1:
                line += 1
        if line >= 4:
            return True


    def check_royal_flush(self, my_cards):
        royal_flush_rank = []
        royal_flush_suit = []
        for card in my_cards:
            royal_flush_rank.append(card["rank"])
            royal_flush_suit.append(card["suit"])
        if 'A' and 'J' and 'Q' and 'K' and '10' in royal_flush_rank:
            same_cards = True
        if same_cards:
            if len(set(royal_flush_suit)) == 1:
                return True