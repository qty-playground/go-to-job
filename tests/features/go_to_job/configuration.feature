Feature: 工作資料夾配置管理
    身為一個開發者
    我想要靈活配置我的工作資料夾位置
    這樣我就能適應不同的工作環境

    Background:
        Given 我有 go-to-job 工具

    Scenario: 使用預設工作資料夾 ~/temp
        """
        當沒有設定時，使用預設的 ~/temp 目錄
        """
        Given 沒有設定工作資料夾
        When 我執行 go-to-job 指令
        Then 應該掃描 "~/temp" 目錄中的專案

    Scenario: 透過環境變數指定工作資料夾
        """
        透過 GOTOJOB_WORK_DIR 環境變數指定工作目錄
        """
        Given 我設定環境變數 "GOTOJOB_WORK_DIR" 為 "~/projects"
        When 我執行 go-to-job 指令
        Then 應該掃描 "~/projects" 目錄中的專案

    Scenario: 透過設定檔指定工作資料夾
        """
        透過設定檔 ~/.go-to-job.conf 指定工作目錄
        """
        Given 我有設定檔 "~/.go-to-job.conf" 內容為 "work_dir=~/my-workspace"
        When 我執行 go-to-job 指令
        Then 應該掃描 "~/my-workspace" 目錄中的專案

    Scenario: 配置優先順序：環境變數優於設定檔
        """
        當同時有環境變數和設定檔時，環境變數應該優先
        """
        Given 我有設定檔 "~/.go-to-job.conf" 內容為 "work_dir=~/workspace"
        And 我設定環境變數 "GOTOJOB_WORK_DIR" 為 "~/priority-projects"
        When 我執行 go-to-job 指令
        Then 應該掃描 "~/priority-projects" 目錄中的專案