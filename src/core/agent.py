from langchain.agents import load_tools, Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from src.core.tools.curl import curl_rss_tool


def agent(prompt):
    # First, let's load the language model we're going to use to control the agent.
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
    llm = OpenAI(model_name="text-davinci-003", temperature=0)
    tools = load_tools(["llm-math", "wikipedia"], llm=llm)
    custom_tools = [
        Tool(
            name="curl_rss",
            func=curl_rss_tool,
            description="Takes RSS feed url. Retrieves content and provides summary."
        )
    ]
    tools = tools + custom_tools

    # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
    agent = initialize_agent(
        tools,
        chat,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True)

    # Now let's test it out!
    ans = agent.run(prompt)

    print('Got ans')
    print(ans)

    return ans
