from datetime import date

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.config.config import Stelselconfig
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class OppervlakteVanVertrekken(Stelselgroep):
    def __init__(
        self, peildatum: date = date.today(), config: Stelselconfig | None = None
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.oppervlakte_van_vertrekken

        super().__init__(peildatum=peildatum, config=config)


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    oppervlakte_van_vertrekken = OppervlakteVanVertrekken(peildatum=date(2024, 1, 1))
    with open(
        "tests/data/zelfstandige_woonruimten/input/41164000002.json", "r+"
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = oppervlakte_van_vertrekken.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
