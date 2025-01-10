import language_tool_python

class GrammarChecker:
    async def correct(self, text: str) -> list:
        """Correct grammar and punctuation."""
        
        tool = language_tool_python.AsyncLanguageTool('en-US')
        result = await tool.check(text)
        
        # Initialize lists to store detected mistakes and their corrections  
        mistakes = []  
        corrections = []  
        start_positions = []  
        end_positions = []  

        # Iterate through the detected language errors  
        for rule in result:  
            if len(rule.replacements) > 0:  
                start_positions.append(rule.offset)  
                end_positions.append(rule.errorLength + rule.offset)  
                mistakes.append(text[rule.offset : rule.errorLength + rule.offset])  
                corrections.append(rule.replacements[0])   
        
        return list(zip(mistakes, corrections))
