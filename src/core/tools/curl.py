import subprocess
from langchain.agents import tool


@tool("curl")
def curl_rss_tool(url: str) -> str:
    """Retrieves the contents of a URL using curl, and parse it as text."""
    curl_cmd = ["curl", url]
    txt_cmd = ["html2text"]
    sumy_cmd = ["sumy", "lex-rank", "--length=12"]

    curl_proc = subprocess.Popen(curl_cmd, stdout=subprocess.PIPE)
    txt_proc = subprocess.Popen(txt_cmd, stdin=curl_proc.stdout, stdout=subprocess.PIPE)
    sumy_proc = subprocess.Popen(sumy_cmd, stdin=txt_proc.stdout, stdout=subprocess.PIPE)

    output, _ = sumy_proc.communicate()
    return output.decode()
