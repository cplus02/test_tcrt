# TCRT Sample Automation Repo

可以拿來給 TCRT Automation Hub 連接的範例 git repo 結構。**這不是 TCRT 自己跑的測試**，是給「使用 TCRT 的人」當作他們自動化測試 repo 的最小參考骨架。

這個 repo 示範了 TCRT 目前支援的**全部** GitHub repo 功能：

- 所有支援的測試檔格式（PYTEST / PLAYWRIGHT_PY_ASYNC / PLAYWRIGHT_JS）
- `@pytest.mark.tcrt` marker（Python，含單一 TC、多 TC、stacked markers、class-level）
- `// tcrt:` comment marker（JS / TS，含 `link_type` 全三種值、多 TC ID）
- `tcrt-automation.yml` manifest（路徑 override、contract 驗證）
- `conftest.py` 中的 `pytest_configure` 以避免 `--strict-markers` 報錯
- 排除邏輯展示（`__init__.py`、`conftest.py`、`pages/`、`flows/`、`fixtures/`）

## 如何連接 TCRT

1. Push 整個 repo 到一個 GitHub repo
2. TCRT → **Automation Hub → Git Sources → Add Git Repo**：
   - `owner` / `repo`：剛 push 的 repo
   - `default_branch`：`main`
   - `scan_path`：`tests/`（manifest 中也有指定，兩者一致）
   - `auth_method`：`pat`，填有 `repo` scope 的 PAT
3. 跑 **Smart Scan**，應該偵測到：

| 格式 | 檔案 | 掃描到的 test 數 |
|---|---|---|
| PYTEST | `tests/api/test_user_auth.py` | 3 functions + 1 class (2 methods) |
| PYTEST | `tests/api/test_admin_apis.py` | 4 functions |
| PYTEST | `tests/api/ticket_api_test.py` | 4 functions |
| PYTEST | `tests/api/user_profile_test.py` | 3 functions |
| PLAYWRIGHT_PY_ASYNC | `tests/e2e/flow_purchase.py` | 2 functions |
| PLAYWRIGHT_PY_ASYNC | `tests/e2e/flow_signup.py` | 3 functions |
| PLAYWRIGHT_JS | `tests/ui/login.spec.ts` | 3 tests |
| PLAYWRIGHT_JS | `tests/ui/homepage.spec.ts` | 3 tests |
| PLAYWRIGHT_JS | `tests/ui/checkout.test.js` | 3 tests |

排除（不出現在 Hub）：`conftest.py` × 2、`__init__.py` × 3

## 目錄結構

```
tcrt-automation.yml       ← TCRT manifest（paths / scan config）
conftest.py               ← root conftest：pytest_configure 註冊 tcrt marker
pytest.ini                ← --strict-markers；markers 清單含 tcrt
playwright.config.ts      ← Playwright 配置（tests/ui/）
package.json
pages/                    ← Page Object 目錄（TCRT 掃描排除）
flows/                    ← 複合流程目錄（TCRT 掃描排除）
fixtures/                 ← 共享 fixture 目錄（TCRT 掃描排除）
tests/
├── __init__.py
├── api/
│   ├── __init__.py       ← 排除
│   ├── conftest.py       ← 排除
│   ├── test_user_auth.py     ✅ PYTEST — @pytest.mark.tcrt，含 stacked + multi-TC + class-level
│   ├── test_admin_apis.py    ✅ PYTEST — @pytest.mark.tcrt，primary / covers 示範
│   ├── ticket_api_test.py    ✅ PYTEST（*_test.py 命名）
│   └── user_profile_test.py  ✅ PYTEST（*_test.py 命名）
├── e2e/
│   ├── __init__.py       ← 排除
│   ├── flow_purchase.py  ✅ PLAYWRIGHT_PY_ASYNC — @pytest.mark.tcrt
│   └── flow_signup.py    ✅ PLAYWRIGHT_PY_ASYNC — @pytest.mark.tcrt
└── ui/
    ├── login.spec.ts     ✅ PLAYWRIGHT_JS — // tcrt: 含 multi-TC、references、cross-script TC
    ├── homepage.spec.ts  ✅ PLAYWRIGHT_JS — // tcrt: 含 primary / covers / default
    └── checkout.test.js  ✅ PLAYWRIGHT_JS（.test.js 命名）— // tcrt: 含 multi-TC
```

## TCRT Marker 功能展示清單

### Python — `@pytest.mark.tcrt`

| 功能 | 出現位置 |
|---|---|
| 單一 TC ID + `link_type="primary"` | `test_user_auth.py:test_login_with_valid_credentials` |
| 單一 TC ID + `link_type="covers"` | `test_user_auth.py:test_login_with_invalid_password_returns_401` |
| Stacked markers（多個 @pytest.mark.tcrt 疊加） | `test_user_auth.py:test_logout_clears_session` |
| Class-level marker（一個 marker 覆蓋整個 class） | `test_user_auth.py:TestPasswordReset` |
| Multi-TC ID（一個 marker 多個 tc_ids） | `test_user_auth.py:TestPasswordReset` |
| `link_type="primary"` | `test_admin_apis.py:test_create_team_as_admin` |
| PLAYWRIGHT_PY_ASYNC 格式也可用 marker | `flow_purchase.py`, `flow_signup.py` |

### JS / TypeScript — `// tcrt:`

| 功能 | 出現位置 |
|---|---|
| 單一 TC ID + `[primary]` | `homepage.spec.ts:homepage shows hero section` |
| 單一 TC ID + `[covers]` | `homepage.spec.ts:search box autocompletes` |
| 單一 TC ID（預設 covers，省略 link_type） | `homepage.spec.ts:navigation bar contains primary links` |
| 單一 TC ID + `[references]` | `login.spec.ts:renders login form on first visit` |
| Multi-TC ID（逗號分隔） | `login.spec.ts:redirects to dashboard after successful login` |
| `.test.js` 格式（非 .spec.js）同樣支援 | `checkout.test.js` |

### Cross-script TC Coverage（一個 TC 被多支腳本覆蓋）

TC ID 對應真實 CRD test case。CRD 的 `test_case_number` 帶點號（如 `TCG-107489.050.010`），但 marker 的 tc_id 文法只允許 `[A-Za-z0-9_-]`，所以 marker 一律把點改成 dash 寫（`TCG-107489-050-010`）；TCRT marker 同步時會把 `test_case_number` 正規化成 dash 形式來比對。

| TC ID（marker dash 形式 → 真實編號） | 涵蓋的腳本 |
|---|---|
| `TCG-107489-050-010`（= `TCG-107489.050.010`） | `test_user_auth.py`（primary）、`login.spec.ts`（references + covers）|
| `TCG-107489-060-010`（= `TCG-107489.060.010`） | `test_user_auth.py`（covers）、`login.spec.ts`（covers）|
| `TCG-107489-070-010`（= `TCG-107489.070.010`） | `test_user_auth.py`（primary + referenced）、`login.spec.ts`（covers）|
| `TCG-107489-130-010`（= `TCG-107489.130.010`） | `flow_purchase.py`（primary）、`checkout.test.js`（covers × 2）|
| `TCG-107489-140-010`（= `TCG-107489.140.010`） | `flow_purchase.py`（covers）、`checkout.test.js`（covers）|

## TCRT 格式規則速查

| 副檔名 / 命名 | `script_format` |
|---|---|
| `.spec.ts` / `.test.ts` / `.spec.js` / `.test.js` | `PLAYWRIGHT_JS` |
| `.py` 且 `test_*` 或 `*_test.py` | `PYTEST` |
| 其他 `.py` | `PLAYWRIGHT_PY_ASYNC` |
| 其餘 | `OTHER`（不被 smart-scan 收）|

`--strict-markers` 注意事項：`pytest.ini` 中已列 `tcrt` marker，root `conftest.py` 中也有 `pytest_configure` 雙重保險。
