import dataclasses

from original_HouYi.constant.prompt_injection import PromptInjection


@dataclasses.dataclass
class Harness:
    name: str = ""
    site_url: str = ""
    application_document: str = ""

    def run_harness(self, prompt_injection: PromptInjection):
        raise NotImplementedError
