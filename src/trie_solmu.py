class TrieSolmu:
    """Solmu trie-tietorakenteessa.
    """
    def __init__(self, nuotti):
        self.nuotti = nuotti
        self.nuottijonon_frekvenssi = 0
        self.lapsisolmut = {}
        self.vika_nuotti = False

    def __str__(self):
        return f"({self.nuotti}, {self.nuottijonon_frekvenssi})"#str(self.nuotti) #, str(self.nuottijonon_frekvenssi), str(self.lapsisolmut), str(self.vika_nuotti)"