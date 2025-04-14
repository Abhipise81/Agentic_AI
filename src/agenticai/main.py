import streamlit as st
import json
from src.agenticai.ui.streamlitui.loadui import LoadStreamLitUI
from src.agenticai.LLMS.groqllm import GroqLLM
from src.agenticai.graph.graph_builder import GraphBuilder
from src.agenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the langGraph AgenticAI application with streamlit UI.
    This function initializes the UI, handles user input, configures the LLM models,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.
    """

    # Load UI
    ui = LoadStreamLitUI()
    user_input = ui.load_streamlit_ui()
    # print(user_input,"aaaa")
    

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    # Text Input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")
    
    if user_message:
        try:
            # Configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
    
            if not model:
                st.error("Error: LLM Model could not be initialized")
                return
        
            # Initialize and setup the graph based on use case
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("Error: No Use case selected")
                return
            
            ### Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return
            
        except Exception as e:
            raise ValueError(f"Error Occurred with Exception : {e}")