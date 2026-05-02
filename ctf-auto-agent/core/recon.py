from utils.logger import info

class ReconAgent:
    def run(self, url):
        info("Recon: analyzing target")
        return {
            "url": url,
            "params": ["id", "q", "search", "file"]
        }
