import sys
import os

# Set core path
CORE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "core_project/core"))
sys.path.append(CORE_DIR)

# Import collect_contexts
from core_project.MCP.mcp import collect_contexts

def test_integration():
    print("--- Testing Time/Weather (No Input) ---")
    print(collect_contexts(["time", "weather"]))
    
    print("\n--- Testing Wikipedia (Input: 'who is Elon Musk') ---")
    print(collect_contexts(["wiki"], user_input="who is Elon Musk"))
    
    print("\n--- Testing Command (Input: 'open google') ---")
    print(collect_contexts(["open_site"], user_input="open google"))
    
    print("\n--- Testing Web Search (Input: 'search python tutorials') ---")
    print(collect_contexts(["web_search"], user_input="search python tutorials"))

if __name__ == "__main__":
    test_integration()
