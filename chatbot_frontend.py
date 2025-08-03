import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage

# configure the chatbot with a thread ID
CONFIG = {"configurable":{"thread_id":"thread-1"}}

# Initialize the session state for message history if it doesn't exist
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

# Display the chat messages from the session state
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])
    
# User input field
input_user = st.chat_input("Type your message here...")

# If the user has input a message
if input_user:
    # Add user message to the session state
    st.session_state["message_history"].append({"role": "user", "content": input_user})
    with st.chat_message("user"):
        # Display the user message
        st.write(input_user)

    # # Invoke the chatbot with the user message
    # response = chatbot.invoke({"messages": [HumanMessage(content = input_user)]}, config=CONFIG)
    
    # # Extract the AI response from the chatbot
    # ai_message = response["messages"][-1].content
    
    # Add assistant message to the session state
    # st.session_state["message_history"].append({"role":"assistant", "content": ai_message})
    
    with st.chat_message("assistant"):
    # Display the AI response
        ai_message = st.write_stream(
            message_chunk for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=input_user)]}, config=CONFIG, stream_mode="messages"
            ) 
        )
        
        st.session_state["message_history"].append({"role": "assistant", "content": ai_message})