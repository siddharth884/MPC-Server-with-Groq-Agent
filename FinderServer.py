from mcp.server.fastmcp import FastMCP
import os
mcp = FastMCP("KeywordFinder")

@mcp.tool()
def check_keyword(path: str, keyword: str) -> str:
    """
    Checks if the given keyword exists in the file or folder at the path.
    If folder, searches recursively in text files.
    """
    found = False
    results = []

    if os.path.isfile(path):
        found = _check_in_file(path, keyword, results)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for f in files:
                file_path = os.path.join(root, f)
                _check_in_file(file_path, keyword, results)
    else:
        return f"Invalid path: {path}"

    if results:
        return f"Keyword '{keyword}' found in:\n" + "\n".join(results)
    else:
        return f"Keyword '{keyword}' not found in any file."

def _check_in_file(file_path, keyword, results):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            if keyword in f.read():
                results.append(file_path)
                return True
    except Exception as e:
        pass
    return False

if __name__ == "__main__":
    mcp.run(transport="stdio")