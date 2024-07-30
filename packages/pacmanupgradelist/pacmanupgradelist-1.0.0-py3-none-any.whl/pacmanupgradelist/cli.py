""" Pacman Upgrade list

    List the latest pacman upgrades and show them in a nice table

    Copyright (C) 2024  Marnix Enthoven

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import subprocess
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.table import Table

__version__ = "1.0.0"


def grep_pacman_log() -> str:
    """Run a grep process to get the Pacman log"""

    if not Path("/var/log/pacman.log").exists():
        raise FileNotFoundError("Pacman log not found!")

    return subprocess.run(
        ["grep", "-i", "upgraded", "/var/log/pacman.log"],
        capture_output=True,
        check=True,
    ).stdout.decode(encoding="utf-8")


def format_date(date: str) -> str:
    """Clean the date string and return formatted output in the format 31-12-2024 23:59"""
    clean_date = datetime.fromisoformat(date.split("[")[1].split("]")[0])
    return clean_date.strftime("%d-%m-%Y %H:%M")


def format_pacman_log(log: str, number_of_lines_tail: int = 100) -> Table:
    """Format pacman log"""
    lines = log.splitlines()[-number_of_lines_tail:]
    raw_table = []
    for item in lines:
        raw_table.append(item.split(" "))

    table = Table(title="Pacman upgrades")

    table.add_column("Upgrade date", justify="right", style="cyan", no_wrap=True)
    table.add_column("Package name", style="magenta")
    table.add_column("Old version", justify="right", style="red")
    table.add_column("New version", justify="left", style="green")

    for item in raw_table:
        table.add_row(
            format_date(item[0]), item[3], item[4].split("(")[1], item[6].split(")")[0]
        )

    return table


def main() -> None:
    """Main application function"""
    parser = argparse.ArgumentParser(
        prog="pacmanupgradelist",
        description="Get a formatted table of the last pacman upgrades",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        help="The number of latest upgraded packages to show [default: 100]",
        default=100,
    )
    args = parser.parse_args()

    log_string = grep_pacman_log()
    table = format_pacman_log(log_string, args.number)

    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()
