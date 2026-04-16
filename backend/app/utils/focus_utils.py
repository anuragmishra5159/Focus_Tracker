from urllib.parse import urlparse
import re # regular expressions: used when scanning a string or url

# here we specify which the categories of sites
PRODUCTIVE_DOMAINS = {
    "github.com", "gitlab.com", "bitbucket.org",
    "stackoverflow.com", "stackexchange.com",
    "developer.mozilla.org", "docs.python.org",
    "medium.com", "dev.to", "hashnode.com",
    "coursera.org", "udemy.com", "edx.org", "khanacademy.org",
    "leetcode.com", "hackerrank.com", "codewars.com",
    "notion.so", "trello.com", "jira.atlassian.com",
    "linear.app", "figma.com",
    "aws.amazon.com", "cloud.google.com", "azure.microsoft.com",
    "npmjs.com", "pypi.org", "hub.docker.com",
    "replit.com", "codesandbox.io", "codepen.io",
    "wikipedia.org", "arxiv.org",
    "openai.com", "anthropic.com",
}

PRODUCTIVE_PATTERNS = [
    r"^docs\.",
    r"^api\.",
    r"^learn\.",
    r"^academy\.",
    r"^tutorial\.",
    r"^developer\.",
]

DISTRACTING_DOMAINS = {
    "youtube.com", "youtu.be",
    "instagram.com", "facebook.com", "twitter.com", "x.com",
    "tiktok.com", "snapchat.com",
    "netflix.com", "primevideo.com", "disneyplus.com", "hulu.com",
    "twitch.tv", "reddit.com",
    "9gag.com", "buzzfeed.com",
    "pinterest.com",
    "whatsapp.com", "telegram.org",
    "gaming.com", "steampowered.com",
    "espn.com", "sports.yahoo.com",
}

NEUTRAL_DOMAINS = {
    "google.com", "bing.com", "duckduckgo.com",
    "gmail.com", "outlook.com", "yahoo.com",
    "news.google.com", "bbc.com", "cnn.com",
    "amazon.com", "ebay.com",
    "maps.google.com",
}

# Functions 

def extract_domain(url: str) -> str: #convert a url into a domain name
    try:
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except Exception as e:
        print(f"Error extracting domain from URL '{url}': {e}")
        return ""
    

def calculate_focus_score(productive_time: float, total_time: float) -> float:
    if total_time == 0:
        return 0.0
    score = (productive_time / total_time) * 100
    return round(min(score, 100.0), 1)