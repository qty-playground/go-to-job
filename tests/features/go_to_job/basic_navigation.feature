Feature: 基本專案導航功能
    身為一個開發者
    我想要快速切換到我的工作專案
    這樣我就能快速開始工作

    Background:
        Given 我有一些專案在工作資料夾

    Scenario: 列出可用的專案
        """
        測試基本功能：掃描並顯示工作目錄中的專案
        """
        Given 我在工作目錄有多個專案
        When 我執行 go-to-job 指令
        Then 我應該看到可用專案的清單

    Scenario: 選擇專案並切換目錄
        """
        測試選擇專案後的導航功能
        """
        Given 我在工作目錄有專案 "web-app"
        When 我執行 go-to-job 指令
        And 我選擇 "web-app" 專案
        Then 我應該切換到 "web-app" 目錄

    Scenario: 自動啟用虛擬環境
        """
        如果專案有 venv 資料夾，應該自動啟用虛擬環境
        """
        Given 我的專案 "api-server" 有虛擬環境
        When 我執行 go-to-job 指令
        And 我選擇 "api-server" 專案
        Then 我應該切換到專案目錄
        And 虛擬環境應該被自動啟用

    Scenario: 處理沒有虛擬環境的專案
        """
        對於沒有 venv 的專案，只切換目錄不啟用環境
        """
        Given 我的專案 "simple-scripts" 沒有虛擬環境
        When 我執行 go-to-job 指令
        And 我選擇 "simple-scripts" 專案
        Then 我應該切換到專案目錄
        And 不應該嘗試啟用虛擬環境