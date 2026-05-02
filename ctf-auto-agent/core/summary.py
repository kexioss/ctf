import os
from datetime import datetime
from utils.logger import success

class SummaryAgent:
    def run(self, results):
        if not os.path.exists("reports"):
            os.makedirs("reports")

        filename = f"reports/report_{datetime.now().timestamp()}.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write("# CTF Agent Scan Report\n\n")

            if not results:
                f.write("No vulnerabilities found.\n")
            else:
                for r in results:
                    f.write(f"## Param: {r['param']}\n")
                    f.write(f"- Payload: `{r['payload']}`\n")
                    f.write(f"- Confidence: {r['confidence']}\n")
                    f.write(f"- Evidence:\n```\n{r['evidence']}\n```\n\n")

        success(f"Report saved: {filename}")
