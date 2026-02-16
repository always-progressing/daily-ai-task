# CLI
import argparse
import json
from datetime import date
from app.services.daily_pipeline import run_daily_pipeline

def parse_args():
    parser = argparse.ArgumentParser(
        description="Run daily AI task pipeline"
    )
    parser.add_argument(
        "--date",
        type=str,
        help="Target date (YYYY-MM_DD), default=today",
    )
    parser.add_argument(
        "--force",
        action="store_true", # ignore cache and re-run all steps
        help="Force regeneration (ignores cache)",
    )

    return parser.parse_args()

def main():
    args = parse_args()

    target_date = None
    if args.date:
        target_date = date.fromisoformat(args.date)

    result = run_daily_pipeline(
        target_date=target_date,
        force=args.force,
    )
    # CLI 输出统一用 JSON（工程最佳实践）
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

