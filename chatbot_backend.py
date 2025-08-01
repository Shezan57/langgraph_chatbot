from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

# define the llm model
llm = ChatOpenAI()

class ChatbotState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    
# Chatbot node
def chat_node(state: ChatbotState):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}


# Graph definition

# memory
checkpointer = InMemorySaver()
graph = StateGraph(ChatbotState)

# START--> chat_node --> END
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)




