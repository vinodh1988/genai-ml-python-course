class Team:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members if members is not None else []
    
    def __add__(self, other):
        if not isinstance(other, Team):
            raise TypeError("Can only add Team objects together")
        combined_members = self.members + other.members
        return Team(f"{self.name} + {other.name}", combined_members)
    
    def __repr__(self):
        return f"Team(name='{self.name}', members={self.members})"

team1 = Team("Team A", ["Alice", "Bob"])
team2 = Team("Team B", ["Charlie", "Diana"])
    
combined_team = team1 + team2
print(combined_team)