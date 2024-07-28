from isaac_analyzer.logging import getLogger
from os.path import join
from isaac_analyzer.utils import get_empty_boss_count_dict, add_dicts, get_month_header
from isaac_analyzer.plotting.single_chart import hbars

logger = getLogger(__name__)


def get_boss_type(run):
    bosses = get_empty_boss_count_dict()

    for floor in run["floors"]:
        if (
            "bossRoom" in floor
            and floor["bossRoom"]["visited"]
            and floor["bossRoom"]["boss"] != "None"
        ):
            bosses[floor["bossRoom"]["boss"]] += 1
        if (
            "bossRoomXL" in floor
            and floor["bossRoomXL"]["visited"]
            and floor["bossRoom"]["boss"] != "None"
        ):
            bosses[floor["bossRoomXL"]["boss"]] += 1

    return bosses


def generate_boss_plot(analyzed_runs, output_path):
    bosses = get_empty_boss_count_dict()

    for analyzed_run in analyzed_runs:
        for run in analyzed_run["runs"]:
            bosses = add_dicts(bosses, run["analytics"]["bosses"])

    del bosses["???"]
    del bosses["Isaac"]
    del bosses["It Lives"]
    del bosses["Mom"]
    del bosses["Satan"]
    del bosses["The Lamb"]

    top_bosses = dict(
        sorted(bosses.items(), key=lambda item: item[1], reverse=True)[:12]
    )
    boss_figure = hbars(
        values=[top_bosses[boss] for boss in top_bosses],
        labels=top_bosses.keys(),
        x_label="Count",
        title=f"Top Bosses ({get_month_header(analyzed_runs[0]["date"])})",
    )

    output_file = join(output_path, "boss.png")
    boss_figure.savefig(output_file, transparent=True)
    logger.info(f"Deal plot saved to {output_file}")
