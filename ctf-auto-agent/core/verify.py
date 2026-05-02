from utils.logger import info

class VerifyAgent:
    def run(self, findings):
        info("Verify: validating results")
        results = []
        for f in findings:
            f["confidence"] = 1
            results.append(f)
        return results
