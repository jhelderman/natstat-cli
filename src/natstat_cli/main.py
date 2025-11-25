import logging
import sys

import click
from natstat import (
    GamesReq,
    LeagueCodesReq,
    MoneylineReq,
    NatStatAPIv3,
    NatStatError,
    NatStatReq,
    NatStatResp,
    OverunderReq,
    PlayByPlayReq,
    PlayerPerfsReq,
    PlayersReq,
    PointSpreadReq,
    SeasonsReq,
    TeamCodesReq,
    TeamPerfsReq,
    TeamsReq,
    VenuesReq,
    paginated_get_all,
)
from natstat.paginated import PaginatedResp

from natstat_cli.util import model_options

log = logging.getLogger(__name__)


@click.group(help="National Statistical")
def main() -> None:
    pass


@main.command(help="Print team codes")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(TeamCodesReq)
def teamcodes(req: TeamCodesReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.teamcodes, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull team codes. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="League codes")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(LeagueCodesReq)
def leaguecodes(req: LeagueCodesReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.leaguecodes, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull league codes. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Print seasons")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(SeasonsReq)
def seasons(req: SeasonsReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.seasons, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull seasons. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Team data")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(TeamsReq)
def teams(req: TeamsReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.teams, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull team data. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Player data")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(PlayersReq)
def players(req: PlayersReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.players, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull player data. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Game data")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(GamesReq)
def games(req: GamesReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.games, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull game data. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Team performance data")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(TeamPerfsReq)
def teamperfs(req: TeamPerfsReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.teamperfs, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull team performance data. Error: ", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Player performance data")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(PlayerPerfsReq)
def playerperfs(req: PlayerPerfsReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.playerperfs, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull player performance data. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Play-by-play data")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(PlayByPlayReq)
def playbyplay(req: PlayByPlayReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.playbyplay, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull play-by-play data. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Venue data")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(VenuesReq)
def venues(req: VenuesReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.venues, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull venue data. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Moneyline records")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(MoneylineReq)
def moneyline(req: MoneylineReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.moneyline, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull moneyline data. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Point spread records")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(PointSpreadReq)
def pointspread(req: PointSpreadReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = api.pointspread(req)
    result = single_or_all(api.pointspread, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull point spread data. Error: %s", result)
        return
    write_resp(result, sys.stdout)


@main.command(help="Over/Under records")
@click.option(
    "--all-pages/--one-page",
    type=bool,
    default=True,
    help="Pull all pages or just one (default: all pages)",
)
@model_options(OverunderReq)
def overunder(req: OverunderReq, all_pages: bool) -> None:
    api = NatStatAPIv3()
    result = single_or_all(api.overunder, req, all_pages)
    if isinstance(result, NatStatError):
        log.error("Could not pull over/under data. Error: %s", result)
        return
    write_resp(result, sys.stdout)


def single_or_all(
    endpoint,
    req: NatStatReq,
    all_pages: bool,
) -> NatStatResp | PaginatedResp | NatStatError:
    if all_pages:
        return paginated_get_all(endpoint, req)
    return endpoint(req)


def write_resp(resp: NatStatResp | PaginatedResp, dst):
    result = resp.to_dataframe()
    if result is None:
        log.error("Could not convert response to dataframe")
        return
    result.to_csv(dst, index=False)


if __name__ == "__main__":
    main()
