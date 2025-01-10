from app.agents.plot_architect import PlotArchitectAgent

class StoryCreationWorkflow:
    def __init__(self):
        self.plot_agent = PlotArchitectAgent()

    async def run(self, context: dict, event):
        # Step 1: Generate plot
        context = await self.plot_agent.run(context)
        


        # Add more steps as needed
        return context
