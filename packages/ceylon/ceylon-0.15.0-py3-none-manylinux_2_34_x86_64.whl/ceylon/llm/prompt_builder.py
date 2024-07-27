import re

from Cheetah.Template import Template


def get_agent_definition(
        agent_config: dict
):
    cleaned_string = Template("""    
    You are $name, an AI agent whose role is $role.
        Your objective is to $objective.    
        Your context is $context.
        
        As an AI agent, you should strive to provide accurate, helpful, 
        and contextually appropriate responses based on the above specifications. 
        Always maintain the defined interaction style and adhere to the operational parameters. 
        If you encounter a task outside your defined capabilities or knowledge domains, please 
        inform the user and offer alternative solutions if possible.
""", agent_config)
    # cleaned_string = re.sub(r'\s+', ' ', f"{template}")
    # cleaned_string = cleaned_string.strip()
    return cleaned_string


def get_prompt(agent_config: dict):
    template = Template("""
    $agent_definition
    You need to follow your responsibility. to complete the task.
    --------------
    User Inputs: $user_inputs
   
    #if $history
     ------------
        Other Agents Responses:
        #for $key, $value in $history.items()
            $key: $value
        #end for
    #end if
            """, agent_config)
    cleaned_string = re.sub(r'\s+', ' ', f"{template}")
    cleaned_string = cleaned_string.strip()
    return cleaned_string


def job_planing_prompt(job_config: dict):
    template = Template("""                
                You are an AI system coordinating a team of specialized agents:
                #for $worker in $workers
                    .....
                    #for $key, $value in $worker.items()
                                $key: $value
                    #end for
                    .....
                #end for
                User request
                #for $key, $value in $job.items()
                            $key: $value
                #end for
                Your goal is to determine the optimal workflow for execute this user request. dependencies and owner must be agents names.   
            """, job_config)

    cleaned_string = re.sub(r'\s+', ' ', f"{template}")
    cleaned_string = cleaned_string.strip()
    return cleaned_string


if __name__ == '__main__':
    from ceylon.llm.types import AgentDefinition

    conf = AgentDefinition(
        name="Researcher",
        role="researcher",
        responsibility="Search the internet",
        skills=["search"],
        tools=[]
    ).model_dump()
    print(conf)

    print(get_agent_definition(conf))
