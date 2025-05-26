# Dependências:
#	• python -m pip install -U nova-act playwright pydantic
#	• playwright install # primeira vez, apenas

# Chave de API | Gere em https://nova.amazon.com/act e exporte:  
#   • Linux/macOS: export NOVA_ACT_API_KEY="SUA_CHAVE"  
#   • Windows PowerShell: $env:NOVA_ACT_API_KEY="SUA_CHAVE"

from nova_act import NovaAct
from pydantic import BaseModel

class Intro(BaseModel):
    paragraph: str

with NovaAct(
    starting_page="https://en.wikipedia.org/wiki/Special:Search",
    headless=False,
) as nova:
    nova.act("type 'Artificial intelligence' in the search box and press Search")
    nova.act("click the result whose title exactly equals 'Artificial intelligence'")
    result = nova.act(
        "Return only the first paragraph of the article",
        schema=Intro.model_json_schema()
    )

    if result.matches_schema:
        print(result.parsed_response["paragraph"])
    else:
        print(result.response or "Nada encontrado")
