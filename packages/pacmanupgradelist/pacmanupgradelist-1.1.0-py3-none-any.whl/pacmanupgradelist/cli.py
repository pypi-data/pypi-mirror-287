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
from datetime import date, datetime
from pathlib import Path

from rich.console import Console
from rich.table import Table

__version__ = "1.1.0"


def grep_pacman_log() -> list[str]:
    """Run a grep process to get the Pacman log"""

    if not Path("/var/log/pacman.log").exists():
        raise FileNotFoundError("Pacman log not found!")

    grep_result = subprocess.run(
        ["grep", "-i", "upgraded", "/var/log/pacman.log"],
        capture_output=True,
        check=True,
    ).stdout.decode(encoding="utf-8")
    return grep_result.splitlines()


def format_date(input_date: str) -> datetime:
    """Clean the input date string formatted as `[2024-07-30T11:09:44+0200]`
    and return datetime object"""
    return datetime.fromisoformat(input_date.split("[")[1].split("]")[0])


def process_log(log: list[str]) -> dict[date, list[str]]:
    """Process the Pacman log and return a dictionary with date as key,
    and package update contents as a list value."""

    upgrade_runs = {}
    for line in log:
        line_items = line.split()
        line_datetime = format_date(line_items[0])
        if line_datetime.date() in upgrade_runs:
            upgrade_runs.get(line_datetime.date(), []).append(line_items)
        else:
            upgrade_runs[line_datetime.date()] = [line_items]
    return upgrade_runs


def create_cli_table(
    upgrade_runs: dict[date, list[str]], number_of_upgrades_back: int = 1
) -> Table:
    """Format pacman log
    Extract the requested number of upgrade runs from the log dict"""
    raw_table = []
    counter = 0
    for item in reversed(upgrade_runs):
        if counter < number_of_upgrades_back:
            raw_table.append(upgrade_runs.get(item))
            counter += 1
        else:
            break

    table = Table(title="Pacman upgrades")

    table.add_column("Upgrade date", justify="right", style="cyan", no_wrap=True)
    table.add_column("Package name", style="magenta")
    table.add_column("Old version", justify="right", style="red")
    table.add_column("New version", justify="left", style="green")

    # Add the rows to the displayed table
    # Format of an item is:
    # ['[2024-07-26T15:15:09+0200]','[ALPM]','upgraded','pangomm-2.48','(2.52.0-1','->','2.54.0-1)']

    for upgrade_run in reversed(raw_table):
        for item in upgrade_run:
            table.add_row(
                format_date(item[0]).strftime("%d-%m-%Y %H:%M"),
                item[3],
                item[4].split("(")[1],
                item[6].split(")")[0],
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
        help="The number of upgrade runs to show [default: 1]",
        default=1,
    )
    args = parser.parse_args()

    pacman_log_contents = grep_pacman_log()
    processed_log = process_log(pacman_log_contents)
    table = create_cli_table(processed_log, args.number)

    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()
