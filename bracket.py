class Stats:
    def __init__(self, wins = 0, losses = 0, alumNamedPatrickMahomes = 0):
        self.wins = wins
        self.losses = losses
        self.alumNamedPatrickMahomes = alumNamedPatrickMahomes

class Team:
    def __init__(self, name, seed, stats = None):
        self.name = name
        self.seed = seed
        self.stats = stats if stats else Stats()
    
class Matchup:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    
    def getWinner(self):
        team1 = self.team1
        team2 = self.team2
        if team1.stats.alumNamedPatrickMahomes != team2.stats.alumNamedPatrickMahomes:
            return team1 if team1.stats.alumNamedPatrickMahomes > team2.stats.alumNamedPatrickMahomes else team2
        elif team1.seed != team2.seed:
            return team1 if team1.seed < team2.seed else team2
        elif team1.stats.wins != team2.stats.wins:
            return team1 if team1.stats.wins > team2.stats.wins else team2
        elif team1.stats.losses != team2.stats.losses:
            return team1 if team1.stats.losses < team2.stats.losses else team2
        else:
            #Can't determine with stats, just pick whoever was team1
            return team1
            
    
class Bracket:
    def __init__(self, year, matchups):
        self.year = year
        self.matchups = matchups
        
    def getWinner(self, round = 0, matchups = None):
        if not matchups:
            matchups = self.matchups
        print(rounds[round])
        nextMatchups = []
        prevWinner = None
        for matchup in matchups:
            winner = matchup.getWinner()
            print("{} ({} vs {})".format(winner.name, matchup.team1.name, matchup.team2.name))
            if prevWinner:
                nextMatchups.append(Matchup(winner,prevWinner))
                prevWinner = None
            else:
                prevWinner = winner
        print("\n")
        if len(nextMatchups) > 0:
            self.getWinner(round + 1, nextMatchups)
    
rounds = ["Round of 64", "Round of 32", "Sweet 16", "Elite 8", "Final Four", "Championship"]
round = 0

matchups2021 = [#West
                Matchup(Team("Gonzaga", 1, Stats(26, 0)), Team("Norfolk State/Appalachian State", 16)),
                Matchup(Team("Oklahoma", 8), Team("Missouri", 9)),
                Matchup(Team("Creighton", 5), Team("UCSB", 12)),
                Matchup(Team("Virginia", 4), Team("Ohio", 13)),
                Matchup(Team("USC", 6), Team("Wichita/Drake", 11)),
                Matchup(Team("Kansas", 3), Team("Eastern Washington", 14)),
                Matchup(Team("Oregon", 7), Team("VCU", 10)),
                Matchup(Team("Iowa", 2), Team("Grand Canyon", 15)),
                
                #East
                Matchup(Team("Michigan", 1, Stats(20, 4)), Team("Mount Saint Mary's/Texas Southern", 16)),
                Matchup(Team("LSU", 8), Team("St Bonaventure", 9)),
                Matchup(Team("Colorado", 5), Team("Georgetown", 12)),
                Matchup(Team("Florida State", 4), Team("UNC Greensboro", 13)),
                Matchup(Team("BYU", 6), Team("Michigan State/UCLA", 11)),
                Matchup(Team("Texas", 3), Team("Abilene Christian", 14)),
                Matchup(Team("UConn", 7), Team("Maryland", 10)),
                Matchup(Team("Alabama", 2), Team("Iona", 15)),
                
                #Midwest
                Matchup(Team("Baylor", 1, Stats(22, 2)), Team("Hartford", 16)),
                Matchup(Team("UNC", 8), Team("Wisconsin", 9)),
                Matchup(Team("Villanova", 5), Team("Winthrop", 12)),
                Matchup(Team("Purdue", 4), Team("North Texas", 13)),
                Matchup(Team("Texas Tech", 6, Stats(17, 10, 1)), Team("Utah State", 11, Stats(20, 8))),
                Matchup(Team("Arkansas", 3), Team("Colgate", 14)),
                Matchup(Team("Florida", 7), Team("Virginia", 10)),
                Matchup(Team("Ohio State", 2), Team("Oral Roberts", 15)),
                
                #South
                Matchup(Team("Illinois", 1, Stats(22, 6)), Team("Drexel", 16)),
                Matchup(Team("Loyola Chicago", 8), Team("Georgia Tech", 9)),
                Matchup(Team("Tennessee", 5), Team("Oregon State", 12)),
                Matchup(Team("Oklahoma State", 4), Team("Liberty", 13)),
                Matchup(Team("San Diego State", 6), Team("Syracuse", 11)),
                Matchup(Team("West Virginia", 3), Team("Moorehead State", 14)),
                Matchup(Team("Clemson", 7), Team("Rutgers", 10)),
                Matchup(Team("Houston", 2), Team("Cleveland State", 15))
            ]

brackets = [Bracket(2021, matchups2021)]

brackets[0].getWinner()


