import logging
import locale
from SapGuiLibrary import SapGuiLibrary
from dotenv import load_dotenv

from hnt_sap_financeiro.fv60_transaction import Fv60Transaction

from .common.session import sessionable


logger = logging.getLogger(__name__)

class SapGui(SapGuiLibrary):
    def __init__(self) -> None:
        SapGuiLibrary.__init__(self, screenshots_on_error=True)
        locale.setlocale(locale.LC_ALL, ('pt_BR.UTF-8'))
        load_dotenv()
        pass
    def format_float(self, value):
        return locale.format_string("%.2f", value)

    @sessionable
    def run_FV60(self, taxa):
        logger.info(f"Enter execute run_FV60 taxa:{taxa}")
        results = {
            "fv60": None,
            "error": None
        }
        try:
            results['fv60'] = Fv60Transaction().execute(self, taxa)
            print('run FV60')
        except Exception as ex:
            logger.error(str(ex))
            results["error"] = str(ex)
        logger.info(f"Leave execute run_hnt_transactions result:{', '.join([str(results[obj]) for obj in results])}")
        return results
