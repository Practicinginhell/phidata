from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.llm.g4f import G4F

assistant = Assistant(llm=G4F(),
                      tools=[DuckDuckGo()],
                      show_tool_calls=True)
assistant.print_response("Whats happening in France?", markdown=True)
