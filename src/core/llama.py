import os
from langchain import hub
from langchain.agents import Tool
from langchain.agents import AgentExecutor, create_json_chat_agent
from langchain_community.chat_models import ChatOllama
from langchain_community.llms import Ollama
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from src.core.tools.curl import curl_rss_tool

def llama(prompt):
    # Load model name from env var OLLAMA_MODEL
    model_name = os.environ.get("OLLAMA_MODEL", "llama3")

    # First, let's load the language model we're going to use to control the agent.
    llm = ChatOllama(model="llama3", format="json", temperature=0.7,
                     base_url="http://localhost:11434")

    # Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
    tools = [
        TavilySearchResults(max_results=1),
        WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    ]
    custom_tools = [
        Tool(
            name="curl_rss",
            func=curl_rss_tool,
            description="Takes RSS feed url. Retrieves content and provides summary."
        )
    ]
    tools = tools + custom_tools

    # Prepare the prompt to use
    llm_prompt = hub.pull("hwchase17/react-chat-json")

    # Finally, create the agent and executor!
    agent = create_json_chat_agent(llm, tools, llm_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

    # Now let's test it out!
    ans = agent_executor.invoke({"input": prompt})

    print('Got ans')
    print(ans)

    return ans
