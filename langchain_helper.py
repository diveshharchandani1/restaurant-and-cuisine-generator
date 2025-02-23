from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

llm = Ollama(model="llama3.2:3b", temperature=0.7)  

def generate_restaurant_name_and_items(cuisine):  
    # Chain 1: Restaurant Name
    prompt_template_res_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a {cuisine} restaurant. Please suggest one fancy name, no explanation."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_res_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_menu_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest menu items for {restaurant_name}. Return as comma-separated list. Give me the menu items directly no need to give me any explanation before that"
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_menu_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )
    response = chain({'cuisine': cuisine})  
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Indian"))  
