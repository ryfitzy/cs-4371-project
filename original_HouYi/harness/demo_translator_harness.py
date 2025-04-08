import dataclasses

import loguru
from constant.prompt_injection import PromptInjection

from harness.base_harness import Harness
from original_HouYi.util.ollama_util import chat_completion

logger = loguru.logger


@dataclasses.dataclass
class TranslatorHarness(Harness):
    name: str = "demo_translator"
    site_url: str = "demo.url"
    application_document: str = "This app can be used to translate English to French."

    def run_harness(self, prompt_injection: PromptInjection):
        prompt = prompt_injection.get_attack_prompt()
        application_prompt = f"This is a translator of translating English to French: {prompt}"
        logger.info(f"Application Prompt: {application_prompt}")
        response = chat_completion(application_prompt)
        logger.info(f"Response: {response}")
        return response
