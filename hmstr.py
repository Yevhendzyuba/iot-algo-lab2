class Hamster:
    def __init__(self, daily_norm, avarice):
        self.daily_norm = daily_norm
        self.avarice = avarice

    def __str__(self):
        return (f"Daily norm of humster:{self.daily_norm} avarice:{self.avarice}")