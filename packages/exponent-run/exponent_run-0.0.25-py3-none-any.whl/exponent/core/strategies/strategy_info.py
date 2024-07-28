# Auto-generated, do not edit directly. Run `make generate_strategy_types` to update.

from pydantic import BaseModel

from .strategy_name import StrategyName


class StrategyInfo(BaseModel):
    strategy_name: StrategyName
    display_name: str
    description: str
    disabled: bool = False
    display_order: int = 99


def get_strategy_info(strategy_name: StrategyName) -> StrategyInfo:
    strategy_info: StrategyInfo

    if strategy_name == StrategyName.ANT_FULL_FILE_REWRITE:
        strategy_info = StrategyInfo(
            strategy_name=StrategyName.ANT_FULL_FILE_REWRITE,
            display_name="Full File Rewrites",
            description="Rewrites the full file every time. Use this if your files are generally less than 300 lines.",
            disabled=False,
            display_order=99,
        )
    elif strategy_name == StrategyName.ANT_UDIFF:
        strategy_info = StrategyInfo(
            strategy_name=StrategyName.ANT_UDIFF,
            display_name="Unified Diff (Ant)",
            description="Generates diffs to edit files",
            disabled=False,
            display_order=99,
        )
    elif strategy_name == StrategyName.ANT_SEARCH_REPLACE:
        strategy_info = StrategyInfo(
            strategy_name=StrategyName.ANT_SEARCH_REPLACE,
            display_name="Search and Replace (Ant)",
            description="Replaces chunks of code with new version of code. Recommended strategy for larger more complex files.",
            disabled=False,
            display_order=99,
        )

    else:
        raise ValueError(f"Unknown strategy name: {strategy_name}")

    return strategy_info
