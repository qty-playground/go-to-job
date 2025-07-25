# Go-to-Job

快速專案導航工具，幫助開發者在多個專案間快速切換並自動啟用 virtual environment。

## 功能

- 自動掃描工作目錄中的專案資料夾
- 快速切換到指定專案目錄
- 自動偵測並啟用 Python virtual environment (`venv/` 或 `.venv/`)
- 清楚顯示專案列表和環境狀態

## 安裝

**推薦使用 pipx 安裝：**

```bash
# 從 PyPI 安裝（正式版本）
pipx install go-to-job

# 或從 GitHub 安裝（最新開發版本）
pipx install git+https://github.com/qty-playground/go-to-job.git
```

> **為什麼推薦 pipx？** pipx 會將 CLI 工具安裝在獨立的 virtual environment 中，避免與其他 Python 套件衝突，同時讓指令在全域可用。

## 使用方法

### 基本指令

```bash
# 顯示所有可用專案
go-to-job

# 直接跳轉到指定專案
go-to-job my-project
```

### 使用範例

假設你的工作目錄結構如下：

```
~/workspace/
├── web-app/          # 有 venv/ 目錄
├── api-server/       # 有 .venv/ 目錄  
├── data-analysis/    # 無 virtual environment
└── scripts/          # 無 virtual environment
```

**列出所有專案：**

```bash
$ go-to-job
Available projects:
  1. web-app (venv available)
  2. api-server (venv available)
  3. data-analysis
  4. scripts

Select project [1-4]: 1
Switching to: ~/workspace/web-app
Virtual environment activated: venv
```

**直接跳轉到專案：**

```bash
$ go-to-job api-server
Switching to: ~/workspace/api-server
Virtual environment activated: .venv
```

**沒有 virtual environment 的專案：**

```bash
$ go-to-job scripts
Switching to: ~/workspace/scripts
(No virtual environment found)
```

