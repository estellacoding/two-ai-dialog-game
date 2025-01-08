# AI 角色對話遊戲
受到 ihower 在 WebConf Taiwan 2024 的 [演講內容](https://ihower.tw/blog/archives/12444) 啟發，做了這個簡單的 AI 角色對話遊戲。

# 主要功能
- 支持多模型: OpenAI GPT、Anthropic Claude、Google Gemini、Mistral 及 xAI Grok。
- 自定義角色: 為3個角色(防守者、挑戰者與評估者)選擇模型及自定義提示詞。
- 多輪對話: 進行防守者與挑戰者之間的多輪對話，並即時記錄對話過程。
- 表現評估: 通過評估者對防守者和挑戰者的表現，進行詳細評估和建議。
- 可視化界面: Streamlit 的視覺化界面，便於操作與即時查看對話結果。

# 前置步驟
## 複製專案
```
git clone https://github.com/estellacoding/two-ai-dialog-game.git
cd two-ai-dialog-game
```
## 安裝套件
```
pip install -r requirements.txt
```

## 設定環境變數
在專案目錄下建立 .streamlit 資料夾及 secrets.toml 檔案。
```
# .streamlit/secrets.toml
# OpenAI GPT API
GPT_API_KEY = <your OpenAI API key>
# Anthropic Claude API
CLAUDE_API_KEY = <your Claude API key>
# Google Gemini API
GEMINI_API_KEY = <your Gemini API key>
# Mistral API
MISTRAL_API_KEY = <your Mistral API key>
# xAI GROK API
GROK_API_API = <your Grok API key>
```

## 專案結構
```
two-ai-dialog-game/
├── app.py                     # 主應用程式
├── dialog_simulation.py       # AI 對話核心邏輯
├── llm_checker.py             # 模型金鑰檢查
├── requirements.txt           # 需安裝的 Python 套件
└── README.md                  # 專案說明
└── .streamlit/secrets.toml    # 設定環境變數
```

# 執行程式
## 啟動 Streamlit
```
streamlit run app.py
```

## 開啟瀏覽器
開啟瀏覽器，進入 localhost:8501，即可使用專案介面。

# 立即體驗
進入 [AI 角色對話遊戲](https://two-ai-dialog-game.streamlit.app/) 吧!