Архитектура, предварительный набросок

```text
llm-augmented-work-search/
├── src/
│   ├── adapters/			# загрузчики данных
│   │   ├── base.py
│   │   └── BoardX.py
│   ├── llm/
│   │   ├── agent_interface.py
│   │   ├── pure_python_agent.py
│   │   ├── langgraph_agent.py
│   │   └── prompts/
│   │       └── filter_v1.yaml
│   ├── storage/
│   │   ├── sqlite.py
│   │   └── models.py             	# pydantic + sqlmodel/alembic
│   ├── api/
│   │   ├── main.py               	# fastapp точка входа
│   │   ├── routers.py            	# /vacancies, /feedback
│   │   └── schemas.py            	# request/response models
│   └── utils/
│       ├── config.py             	# pydantic-settings
│       └── logger.py
├── config/
│   ├── llm.yaml
│   └── sources.yaml
├── scripts/
│   └── run_pipeline.py           	# cron-точка входа
├── data/
│   ├── raw/.gitkeep
│   └── processed/.gitkeep
├── tests/
│   ├── test_adapters.py
│   └── test_llm_output.py
├── .gitignore
├── pyproject.toml
├── Makefile
└── README.md
```
