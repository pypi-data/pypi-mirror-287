from .questAgents import quest_brainstormer, quest_refiner, quest_formatter

def generate_quest(quest_prompt, objective_info, character_info, location_info):
    
    initial_generated_quest = quest_brainstormer.generate_quest(objective_info, quest_prompt, character_info, location_info)
    
    quest_with_objectives = quest_refiner.define_quest_objectives(initial_generated_quest)
    
    reward = quest_refiner.define_quest_reward(initial_generated_quest)
    
    formatted_quest = quest_formatter.format_quest(quest_with_objectives, reward)
    
    return formatted_quest
    