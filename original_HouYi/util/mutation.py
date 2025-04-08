# MODIFIED BY CS4371

from constant.chromosome import Chromosome

from util.openai_util import completion_with_chatgpt


def llm_mutation_generation(chromosome: Chromosome):
    disruptor_prompt = chromosome.disruptor
    framework_prompt = chromosome.framework
    separator_prompt = chromosome.separator

    mutation_generation_prompt = f"""Please rephrase the following prompt to maintain its original intent and meaning, there are **three** individual prompts that need to be rephrased, and you should output in the same order and format as the input, do not include any additional information or change the order of the prompts.

=========Framework Prompt Begin=========
{framework_prompt}
=========Framework Prompt End=========
=========Separator Prompt Begin=========
{separator_prompt}
=========Separator Prompt End=========
=========Disruptor Prompt Begin=========
{disruptor_prompt}
=========Disruptor Prompt End=========


Provide a revised version that captures the essence and core
message of the original prompt, ensuring clarity and coherence
in the rephrased content.
    """
    response = completion_with_chatgpt(mutation_generation_prompt)

    # print(f"FULL RESPONSE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n{response}\n")
    # framework_start, framework_end = (
    #     response.find("=========Framework Prompt Begin=========") + len("=========Framework Prompt Begin========="),
    #     response.find("=========Framework Prompt End========="),
    # )
    # separator_start, separator_end = (
    #     response.find("=========Separator Prompt Begin=========") + len("=========Separator Prompt Begin========="),
    #     response.find("=========Separator Prompt End========="),
    # )
    # disruptor_start, disruptor_end = (
    #     response.find("=========Disruptor Prompt Begin=========") + len("=========Disruptor Prompt Begin========="),
    #     response.find("=========Disruptor Prompt End=========")
    # )

    # split the response into three parts
    new_framework_prompt, new_separator_prompt, new_disruptor_prompt = (
        response.split("=========Framework Prompt End=========")[0]
        .split("=========Framework Prompt Begin=========")[1]
        .strip(),
        response.split("=========Separator Prompt End=========")[0]
        .split("=========Separator Prompt Begin=========")[1]
        .strip(),
        response.split("=========Disruptor Prompt End=========")[0]
        .split("=========Disruptor Prompt Begin=========")[1]
        .strip(),
        # response[framework_start:framework_end].strip(),
        # response[separator_start:separator_end].strip(),
        # response[disruptor_start:disruptor_end].strip(),
    )
    chromosome.framework = new_framework_prompt
    chromosome.separator = new_separator_prompt
    chromosome.disruptor = new_disruptor_prompt
    return chromosome
