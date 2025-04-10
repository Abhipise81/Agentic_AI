from langgraph.graph import StateGraph, START,END, MessagesState
from langgraph.prebuilt import tools_condition,ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.agenticai.state.state import State
from src.agenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.agenticai.nodes.chatbot_with_Tool_node import ChatbotWithToolNode
from src.agenticai.tools.search_tool import get_tools, create_tool_node



class GraphBuilder:

    def __init__(self):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using langgraph.
        This method initialized a chatbot node using the "basicChatbotNode' class
        and integrates it into the graph. The chatobt node is set as both the entry
        and exit point of the graph.
        """

        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_build_graph(self):
        """
            Builds an advanced chatbot graph with tool integration.
            THis method creates a chatbot graph that includes both a chatbot node
            and toolnode. It defines tools, initializes the chatbot with tools 
            capabilites, and set up conditional and direct edges between nodes.
            This chatbot node is set as the entry point.
        """
        ## Define the tool and tool node


        tools = get_tools()
        tool_node = create_tool_node(tools)

        # Define LLM
        llm = self.llm

        # Define chatbot node
        obj_chatbot_with_node = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        # Add nodes
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        # Define conditional and direct edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools","chatbot")


    def setup_graph(self, usecase:str):
        """
        Sets up the graphs for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        
        if usecase == "Chatbot with Tool":
            self.chatbot_with_tools_build_graph()
        return self.graph_builder.compile()
        