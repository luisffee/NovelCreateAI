from app.agents.base_agent import BaseAgent

class PlotArchitectAgent(BaseAgent):
    async def run(self, context: dict):
        prompt = context.get("plot_idea", "Create a new plot")
        raw_plot = await self.llm_tool.generate(prompt)
        corrected_plot = self.grammar_checker.correct(raw_plot)

        context["plot"] = corrected_plot
        return context
