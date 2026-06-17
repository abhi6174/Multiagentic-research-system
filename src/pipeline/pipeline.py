from src.agents.agents import build_search_agent,build_reader_agent,writer_chain,critiq_chain
from rich import print
import time

def run_research_pipeline(topic:str) -> dict:

    state ={}
    print("\n"+"="*50)
    print("search agent is running\n" )
    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages":[(
            "user",
            f"""
            Use the web_search tool to gather recent information about {topic}.
            Do not answer from your own knowledge.
            Search first, then provide findings.
            """
        )]
    })

    state["search_results"] = search_result["messages"][-1].content
    print("search result : ",search_result)
    print("\n"+"="*50)
    print("Reader agent is running\n")

    reader_agent= build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages":[("user",
            f"Based on the following search results about {topic}\n"
            f"pick the most relevant url and scrape it for deeper content.\n\n"
            f"Search results : {state['search_results'][:800]}"
        )]
    })
    state["scraped_content"] = reader_result["messages"][-1].content
    print("\nscraped content"+"-"*50+"\n")
    print(reader_result)

    print("\n"+"="*50)
    print("Writing draft report")
    print("="*50)
    
    research_content = (
        f"search result : \n{state['search_results']}\n"
        f"scraped content : \n{state['scraped_content']}\n"
    )
    state["report"] = writer_chain.invoke({
        "topic":topic,
        "research": research_content
    })

    print("\nFinal report : ",state["report"])

    state["Evaluation"] = critiq_chain.invoke({
        "report":state['report']
    })
    print("\n critiq :\n",state["Evaluation"])