from langchain.community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot.
    """
    tools = [TavilySearchResults(max_result=2)]
    return tools

def create_tool_node(tools):
    """
    Create and returns a tool node from the graph
    """
    return ToolNode(tools=tools)
