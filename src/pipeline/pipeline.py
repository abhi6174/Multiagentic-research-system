from src.agents.agents import build_reader_agent,writer_chain,critiq_chain
from src.tools.tools import web_search
from rich import print

def run_research_pipeline(topic:str) -> dict:

    state ={}
    print("\n"+"="*50)
    print("search tool is running\n" )

    state["search_results"]  = web_search.invoke({
        "query":topic
    })

    print("search result : ",state["search_results"])
    print("\n"+"="*50)
    print("Reader agent is running\n")

    reader_agent= build_reader_agent()
    reader_result = reader_agent.invoke(
        {
            "messages":[("user",
                f"""
                Based on these search results about {topic},
                Use the scraper tool to select the most important urls and extract important informations
                Search results : {state['search_results']}
                """
            )]
        }
    )
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

    return state