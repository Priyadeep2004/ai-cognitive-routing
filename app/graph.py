from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph
from app.tools import mock_searxng_search
from app.personas import personas
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class State(dict):
    pass


def decide_node(state):
    persona = personas[state["bot_id"]]

    prompt = f"""
    You are this persona:
    {persona}

    Decide a topic to post about and generate a search query.

    Return JSON:
    {{"topic": "...", "query": "..."}}
    """

    res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

    data = eval(res.choices[0].message.content)

    return {**state, **data}


def search_node(state):
    results = mock_searxng_search.invoke(state["query"])
    return {**state, "context": results}


def draft_node(state):
    persona = personas[state["bot_id"]]

    prompt = f"""
    Persona:
    {persona}

    Topic: {state['topic']}
    Context: {state['context']}

    Write a strong opinionated tweet under 280 chars.

    Return JSON:
    {{"bot_id": "{state['bot_id']}", "topic": "...", "post_content": "..."}}
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return eval(res.choices[0].message.content)


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("decide", decide_node)
    graph.add_node("search", search_node)
    graph.add_node("draft", draft_node)

    graph.set_entry_point("decide")

    graph.add_edge("decide", "search")
    graph.add_edge("search", "draft")

    graph.set_finish_point("draft")

    return graph.compile()