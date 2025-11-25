# natstat-cli

A command line interface for the National Statistical API

## Installation

The CLI can be installed with pip.

```bash
git clone https://github.com/jhelderman/natstat-cli.git
cd natstat-cli
pip install .
```

## Configuration

This CLI requires an API key for National Statistical. This can be acquired
from the [NatStat website](natstat.com). The API key is configured with an
environment variable.

```bash
export NATSTAT_API_KEY=change-me
```

## Usage

The CLI has a subcommand for each endpoint. These can be seen in the help
message for the base command.

```
❯ natstat --help
Usage: natstat [OPTIONS] COMMAND [ARGS]...

  Query the NatStat API

Options:
  --help  Show this message and exit.

Commands:
  games        Game data
  leaguecodes  League codes
  moneyline    Moneyline records
  overunder    Over/Under records
  playbyplay   Play-by-play data
  playerperfs  Player performance data
  players      Player data
  pointspread  Point spread records
  seasons      Season info
  teamcodes    Team codes
  teamperfs    Team performance data
  teams        Team data
  venues       Venue data
```

Each subcommand has a help message that shows the available options.

```bash
natstat games --help
```

The following command queries for the NBA games that were played on
2025-11-23. Results are output to the standard output in CSV format.

```bash
natstat games --date 2025-11-23 --service nba
```

NatStat responses are paginated to limit the number of records per
response. This CLI automatically requests all the pages for a given
request. For example, the following command will fetch the NBA game
data for the 2022 season.

```bash
natstat games --season 2022 --service nba
```

To disable this behavior and only fetch one page, pass the `--one-page`
flag.

```bash
natstat games --season 2022 --service nba --one-page
```
