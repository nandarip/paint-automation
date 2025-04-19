import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
from google import genai
from concurrent.futures import TimeoutError
from functools import partial

# Load environment variables from .env file
load_dotenv()

# Access your API key and initialize Gemini client correctly
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

max_iterations = 3
last_response = None
iteration = 0
iteration_response = []

async def generate_with_timeout(client, prompt, timeout=10):
    """Generate content with a timeout"""
    print("Starting LLM generation...")
    try:
        # Convert the synchronous generate_content call to run in a thread
        loop = asyncio.get_event_loop()
        response = await asyncio.wait_for(
            loop.run_in_executor(
                None, 
                lambda: client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
            ),
            timeout=timeout
        )
        print("LLM generation completed")
        return response
    except TimeoutError:
        print("LLM generation timed out!")
        raise
    except Exception as e:
        print(f"Error in LLM generation: {e}")
        raise

async def main():
    try:
        # Create server parameters
        server_params = StdioServerParameters(
            command="python",
            args=["mcp_server.py"]
        )
        
        # Create client connection
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize session
                await session.initialize()
                
                # Get available tools
                tools_result = await session.list_tools()
                tools = tools_result.tools
                print(f"Available tools: {[tool.name for tool in tools]}")
                
                # Example: Call a tool (replace with actual tool name and parameters)
                try:
                    result = await session.call_tool("example_tool", arguments={"param1": "value1"})
                    print(f"Tool result: {result}")
                except Exception as e:
                    print(f"Error calling tool: {e}")
                
    except Exception as e:
        print(f"Error in main execution: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
    
    