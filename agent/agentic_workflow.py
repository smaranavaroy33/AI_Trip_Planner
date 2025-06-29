from utils.model_loader import load_model
from prompt_library import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessageState, END, START
from langgraph.prebuilt import ToolNode, tools_conditions 

class GraphBuilder():
    def __init__(self):
        self.system_prompt = SYSTEM_PROMPT

    def agent_function(self, state: MessageState):
        ## Main Agent Function
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages": [response]}

    def build_graph(delf):
        graph_builder = StateGraph(MessageState) 
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent", tools_conditions)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)
        self.graph = graph_builder.compile()
        return self.graph


    def __call__(self):
        return self.build_graph()

