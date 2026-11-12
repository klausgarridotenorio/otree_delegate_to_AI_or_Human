import socket
from os import environ

LOCAL_NAMES = ['glendronach', 'awesom-o-4000',
               'Klauss-MacBook-Pro.local', 'Asus-Tuf-Dash-f15', 'mac.home']


def get_active_classes(config: dict) -> dict[str, dict[str, int]]:
    from common import CLASS_DICT
    return {class_name: params
            for class_name, params in CLASS_DICT.items()
            if config.get(class_name) is True}


SESSION_CONFIGS = [
    dict(
        name='Full_Experiment',
        display_name='Full Experiment',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
    ),
    dict(
        name='Experiment',
        app_sequence=['experiment'],
        num_demo_participants=4,
    ),
    dict(
        name='Intro',
        app_sequence=['intro'],
        num_demo_participants=4,
    ),
    dict(
        name='1_C_Supplier_First_AI',
        display_name='1_C_Supplier_First_AI',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=False,
        force_supplier_first=True,
        force_retailer_first=False,
        class_a=False,
        class_b=False,
        class_c=True,
    ),
    dict(
        name='2_C_Supplier_First_Human',
        display_name='2_C_Supplier_First_Human',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=True,
        force_supplier_first=True,
        force_retailer_first=False,
        class_a=False,
        class_b=False,
        class_c=True,
    ),
    dict(
        name='3_B_Retailer_First_AI',
        display_name='3_B_Retailer_First_AI',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=False,
        force_supplier_first=False,
        force_retailer_first=True,
        class_a=False,
        class_b=True,
        class_c=False,
    ),
    dict(
        name='4_B_Retailer_First_Human',
        display_name='4_B_Retailer_First_Human',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=True,
        force_supplier_first=False,
        force_retailer_first=True,
        class_a=False,
        class_b=True,
        class_c=False,
    ),
    dict(
        name='5_A_Supplier_First_AI',
        display_name='5_A_Supplier_First_AI',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=False,
        force_supplier_first=True,
        force_retailer_first=False,
        class_a=True,
        class_b=False,
        class_c=False,
    ),
    dict(
        name='6_A_Supplier_First_Human',
        display_name='6_A_Supplier_First_Human',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=True,
        force_supplier_first=True,
        force_retailer_first=False,
        class_a=True,
        class_b=False,
        class_c=False,
    ),
    dict(
        name='7_C_Retailer_First_AI',
        display_name='7_C_Retailer_First_AI',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=False,
        force_supplier_first=False,
        force_retailer_first=True,
        class_a=False,
        class_b=False,
        class_c=True,
    ),
    dict(
        name='8_C_Retailer_First_Human',
        display_name='8_C_Retailer_First_Human',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=True,
        force_supplier_first=False,
        force_retailer_first=True,
        class_a=False,
        class_b=False,
        class_c=True,
    ),
    dict(
        name='9_B_Supplier_First_AI',
        display_name='9_B_Supplier_First_AI',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=False,
        force_supplier_first=True,
        force_retailer_first=False,
        class_a=False,
        class_b=True,
        class_c=False,
    ),
    dict(
        name='10_B_Supplier_First_Human',
        display_name='10_B_Supplier_First_Human',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=True,
        force_supplier_first=True,
        force_retailer_first=False,
        class_a=False,
        class_b=True,
        class_c=False,
    ),
    dict(
        name='11_A_Retailer_First_AI',
        display_name='11_A_Retailer_First_AI',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=False,
        force_supplier_first=False,
        force_retailer_first=True,
        class_a=True,
        class_b=False,
        class_c=False,
    ),
    dict(
        name='12_A_Retailer_First_Human',
        display_name='12_A_Retailer_First_Human',
        app_sequence=['intro', 'experiment'],
        num_demo_participants=4,
        baseline=True,
        force_supplier_first=False,
        force_retailer_first=True,
        class_a=True,
        class_b=False,
        class_c=False,
    )
]




SESSION_CONFIG_DEFAULTS = {
    'room': -1,

    'force_retailer_first': False,
    'force_supplier_first': False,
    'baseline': False,

    'timeout_experiment': 5 * 60,

    # Fixed market price and production cost are only used in test
    # Will be randomized if not set to >= 0
    'market_price': -1,
    'production_cost': -1,

    # For experiment, always randomize the values
    'market_price_low': 10,
    'market_price_high': 12,
    'production_cost_low': 3,
    'production_cost_high': 5,
    'demand_min': 0,
    'demand_max': 100,

    'delegation_cost_1': 20,
    'delegation_cost_2': 10,

    'class_a': True,
    'class_b': True,
    'class_c': True,

    # TODO gemma3?
    'llm_user': 'otree',
    'llm_pass': 'ped+GlubbomOnEc4',
    'llm_model': 'llama3', #llama3
    'llm_temp': 0.1,
    # TODO v3?
    'llm_reader': 'offer_reader_v2',

    "https://ollama1.src-automating.src.surf-hosted.nl": True,
    "https://ollama2.src-automating.src.surf-hosted.nl": True,
    "https://ollama3.src-automating.src.surf-hosted.nl": True,
    "https://ollama4.src-automating.src.surf-hosted.nl": True,
    "https://ollama5.src-automating.src.surf-hosted.nl": True,
    "https://ollama6.src-automating.src.surf-hosted.nl": True,
    "https://ollama7.src-automating.src.surf-hosted.nl": True,

    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,

    'doc': "",
}

ROOMS = [
    dict(
        name='1',
        display_name='1_C_Supplier_First_AI',
    ),
    dict(
        name='2',
        display_name='2_C_Supplier_First_Human'
    ),
    dict(
        name='3',
        display_name='3_B_Retailer_First_AI',
    ),
    dict(
        name='4',
        display_name='4_B_Retailer_First_Human'
    ),
    dict(
        name='5',
        display_name='5_A_Supplier_First_AI',
    ),
    dict(
        name='6',
        display_name='6_A_Supplier_First_Human'
    ),
    dict(
        name='7',
        display_name='7_C_Retailer_First_AI',
    ),
    dict(
        name='8',
        display_name='8_C_Retailer_First_Human'
    ),
    dict(
        name='9',
        display_name='9_B_Supplier_First_AI',
    ),
    dict(
        name='10',
        display_name='10_B_Supplier_First_Human'
    ),
    dict(
        name='11',
        display_name='11_A_Retailer_First_AI'
    ),
    dict(
        name='12',
        display_name='12_A_Retailer_First_Human'
    ), 
]

CONFIG = SESSION_CONFIG_DEFAULTS

hostname = socket.gethostname()
if hostname in LOCAL_NAMES[:2]:
    CONFIG['timeout_experiment'] *= 100

if hostname in LOCAL_NAMES:
    # Each non-existent host adds 5 seconds to Session initialization
    for key in [k for k in CONFIG.keys() if k.startswith('http')]:
        CONFIG[key] = False
    # Otree on Awesom-o with Ollama on Glendronach
    if hostname == LOCAL_NAMES[1]:  # and False:
        CONFIG["http://192.168.199.13:11434"] = True
    else:
        CONFIG["http://localhost:11434"] = True

PARTICIPANT_FIELDS = ['role', 'choice']
SESSION_FIELDS = ['first_mover_role', 'llm_hosts']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5388071882920'
