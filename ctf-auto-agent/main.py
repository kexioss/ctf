import argparse
from core.recon import ReconAgent
from core.exploit import ExploitAgent
from core.verify import VerifyAgent
from core.summary import SummaryAgent

def load_payloads():
    with open("data/payloads.txt") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()

    payloads = load_payloads()

    recon = ReconAgent()
    exploit = ExploitAgent(payloads)
    verify = VerifyAgent()
    summary = SummaryAgent()

    data = recon.run(args.url)
    findings = exploit.run(data)
    results = verify.run(findings)
    summary.run(results)

if __name__ == "__main__":
    main()
