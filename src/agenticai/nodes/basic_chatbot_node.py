from src.agenticai.state.state import State

class BasicChatbotNode:
    """
    Basic chatbot logic implementation
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Process the input state and generates a chatbot response,
        """
        print({"messages": self.llm.invoke(state["messages"])},"aaa")
        return {"messages": self.llm.invoke(state["messages"])}