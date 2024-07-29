import asyncio
import aiohttp
from typing import Optional, List, Callable
from .gpt import Completion
from .search_text import search_text, search_text_async
from .selenium_scrapper import SeleniumScraper

class Tool:
    """
    Base class for tools used by agents.
    """
    async def use_tool(self, query):
        raise NotImplementedError("This method should be overridden by subclasses.")

class Agent:
    def __init__(self, name: str, backstory: str = "", verbose: bool = False, memory: bool = False,
                 output_goal: Optional[str] = None, model: Optional[str] = None, token: Optional[str] = None,
                 tools: Optional[List] = None, connect: bool = False):
        self.name = name
        self.backstory = backstory
        self.verbose = verbose
        self.memory = memory
        self.output_goal = output_goal
        self.model = model
        self.token = token
        self.tools = tools or []
        self.connect = connect
        self.completion = Completion()

    async def _create_async(self, prompt: str) -> str:
        if self.model and self.token:
            headers = {"Authorization": f"Bearer {self.token}"}
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url=f"https://api.openai.com/v1/engines/{self.model}/completions",
                    headers=headers,
                    json={"prompt": prompt}
                ) as resp:
                    data = await resp.json()
                    return data.get("choices", [{}])[0].get("text", "Error: Unable to generate text.")
        else:
            return await self.completion.create_async(prompt)

    async def generate_with_search(self, query: str, max_results: int = 5) -> str:
        search_results = await search_text_async(query, max_results)
        context = "\n".join([f"Title: {result.get('title')}\nBody: {result.get('body')}" for result in search_results])
        prompt = f"Using the following information:\n{context}\n\nAnswer the following question:\n{query}"
        return await self._create_async(prompt)

    async def create_prompt_template(self, query: str) -> str:
        context = f"Agent Name: {self.name}\nBackstory: {self.backstory}\n\nQuery: {query}\n"
        if self.tools:
            tool_contexts = await asyncio.gather(*[tool.use_tool(query) for tool in self.tools])
            tool_context = "\n\n".join(tool_contexts)
            context += f"\n\nTools:\n{tool_context}"
        return context

    async def generate_response(self, query: str) -> str:
        prompt = await self.create_prompt_template(query)
        response = await self._create_async(prompt)
        if self.connect:
            return await self._connected_agents_response(response)
        return response

    async def _connected_agents_response(self, initial_response: str) -> str:
        for tool in self.tools:
            if isinstance(tool, Agent):
                response = await tool.generate_response(initial_response)
                return response
        return initial_response


class CustomTool(Tool):
    def __init__(self, name, tool_logic):
        self.name = name
        self.tool_logic = tool_logic

    async def use_tool(self, query):
        """
        Use the custom tool with the given query.

        Args:
            query (str): The query to use with the custom tool.

        Returns:
            str: The result from the custom tool.
        """
        return await self.tool_logic(query)
    
class WebScraper(Tool):
    def __init__(self, name, base_url):
        self.name = name
        self.base_url = base_url

    async def scrape(self, path):
        """
        Scrape content from the specified path on the base URL.

        Args:
            path (str): The path to scrape content from.

        Returns:
            str: The scraped content.
        """
        url = f"{self.base_url}{path}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    raise Exception(f"Failed to scrape {url}. Status code: {response.status}")

    async def use_tool(self, query):
        """
        Use the web scraper as a tool to fetch and return content based on the query.

        Args:
            query (str): The query to determine the path for scraping.

        Returns:
            str: The result from the web scraper.
        """
        # For simplicity, let's assume the query is directly the path to scrape
        return await self.scrape(query)