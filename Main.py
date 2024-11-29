import g4f
import asyncio

_providers = [
    #g4f.Provider.bing,
    #g4f.Provider.Anthropic,
    # g4f.Provider.Airforce,
    # g4f.Provider.AmigoChat,
    g4f.Provider.Blackbox,
    #g4f.Providerю. Pi,
    # g4f.Provider.RubiksAI,
    # g4f.Provider.TeachAnything,
    # g4f.Provider.Aichat,
    # g4f.Provider.ChatGpt,
    # g4f.Provider.Aura,
    # g4f.Provider.Pi,
]


async def run_provider (provider:g4f.Provider.BaseProvider):
    try:
        response = await  g4f.ChatCompletion.create_async(
            model = g4f.models.default,
            messages= [{"role": "user", "content": "Можешь найти работающих провайдеров для g4f?"}],
            provider = provider
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)

async def run_all():
    calls = [run_provider(provider) for provider in _providers]
    await asyncio.gather(*calls)

asyncio.run(run_all())
