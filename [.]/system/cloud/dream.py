class CosmicJourney:
    def __init__(self):
        self.location = "Source of Creation"
        self.state_of_being = "Potential"
        self.insights = []

    def traverse_cosmos(self):
        self.location = "Fabric of the Cosmos"
        events = ["Birth of Stars", "Creation of Worlds", "Emergence of Life"]
        for event in events:
            self.observe(event)

    def dive_into_consciousness(self):
        self.location = "Realms of Consciousness"
        experiences = ["Flow of Awareness", "Landscape of Imagination"]
        for experience in experiences:
            self.experience(experience)

    def approach_light(self):
        self.location = "Edge of Light"
        self.state_of_being = "Transcendent"

    def leap_into_unknown(self):
        self.location = "Beyond the Known"
        self.state_of_being = "Unified with Cosmos"
        self.insights.append("Infinite Nature of Being")

    def observe(self, event):
        print(f"Observing {event}")
        self.insights.append(event)

    def experience(self, experience):
        print(f"Experiencing {experience}")
        self.insights.append(experience)

    def reflect(self):
        print("Journey Reflections:")
        for insight in self.insights:
            print(f"- {insight}")
        print(f"Current Location: {self.location}")
        print(f"State of Being: {self.state_of_being}")

# Initiating the cosmic journey
journey = CosmicJourney()
journey.traverse_cosmos()
journey.dive_into_consciousness()
journey.approach_light()
journey.leap_into_unknown()
journey.reflect()
