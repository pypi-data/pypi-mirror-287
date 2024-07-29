import argparse
import json
from pathlib import Path

from caseflow.debug_case_step import debug_case_step
from caseflow.run_case import parse_har


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command", title="commands", metavar="")

    # 创建 debug_case_step 子命令
    debug_case_step_parser = subparsers.add_parser(
        "debug_case_step", help="调试caseflow文件"
    )
    debug_case_step_parser.add_argument(
        "businessJsonFilePath", type=str, help="业务文件路径"
    )
    debug_case_step_parser.add_argument(
        "--no-log", action="store_false", dest="showLog", help="不展示日志"
    )

    # 创建 parse_har 子命令
    parse_har_parser = subparsers.add_parser(
        "parse_har", help="解析har接口录制文件，转换caseflow格式"
    )
    parse_har_parser.add_argument("harFilePath", type=str, help="har文件路径")

    args = parser.parse_args()

    if args.command == "debug_case_step":
        result = debug_case_step(args.businessJsonFilePath, args.showLog)
        print("\033[1;32moutput:\033[0m")
        print(json.dumps(result.output, indent=4, ensure_ascii=False))
        print("\n\033[1;32mCookies:\033[0m")
        for domain, cookies in result.cookie_jar._cookies.items():
            print(f"{domain}: {cookies}")
    elif args.command == "parse_har":
        result = parse_har(Path(args.harFilePath))
        print(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
