class TrieSolmu:
    """Solmu trie-tietorakenteessa.
    """

    def __init__(self, nuotti: int):
        """Liittää solmuun lähtötiedot.

        Args:
            nuotti: kyseisen solmun nuotti lukuna.
        """
        self.nuotti = nuotti
        self.nuottijonon_frekvenssi = 0
        self.lapsisolmut = {}

    def palauta_frekvenssi(self):
        """Auttaa hakemaan haluttuun solmuun liittyvän osanuottijonon frekvenssin.

        Returns:
            int: nuottijonon frekvenssi
        """
        return self.nuottijonon_frekvenssi
